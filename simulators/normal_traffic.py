import requests
import random
import time
from datetime import datetime
from base_simulator import BaseSimulator

class NormalTrafficSimulator(BaseSimulator):
    def __init__(self, target_url="http://localhost:5000"):
        super().__init__(target_url)
        self.attack_type = "Normal"

        self.normal_endpoints = [
            "/", "/home", "/about", "/contact", "/products",
            "/services", "/blog", "/news", "/help", "/profile"
        ]

        self.normal_payloads = [
            "search term", "user query", "contact form", 
            "product review", "normal comment", "feedback"
        ]

    def generate_normal_log(self):
        """Generate normal traffic log"""
        endpoint = random.choice(self.normal_endpoints)
        method = random.choice(["GET", "POST"])
        payload = random.choice(self.normal_payloads) if method == "POST" else ""

        attack_log = {
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "ip": self.generate_random_ip(),
            "method": method,
            "endpoint": endpoint,
            "payload": payload,
            "response_time_ms": random.randint(50, 300),
            "status_code": random.choices([200, 404, 302], weights=[80, 15, 5])[0],
            "type": self.attack_type,
            "user_agent": self.generate_user_agent()
        }

        return attack_log

    def run_simulation(self, num_requests=30):
        """Run normal traffic simulation"""
        print(f"✅ Starting Normal Traffic simulation - {num_requests} requests")

        traffic_logs = []

        for i in range(num_requests):
            try:
                log = self.generate_normal_log()

                if self.send_to_backend:
                    self.send_log_to_backend(log)

                traffic_logs.append(log)

                if (i + 1) % 10 == 0:
                    print(f"   Completed {i + 1}/{num_requests} requests")

                time.sleep(random.uniform(0.5, 2))

            except Exception as e:
                print(f"   Error in request {i + 1}: {e}")

        print(f"✅ Normal Traffic simulation completed!")
        return traffic_logs

if __name__ == "__main__":
    simulator = NormalTrafficSimulator()
    logs = simulator.run_simulation(num_requests=20)
