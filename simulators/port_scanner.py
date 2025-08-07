import requests
import random
import time
from datetime import datetime
from base_simulator import BaseSimulator

class PortScannerSimulator(BaseSimulator):
    def __init__(self, target_url="http://localhost:5000"):
        super().__init__(target_url)
        self.attack_type = "Port Scan"

        self.scan_endpoints = [
            "/.env", "/admin.php", "/config.php", "/backup.zip",
            "/robots.txt", "/.htaccess", "/wp-admin", "/phpmyadmin",
            "/api", "/admin", "/test", "/dev"
        ]

    def generate_attack_log(self):
        """Generate port scan attack"""
        endpoint = random.choice(self.scan_endpoints)

        attack_log = {
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "ip": self.generate_random_ip(),
            "method": "GET",
            "endpoint": endpoint,
            "payload": "",
            "response_time_ms": random.randint(10, 200),
            "status_code": random.choices([404, 403, 200], weights=[70, 20, 10])[0],
            "type": self.attack_type,
            "user_agent": self.generate_user_agent()
        }

        return attack_log

    def run_simulation(self, num_attacks=15):
        """Run port scan simulation"""
        print(f"🔍 Starting Port Scan simulation - {num_attacks} attacks")

        attack_logs = []

        for i in range(num_attacks):
            try:
                attack_log = self.generate_attack_log()

                if self.send_to_backend:
                    self.send_log_to_backend(attack_log)

                attack_logs.append(attack_log)

                if (i + 1) % 5 == 0:
                    print(f"   Completed {i + 1}/{num_attacks} attacks")

                time.sleep(random.uniform(0.2, 1))

            except Exception as e:
                print(f"   Error in attack {i + 1}: {e}")

        print(f"✅ Port Scan simulation completed!")
        return attack_logs

if __name__ == "__main__":
    simulator = PortScannerSimulator()
    logs = simulator.run_simulation(num_attacks=10)
