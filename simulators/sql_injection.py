import requests
import random
import time
from datetime import datetime
from base_simulator import BaseSimulator

class SQLInjectionSimulator(BaseSimulator):
    def __init__(self, target_url="http://localhost:5000"):
        super().__init__(target_url)
        self.attack_type = "SQLi"

        self.payloads = [
            "' OR '1'='1",
            "' OR '1'='1' --",
            "admin'--",
            "' OR 1=1--",
            "' OR 1=1#",
            "') OR '1'='1--",
            "1' OR '1'='1",
            "' UNION SELECT NULL--",
            "' UNION SELECT username,password FROM users--",
            "'; DROP TABLE users; --",
            "'; INSERT INTO users VALUES('hacker','password'); --",
            "' AND (SELECT COUNT(*) FROM users) > 0 --"
        ]

        self.target_endpoints = [
            "/login",
            "/search", 
            "/user",
            "/admin",
            "/api/login",
            "/dashboard"
        ]

    def generate_attack_log(self):
        """Generate a single SQL injection attack log"""
        payload = random.choice(self.payloads)
        endpoint = random.choice(self.target_endpoints)
        method = random.choice(["GET", "POST"])

        response_time = random.randint(200, 2000)
        status_code = random.choices([200, 500, 401, 403, 404], weights=[10, 40, 20, 15, 15])[0]

        attack_log = {
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "ip": self.generate_random_ip(),
            "method": method,
            "endpoint": endpoint,
            "payload": payload,
            "response_time_ms": response_time,
            "status_code": status_code,
            "type": self.attack_type,
            "user_agent": self.generate_user_agent()
        }

        return attack_log

    def run_simulation(self, num_attacks=30):
        """Run SQL injection simulation"""
        print(f"🔍 Starting SQL Injection simulation - {num_attacks} attacks")

        attack_logs = []
        successful_attacks = 0

        for i in range(num_attacks):
            try:
                attack_log = self.generate_attack_log()

                if self.send_to_backend:
                    response = self.send_log_to_backend(attack_log)
                    if response and response.get('threat_detected'):
                        successful_attacks += 1

                attack_logs.append(attack_log)

                if (i + 1) % 5 == 0:
                    print(f"   Completed {i + 1}/{num_attacks} attacks")

                time.sleep(random.uniform(1, 3))

            except Exception as e:
                print(f"   Error in attack {i + 1}: {e}")

        print(f"✅ SQL Injection simulation completed!")
        print(f"   Total attacks: {num_attacks}")
        print(f"   Detected by system: {successful_attacks}")

        return attack_logs

if __name__ == "__main__":
    simulator = SQLInjectionSimulator()
    logs = simulator.run_simulation(num_attacks=20)
