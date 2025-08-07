#!/usr/bin/env python3
"""
NeuroShield Attack Storm Mode
Runs endless high-intensity attack simulations to fill the dashboard with threat data.
"""

import os
import sys
import time
import random
from datetime import datetime

# Add current directory to path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from sql_injection import SQLInjectionSimulator
from xss_simulator import XSSSimulator
from brute_force import BruteForceSimulator
from port_scanner import PortScannerSimulator
from normal_traffic import NormalTrafficSimulator

def main():
    print("⚡ NeuroShield Attack Storm Mode ⚡")
    print("=" * 50)
    print(f"Starting high-intensity attack simulation at {datetime.now()}")

    os.makedirs("logs", exist_ok=True)

    # Use aggressive payload counts to ensure detection
    simulators = [
        ("SQL Injection", SQLInjectionSimulator(), 20),
        ("XSS Attacks", XSSSimulator(), 20),
        ("Brute Force", BruteForceSimulator(), 15),
        ("Port Scanning", PortScannerSimulator(), 15),
        ("Normal Traffic", NormalTrafficSimulator(), 5)  # small amount for realism
    ]

    total_attacks = 0
    loop_count = 0

    while True:
        loop_count += 1
        print(f"\n--- Storm cycle #{loop_count} ---")

        for name, simulator, count in simulators:
            print(f"\n🚀 Running {name} simulation...")
            try:
                # Randomize counts slightly so traffic looks natural
                logs = simulator.run_simulation(count + random.randint(0, 5)) if hasattr(simulator, 'run_simulation') else []
                total_attacks += len(logs)
                print(f"✅ {name} completed: {len(logs)} events generated")
            except Exception as e:
                print(f"❌ {name} failed: {e}")

            time.sleep(0.5)  # short pause for realism

        print(f"\n🎯 Storm Summary after {loop_count} cycles")
        print("=" * 50)
        print(f"Total events generated so far: {total_attacks}")
        print(f"Last cycle completed at: {datetime.now()}")
        print(f"Dashboard: http://localhost:3000")
        print(f"Backend API: http://localhost:5000")

        # Short pause before next cycle (storm effect)
        time.sleep(2)

if __name__ == "__main__":
    main()
