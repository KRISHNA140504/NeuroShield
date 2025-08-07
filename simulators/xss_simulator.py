import requests
import random
import time
import urllib.parse
from datetime import datetime
from base_simulator import BaseSimulator

class XSSSimulator(BaseSimulator):
    def __init__(self, target_url="http://localhost:5000"):
        super().__init__(target_url)
        self.attack_type = "XSS"

        self.xss_payloads = [
            "<script>alert('XSS')</script>",
            "<script>alert(document.cookie)</script>",
            "<ScRiPt>alert('XSS')</ScRiPt>",
            "'><script>alert('XSS')</script>",
            '"><script>alert("XSS")</script>',
            "<img src=x onerror=alert('XSS')>",
            "<body onload=alert('XSS')>",
            "<div onmouseover=alert('XSS')>",
            "<svg onload=alert('XSS')>",
            "<input onfocus=alert('XSS') autofocus>",
            "javascript:alert('XSS')"
        ]

        self.target_endpoints = [
            "/search?q=",
            "/user?name=",
            "/comment",
            "/profile",
            "/feedback"
        ]

    def generate_attack_log(self):
        """Generate XSS attack"""
        payload = random.choice(self.xss_payloads)
        endpoint = random.choice(self.target_endpoints)

        if "?" in endpoint:
            full_endpoint = f"{endpoint}{urllib.parse.quote(payload)}"
            method = "GET"
        else:
            full_endpoint = endpoint
            method = "POST"

        attack_log = {
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "ip": self.generate_random_ip(),
            "method": method,
            "endpoint": full_endpoint,
            "payload": payload,
            "response_time_ms": random.randint(100, 800),
            "status_code": random.choices([200, 404, 400], weights=[70, 20, 10])[0],
            "type": self.attack_type,
            "user_agent": self.generate_user_agent()
        }

        return attack_log

    def run_simulation(self, num_attacks=25):
        """Run XSS simulation"""
        print(f"🕷️ Starting XSS simulation - {num_attacks} attacks")

        attack_logs = []

        for i in range(num_attacks):
            try:
                attack_log = self.generate_attack_log()

                if self.send_to_backend:
                    self.send_log_to_backend(attack_log)

                attack_logs.append(attack_log)

                if (i + 1) % 5 == 0:
                    print(f"   Completed {i + 1}/{num_attacks} attacks")

                time.sleep(random.uniform(1, 3))

            except Exception as e:
                print(f"   Error in attack {i + 1}: {e}")

        print(f"✅ XSS simulation completed!")
        return attack_logs

if __name__ == "__main__":
    simulator = XSSSimulator()
    logs = simulator.run_simulation(num_attacks=15)
