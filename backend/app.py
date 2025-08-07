from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timedelta
import pickle
import pandas as pd
import numpy as np
import json
import os
import logging
from werkzeug.exceptions import BadRequest

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///neuroshield.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'neuroshield-secret-key-2025'

# Initialize extensions
CORS(app)
db = SQLAlchemy(app)

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Database Models
class ThreatLog(db.Model):
    __tablename__ = 'threat_logs'

    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    ip = db.Column(db.String(15), nullable=False)
    method = db.Column(db.String(10))
    endpoint = db.Column(db.String(255))
    payload = db.Column(db.Text)
    response_time = db.Column(db.Integer)
    status_code = db.Column(db.Integer)
    user_agent = db.Column(db.Text)
    threat_type = db.Column(db.String(50))
    confidence_score = db.Column(db.Float)

    def to_dict(self):
        return {
            'id': self.id,
            'timestamp': self.timestamp.isoformat() if self.timestamp else None,
            'ip': self.ip,
            'method': self.method,
            'endpoint': self.endpoint,
            'payload': self.payload,
            'response_time': self.response_time,
            'status_code': self.status_code,
            'threat_type': self.threat_type,
            'confidence_score': self.confidence_score
        }

class Detection(db.Model):
    __tablename__ = 'detections'

    id = db.Column(db.Integer, primary_key=True)
    log_id = db.Column(db.Integer, db.ForeignKey('threat_logs.id'))
    threat_type = db.Column(db.String(50))
    confidence_score = db.Column(db.Float)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            'id': self.id,
            'log_id': self.log_id,
            'threat_type': self.threat_type,
            'confidence_score': self.confidence_score,
            'timestamp': self.timestamp.isoformat()
        }

class BlockedIP(db.Model):
    __tablename__ = 'blocked_ips'

    id = db.Column(db.Integer, primary_key=True)
    ip = db.Column(db.String(15), nullable=False)
    reason = db.Column(db.Text)
    blocked_at = db.Column(db.DateTime, default=datetime.utcnow)
    status = db.Column(db.String(20), default='active')

    def to_dict(self):
        return {
            'id': self.id,
            'ip': self.ip,
            'reason': self.reason,
            'blocked_at': self.blocked_at.isoformat(),
            'status': self.status
        }

# Simple ML threat detection
def extract_features(log_data):
    """Extract ML features from log data"""
    payload = log_data.get('payload', '')
    endpoint = log_data.get('endpoint', '')

    features = [
        len(payload),
        payload.lower().count('select'),
        payload.lower().count('union'),
        payload.lower().count('script'),
        payload.lower().count('alert'),
        payload.lower().count('admin'),
        payload.lower().count('password'),
        log_data.get('response_time', 0),
        log_data.get('status_code', 200),
        1 if log_data.get('method') == 'POST' else 0,
        1 if '/admin' in endpoint else 0,
        1 if '/login' in endpoint else 0,
    ]
    return features

def classify_threat_type(log_data):
    """Classify the type of threat"""
    payload = log_data.get('payload', '').lower()
    endpoint = log_data.get('endpoint', '').lower()

    if any(sql_pattern in payload for sql_pattern in ['select', 'union', 'drop', 'insert', "'"]):
        return 'SQLi'
    elif any(xss_pattern in payload for xss_pattern in ['script', 'alert', 'onerror', '<', '>']):
        return 'XSS'
    elif 'admin' in endpoint and log_data.get('method') == 'POST':
        return 'Brute Force'
    elif log_data.get('response_time', 0) > 5000:
        return 'DDoS'
    elif any(scan_pattern in endpoint for scan_pattern in ['.php', '.asp', '.jsp']):
        return 'Port Scan'
    else:
        return 'Unknown'

def calculate_threat_probability(features):
    """Simple threat probability calculation - DEMO MODE"""
    score = 0.0

    # Payload length indicator
    if features[0] > 50:
        score += 0.4  # was 0.2

    # SQL injection patterns
    if features[1] > 0 or features[2] > 0:  # select, union
        score += 0.6  # was 0.4

    # XSS patterns  
    if features[3] > 0 or features[4] > 0:  # script, alert
        score += 0.6  # was 0.4

    # Admin/password patterns
    if features[5] > 0 or features[6] > 0:
        score += 0.7  # was 0.5

# Error status codes
    if features[8] in [500, 403, 401]:
        score += 0.5  # was 0.3


    # Error status codes
    if features[8] in [500, 403, 401]:
        score += 0.3  # was 0.1

    # Admin endpoints with POST
    if features[9] and features[10]:
        score += 0.5  # was 0.3

    return min(score, 1.0)


# API Routes
@app.route('/api/logs', methods=['POST'])
def ingest_log():
    """Ingest and analyze incoming logs"""
    try:
        data = request.get_json()

        if not data:
            raise BadRequest("No JSON data provided")

        # Extract features and classify threat
        features = extract_features(data)
        threat_probability = calculate_threat_probability(features)
        threat_type = classify_threat_type(data)

        is_threat = threat_probability > 0.2

        # Create log entry
        log_entry = ThreatLog(
            timestamp=datetime.now(),
            ip=data.get('ip'),
            method=data.get('method'),
            endpoint=data.get('endpoint'),
            payload=data.get('payload', ''),
            response_time=data.get('response_time_ms', 0),
            status_code=data.get('status_code', 200),
            user_agent=data.get('user_agent', ''),
            threat_type=threat_type if is_threat else None,
            confidence_score=threat_probability if is_threat else 0.1
        )

        db.session.add(log_entry)

        # If high confidence threat, create detection and potentially block IP
        if is_threat:
            detection = Detection(
                log_id=log_entry.id,
                threat_type=threat_type,
                confidence_score=threat_probability,
                timestamp=datetime.now()
            )
            db.session.add(detection)

            # Auto-block high confidence threats
            if threat_probability > 0.8:
                existing_block = BlockedIP.query.filter_by(ip=data.get('ip'), status='active').first()
                if not existing_block:
                    blocked_ip = BlockedIP(
                        ip=data.get('ip'),
                        reason=f"{threat_type} detected with {threat_probability:.2f} confidence",
                        blocked_at=datetime.now(),
                        status='active'
                    )
                    db.session.add(blocked_ip)

        db.session.commit()

        return jsonify({
            'status': 'success',
            'threat_detected': is_threat,
            'threat_type': threat_type if is_threat else None,
            'confidence': threat_probability
        })

    except Exception as e:
        logger.error(f"Error processing log: {e}")
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@app.route('/api/logs', methods=['GET'])
def get_logs():
    """Retrieve paginated logs"""
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 50, type=int)

    logs = ThreatLog.query.order_by(ThreatLog.timestamp.desc()).paginate(
        page=page, per_page=per_page, error_out=False
    )

    return jsonify({
        'logs': [log.to_dict() for log in logs.items],
        'total': logs.total,
        'pages': logs.pages,
        'current_page': page
    })

@app.route('/api/stats', methods=['GET'])
def get_stats():
    """Get real-time system statistics"""
    total_logs = ThreatLog.query.count()
    total_threats = Detection.query.count()
    blocked_ips_count = BlockedIP.query.filter_by(status='active').count()

    # Threat distribution
    threat_types = db.session.query(
        Detection.threat_type,
        db.func.count(Detection.id).label('count')
    ).group_by(Detection.threat_type).all()

    # Recent threats
    recent_threats = Detection.query.order_by(Detection.timestamp.desc()).limit(10).all()

    return jsonify({
        'total_logs': total_logs,
        'total_threats': total_threats,
        'blocked_ips': blocked_ips_count,
        'threat_distribution': {t.threat_type: t.count for t in threat_types},
        'recent_threats': [threat.to_dict() for threat in recent_threats]
    })

@app.route('/api/blocked-ips', methods=['GET'])
def get_blocked_ips():
    """Get list of blocked IPs"""
    blocked_ips = BlockedIP.query.filter_by(status='active').order_by(BlockedIP.blocked_at.desc()).all()
    return jsonify([ip.to_dict() for ip in blocked_ips])

@app.route('/api/export/<format>', methods=['GET'])
def export_data(format):
    """Export data in CSV or JSON format"""
    try:
        if format == 'csv':
            logs = ThreatLog.query.all()
            df = pd.DataFrame([log.to_dict() for log in logs])
            filename = f'logs_export_{datetime.now().strftime("%Y%m%d_%H%M%S")}.csv'
            filepath = os.path.join('exports', filename)
            os.makedirs('exports', exist_ok=True)
            df.to_csv(filepath, index=False)
            return send_file(filepath, as_attachment=True)

        elif format == 'json':
            logs = ThreatLog.query.all()
            data = [log.to_dict() for log in logs]
            filename = f'logs_export_{datetime.now().strftime("%Y%m%d_%H%M%S")}.json'
            filepath = os.path.join('exports', filename)
            os.makedirs('exports', exist_ok=True)
            with open(filepath, 'w') as f:
                json.dump(data, f, indent=2, default=str)
            return send_file(filepath, as_attachment=True)

        else:
            return jsonify({'error': 'Unsupported format'}), 400

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.now().isoformat(),
        'version': '1.0.0'
    })

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        logger.info("Database initialized")

    logger.info("Starting NeuroShield Backend Server...")
    app.run(debug=True, host='0.0.0.0', port=5000)
