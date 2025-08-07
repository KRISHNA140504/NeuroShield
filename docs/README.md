# 🛡️ NeuroShield: AI-Powered Threat Detection and Autonomous Cyber Defense System

![NeuroShield Logo](https://img.shields.io/badge/NeuroShield-AI%20Cyber%20Defense-blue?style=for-the-badge&logo=shield)

## 🎯 Project Overview

NeuroShield is a comprehensive, full-stack cybersecurity platform that combines AI-powered threat detection, real-time monitoring, attack simulation, and business intelligence. The system demonstrates production-ready cybersecurity practices with modern development methodologies.

### ⚡ Key Features

- **🤖 AI-Powered Detection**: Machine learning models for real-time threat identification
- **📊 Interactive Dashboard**: React-based real-time monitoring interface
- **🎯 Attack Simulation**: Comprehensive suite of attack generators (SQLi, XSS, Brute Force, etc.)
- **🚫 Auto Defense**: Automated IP blocking and threat response
- **📈 Business Intelligence**: Power BI integration for executive reporting
- **🔄 Real-time Updates**: Live dashboard with WebSocket connections
- **🐳 Docker Support**: Complete containerization for easy deployment

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                     NeuroShield Architecture                    │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  Frontend (React.js) ↔ Backend API (Flask) ↔ ML Engine         │
│        ↕                    ↕                     ↕             │
│  Dashboard UI        SQLite Database      Attack Simulators    │
│        ↕                    ↕                     ↕             │
│   Power BI  ←→  Auto Defense Module  ←→  Log Analysis Engine   │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

## 🛠 Technology Stack

- **Backend**: Python Flask, SQLAlchemy, SQLite
- **Frontend**: React.js, Chart.js, CSS3, HTML5
- **AI/ML**: Scikit-learn, XGBoost, Pandas, NumPy
- **Visualization**: Chart.js, Power BI integration
- **Security**: Attack simulation, anomaly detection, automated blocking
- **DevOps**: Docker, RESTful APIs, automated testing

## 📂 Project Structure

```
Main Project/
├── backend/                    # Flask API server
│   ├── app.py                 # Main application
│   ├── requirements.txt       # Python dependencies
│   └── exports/               # Data export directory
├── frontend/                   # React dashboard
│   ├── package.json           # Node.js dependencies
│   ├── public/                # Static files
│   └── src/                   # React components
│       ├── components/        # Dashboard components
│       └── styles/            # CSS files
├── simulators/                # Attack generators
│   ├── sql_injection.py       # SQL injection attacks
│   ├── xss_simulator.py       # Cross-site scripting
│   ├── brute_force.py         # Password attacks
│   ├── port_scanner.py        # Port scanning
│   ├── normal_traffic.py      # Legitimate traffic
│   └── run_all_simulations.py # Master controller
├── powerbi/                   # Business intelligence
│   └── data_exporter.py       # Power BI integration
└── docs/                      # Documentation
    ├── README.md              # This file
    └── INSTALLATION.md        # Setup guide
```

## 🚀 Quick Start

### Prerequisites
- Python 3.8+ installed
- Node.js 14+ installed
- Git installed

### 1. Backend Setup
```bash
# Navigate to backend directory
cd "Main Project/backend"

# Create virtual environment
python -m venv neuroshield_env

# Activate virtual environment
# On Windows:
neuroshield_env\Scripts\activate
# On macOS/Linux:
source neuroshield_env/bin/activate

# Install dependencies
pip install -r requirements.txt

# Start backend server
python app.py
```

Backend will run on: http://localhost:5000

### 2. Frontend Setup
```bash
# Navigate to frontend directory (new terminal)
cd "Main Project/frontend"

# Install dependencies
npm install

# Start frontend server
npm start
```

Frontend will run on: http://localhost:3000

### 3. Run Attack Simulations
```bash
# Navigate to simulators directory (new terminal)
cd "Main Project/simulators"

# Install dependencies
pip install -r requirements.txt

# Run all simulations
python run_all_simulations.py
```

## 📊 Dashboard Features

### Real-time Monitoring
- **Live Threat Feed**: Real-time display of detected attacks
- **System Metrics**: Total logs, threats detected, blocked IPs
- **Threat Analytics**: Visual charts showing attack distribution
- **Defense Actions**: List of automated responses and blocked IPs

### Interactive Elements
- **Auto Refresh**: Dashboard updates every 5 seconds
- **Export Functions**: Download data in CSV or JSON format
- **Print Reports**: Generate printable security reports
- **Responsive Design**: Works on desktop, tablet, and mobile

## 🎯 Attack Simulation Suite

The system includes comprehensive attack simulators:

### SQL Injection (`sql_injection.py`)
- Various injection techniques
- Union-based attacks
- Time-based blind injection
- Error-based injection

### Cross-Site Scripting (`xss_simulator.py`)
- Reflected XSS attacks
- Stored XSS payloads
- DOM-based XSS
- Event handler attacks

### Brute Force (`brute_force.py`)
- Password dictionary attacks
- Credential stuffing
- Login form targeting
- Multi-threaded attacks

### Port Scanning (`port_scanner.py`)
- Common file enumeration
- Directory traversal attempts
- Admin panel discovery
- Configuration file access

### Normal Traffic (`normal_traffic.py`)
- Legitimate user behavior
- Normal API requests
- Regular web browsing
- Form submissions

## 🤖 AI/ML Components

### Threat Detection Engine
- **Feature Extraction**: Analyzes request patterns, payload content, response times
- **Classification**: Identifies attack types (SQLi, XSS, Brute Force, etc.)
- **Confidence Scoring**: Provides threat probability scores
- **Anomaly Detection**: Identifies unusual patterns in traffic

### Auto Defense System
- **Real-time Blocking**: Automatically blocks high-confidence threats
- **IP Blacklisting**: Maintains list of malicious IP addresses
- **Response Logging**: Records all defensive actions taken
- **Threshold Management**: Configurable confidence thresholds

## 📈 Power BI Integration

### Data Export
- **CSV Format**: Structured data for easy import
- **JSON Format**: Hierarchical data with full details
- **Real-time Updates**: Automated data refresh capabilities
- **Custom Reports**: Executive dashboards and KPI tracking

### Visualization Templates
- **Threat Timeline**: Time-series analysis of attacks
- **Geographic Distribution**: Attack sources by location
- **Model Performance**: AI accuracy and effectiveness metrics
- **Executive Summary**: High-level security overview

## 🔧 Configuration

### Backend Configuration
Edit `backend/app.py` for:
- Database connection settings
- ML model parameters
- API endpoint configuration
- Logging levels

### Frontend Configuration  
Edit `frontend/src/components/Dashboard.js` for:
- API endpoint URLs
- Refresh intervals
- Chart configurations
- UI customization

### Simulator Configuration
Edit individual simulator files for:
- Attack payload customization
- Target endpoint modification
- Attack frequency settings
- Output format options

## 🐛 Troubleshooting

### Common Issues

**Backend won't start:**
- Check Python version (3.8+ required)
- Verify all dependencies installed: `pip list`
- Check port 5000 availability

**Frontend won't start:**
- Check Node.js version (14+ required)  
- Clear npm cache: `npm cache clean --force`
- Delete node_modules and reinstall: `rm -rf node_modules && npm install`

**Simulators not connecting:**
- Verify backend is running on localhost:5000
- Check firewall settings
- Ensure virtual environment is activated

**Dashboard not updating:**
- Check browser console for errors
- Verify backend API is responding: http://localhost:5000/api/health
- Clear browser cache

### Getting Help
- Check the logs in terminal for error messages
- Verify all dependencies are installed correctly
- Ensure Python virtual environment is activated
- Check that all required ports are available

## 🎓 Educational Use

This project is perfect for:
- **Cybersecurity Education**: Understanding attack vectors and defense mechanisms
- **Full-stack Development**: Learning modern web development practices
- **Machine Learning**: Practical AI applications in security
- **DevOps Practices**: Containerization and deployment strategies

## 📝 License

This project is for educational and research purposes. Please use responsibly and only on systems you own or have explicit permission to test.

## 🚀 Next Steps

1. **Start the system** using the Quick Start guide above
2. **Run attack simulations** to generate sample data
3. **Explore the dashboard** to see real-time threat detection
4. **Export data** for Power BI analysis
5. **Customize and extend** the system for your needs

---

**🛡️ Stay secure with NeuroShield!**