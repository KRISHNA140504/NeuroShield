import requests
import random
import time
from datetime import datetime
from base_simulator import BaseSimulator

class BruteForceSimulator(BaseSimulator):
    def __init__(self, target_url="http://localhost:5000"):
        super().__init__(target_url)
        self.attack_type = "Brute Force"

        self.common_usernames = [
            "admin", "administrator", "root", "user", "guest", "test",
            "demo", "manager", "support", "oracle", "postgres"
        ]

        self.common_passwords = [
            "password", "123456", "password123", "admin", "12345678",
            "qwerty", "abc123", "Password1", "welcome", "login"
        ]

        self.target_endpoints = ["/login", "/admin", "/auth", "/signin"]

    def generate_attack_log(self):
        """Generate brute force attack"""
        username = random.choice(self.common_usernames)
        password = random.choice(self.common_passwords)
        endpoint = random.choice(self.target_endpoints)

        # Simulate login attempt
        success = username == "admin" and password == "password" and random.random() < 0.05

        attack_log = {
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "ip": self.generate_random_ip(),
            "method": "POST",
            "endpoint": endpoint,
            "payload": f"username={username}&password={password}",
            "response_time_ms": random.randint(300, 1200),
            "status_code": 200 if success else random.choice([401, 403, 422]),
            "type": self.attack_type,
            "user_agent": self.generate_user_agent()
        }

        return attack_log

    def run_simulation(self, num_attacks=20):
        """Run brute force simulation"""
        print(f"🔨 Starting Brute Force simulation - {num_attacks} attacks")

        attack_logs = []

        for i in range(num_attacks):
            try:
                attack_log = self.generate_attack_log()

                if self.send_to_backend:
                    self.send_log_to_backend(attack_log)

                attack_logs.append(attack_log)

                if (i + 1) % 5 == 0:
                    print(f"   Completed {i + 1}/{num_attacks} attacks")

                time.sleep(random.uniform(0.5, 2))

            except Exception as e:
                print(f"   Error in attack {i + 1}: {e}")

        print(f"✅ Brute Force simulation completed!")
        return attack_logs

if __name__ == "__main__":
    simulator = BruteForceSimulator()
    logs = simulator.run_simulation(num_attacks=15)
