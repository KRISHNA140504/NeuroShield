# NeuroShield
<h3>AI-powered real-time cyber threat detection &amp; defense system with ML, automated IP blocking, and interactive dashboard.<h3/>
<br/>
🛡️ NeuroShield — AI-Powered Cyber Threat Detection & Response
NeuroShield is a real-time cyber threat detection dashboard that uses Machine Learning + Flask + React to monitor system activities, detect malicious traffic, and take automated defense actions.
It simulates and detects attacks like SQL Injection, XSS, Brute Force, and Port Scanning — all in a visual, interactive dashboard.

🚀 Features
Real-Time Monitoring — Track incoming requests, system metrics, and threats live.

ML-Based Threat Detection — Detects threats with probability scoring.

Automated Defense Actions — Auto-blocks high-confidence malicious IPs.

Attack Simulation Suite — Simulate SQLi, XSS, Brute Force, Port Scans, and Normal Traffic.

Data Export — Export logs in CSV/JSON for offline analysis.

Interactive Dashboard — Built with React + Chart.js for live visualization.

🛠️ Tech Stack
Frontend: React.js, TailwindCSS, Chart.js
Backend: Python, Flask, Flask-SQLAlchemy, Flask-CORS
Database: SQLite
Machine Learning: scikit-learn, NumPy, Pandas
Visualization: Power BI (for analytics), Chart.js (for frontend graphs)
Attack Simulations: Custom Python scripts for various threat types

📂 Project Structure
bash
Copy code
NeuroShield/
│
├── backend/           # Flask backend (API + ML logic + database)
├── frontend/          # React dashboard
├── simulators/        # Attack simulation scripts
├── powerbi/           # Power BI dashboards
├── run_backend.bat    # Quick start for backend
├── run_frontend.bat   # Quick start for frontend
├── run_simulators.bat # Quick start for simulators
└── README.md
⚡ Quick Start
1️⃣ Clone the Repository
bash
Copy code
git clone https://github.com/KRISHNA140504/NeuroShield.git
cd NeuroShield
2️⃣ Start Backend
bash
Copy code
cd backend
python -m venv neuroshield_env
neuroshield_env\Scripts\activate
pip install -r requirements.txt
python app.py
3️⃣ Start Frontend
bash
Copy code
cd frontend
npm install
npm start
4️⃣ Run Simulators
bash
Copy code
cd simulators
python run_all_simulations.py
📊 Dashboard Preview
Before: No threats detected, normal traffic only.
After: Multiple threats detected with blocked IPs, visualized in real-time.

(Insert before/after screenshots here)

📜 License
MIT License — Feel free to use and modify with credit.

✨ Author
Krishna Mahajan
🔗 LinkedIn | 🌐 GitHub
