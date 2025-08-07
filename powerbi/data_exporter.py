#!/usr/bin/env python3
"""
NeuroShield Power BI Data Exporter
Exports threat detection data for Power BI visualization
"""

import pandas as pd
import json
import sqlite3
from datetime import datetime, timedelta
import os

class PowerBIExporter:
    def __init__(self, db_path="../backend/neuroshield.db"):
        self.db_path = db_path

    def export_all_data(self):
        """Export all data for Power BI analysis"""
        print("🔄 Exporting NeuroShield data for Power BI...")

        if not os.path.exists(self.db_path):
            print(f"❌ Database not found: {self.db_path}")
            print("   Make sure the backend has been started at least once.")
            return

        try:
            conn = sqlite3.connect(self.db_path)

            # Export threat logs
            logs_query = """
            SELECT 
                id,
                datetime(timestamp) as timestamp,
                ip,
                method,
                endpoint,
                SUBSTR(payload, 1, 100) as payload_preview,
                response_time,
                status_code,
                threat_type,
                ROUND(confidence_score * 100, 2) as confidence_percentage
            FROM threat_logs
            ORDER BY timestamp DESC
            """

            df_logs = pd.read_sql_query(logs_query, conn)
            df_logs.to_csv('threat_logs_powerbi.csv', index=False)
            print(f"✅ Exported {len(df_logs)} log records to threat_logs_powerbi.csv")

            # Export detections
            detections_query = """
            SELECT 
                d.id,
                datetime(d.timestamp) as detection_time,
                d.threat_type,
                ROUND(d.confidence_score * 100, 2) as confidence_percentage,
                l.ip,
                l.endpoint,
                l.method
            FROM detections d
            JOIN threat_logs l ON d.log_id = l.id
            ORDER BY d.timestamp DESC
            """

            df_detections = pd.read_sql_query(detections_query, conn)
            df_detections.to_csv('threat_detections_powerbi.csv', index=False)
            print(f"✅ Exported {len(df_detections)} detection records to threat_detections_powerbi.csv")

            # Export blocked IPs
            blocked_query = """
            SELECT 
                ip,
                reason,
                datetime(blocked_at) as blocked_time,
                status
            FROM blocked_ips
            ORDER BY blocked_at DESC
            """

            df_blocked = pd.read_sql_query(blocked_query, conn)
            df_blocked.to_csv('blocked_ips_powerbi.csv', index=False)
            print(f"✅ Exported {len(df_blocked)} blocked IP records to blocked_ips_powerbi.csv")

            # Create summary statistics
            summary_stats = {
                "export_date": datetime.now().isoformat(),
                "total_logs": len(df_logs),
                "total_detections": len(df_detections),
                "total_blocked_ips": len(df_blocked),
                "threat_types": df_detections['threat_type'].value_counts().to_dict(),
                "top_attacking_ips": df_detections['ip'].value_counts().head(10).to_dict()
            }

            with open('neuroshield_summary.json', 'w') as f:
                json.dump(summary_stats, f, indent=2)

            conn.close()

            print("\n📊 Power BI Export Summary:")
            print("="*40)
            print(f"Total Logs: {summary_stats['total_logs']}")
            print(f"Total Detections: {summary_stats['total_detections']}")
            print(f"Blocked IPs: {summary_stats['total_blocked_ips']}")
            print("\nFiles created:")
            print("- threat_logs_powerbi.csv")
            print("- threat_detections_powerbi.csv") 
            print("- blocked_ips_powerbi.csv")
            print("- neuroshield_summary.json")
            print("\n🎯 Import these CSV files into Power BI Desktop to create dashboards!")

        except Exception as e:
            print(f"❌ Error exporting data: {e}")

if __name__ == "__main__":
    exporter = PowerBIExporter()
    exporter.export_all_data()