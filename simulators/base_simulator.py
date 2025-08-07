import requests
import random
import json
import csv
from datetime import datetime
import time

class BaseSimulator:
    def __init__(self, target_url="http://localhost:5000"):
        self.target_url = target_url
        self.send_to_backend = True
        self.attack_type = "Generic"

    def generate_random_ip(self):
        """Generate random IP address"""
        return f"{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}"

    def generate_user_agent(self):
        """Generate random user agent"""
        user_agents = [
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:91.0) Gecko/20100101",
            "curl/7.68.0",
            "python-requests/2.25.1"
        ]
        return random.choice(user_agents)

    def send_log_to_backend(self, log_data):
        """Send log data to backend API"""
        try:
            if self.send_to_backend:
                response = requests.post(
                    f"{self.target_url}/api/logs",
                    json=log_data,
                    timeout=5
                )
                return response.json() if response.status_code == 200 else None
        except Exception as e:
            print(f"Error sending to backend: {e}")
            return None

    def save_logs(self, logs, filename_prefix):
        """Save logs to JSON and CSV files"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

        # Save as JSON
        json_filename = f"logs/{filename_prefix}_{timestamp}.json"
        with open(json_filename, 'w') as f:
            json.dump(logs, f, indent=2, default=str)

        # Save as CSV
        csv_filename = f"logs/{filename_prefix}_{timestamp}.csv"
        if logs:
            df_logs = pd.DataFrame(logs)
            df_logs.to_csv(csv_filename, index=False)

        print(f"   Saved logs: {json_filename}, {csv_filename}")

    def url_encode(self, payload):
        """URL encode payload"""
        import urllib.parse
        return urllib.parse.quote(payload)

    def hex_encode(self, payload):
        """Hex encode payload"""
        return ''.join([hex(ord(c))[2:] for c in payload])

    def unicode_encode(self, payload):
        """Unicode encode payload"""
        return ''.join([f"\\u{ord(c):04x}" for c in payload])

