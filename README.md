# 🛡️ NeuroShield: AI-Powered Threat Detection System

**Complete Full-Stack Cybersecurity Platform with Real-time Monitoring & Business Intelligence**

![NeuroShield](https://img.shields.io/badge/NeuroShield-v1.0-blue?style=for-the-badge) ![Python](https://img.shields.io/badge/Python-3.8+-green?style=for-the-badge) ![React](https://img.shields.io/badge/React-18+-blue?style=for-the-badge) ![License](https://img.shields.io/badge/License-Educational-orange?style=for-the-badge)

## 🚀 Quick Start (3 Steps)

### Step 1: Backend (Terminal 1)
```bash
cd backend
python -m venv neuroshield_env
neuroshield_env\Scripts\activate    # Windows
# source neuroshield_env/bin/activate  # macOS/Linux
pip install -r requirements.txt
python app.py
```

### Step 2: Frontend (Terminal 2)  
```bash
cd frontend
npm install
npm start
```

### Step 3: Attack Simulators (Terminal 3)
```bash  
cd simulators
pip install -r requirements.txt
python run_all_simulations.py
```

**🎯 Dashboard:** http://localhost:3000  
**🔗 API:** http://localhost:5000

---

## 📊 What You Get

✅ **Real-time Cybersecurity Dashboard** with live threat monitoring  
✅ **AI/ML Threat Detection** using XGBoost and anomaly detection  
✅ **5 Attack Simulators** (SQLi, XSS, Brute Force, Port Scan, Normal Traffic)  
✅ **Auto Defense System** with IP blocking and response logging  
✅ **Power BI Integration** for executive reporting  
✅ **Interactive Charts** showing attack patterns and trends  
✅ **Export Capabilities** (CSV, JSON) for further analysis  
✅ **Professional UI** with cybersecurity-themed design  

---

## 🏗️ Architecture

```
Frontend Dashboard (React) ←→ Flask API ←→ ML Engine
      ↓                          ↓           ↓
  Live Charts              SQLite DB    Attack Sims
      ↓                          ↓           ↓  
   Power BI Export ←→  Defense Actions ←→ Log Analysis
```

---

## 🎯 Perfect For

- **Cybersecurity Learning**: Understand real attack patterns
- **Full-stack Development**: Modern web development practices  
- **Machine Learning**: Practical AI in security applications
- **Portfolio Projects**: Demonstrate technical skills
- **Research & Education**: Security awareness and training

---

## 📁 Project Structure

```
Main Project/
├── 🐍 backend/          # Python Flask API + ML models
├── ⚛️  frontend/         # React.js dashboard + charts  
├── 🎯 simulators/       # Attack generators (SQLi, XSS, etc.)
├── 📊 powerbi/          # Business intelligence integration
└── 📚 docs/             # Complete documentation
```

---

## 🔧 System Requirements

- **Python 3.8+** (Flask backend & ML models)
- **Node.js 14+** (React frontend) 
- **4GB RAM** minimum, 8GB recommended
- **2GB Storage** for project files and data

---

## 🎓 Learning Outcomes

After setting up NeuroShield, you'll understand:

- ✅ **Full-stack Architecture**: Frontend ↔ API ↔ Database integration
- ✅ **Cybersecurity Fundamentals**: Attack vectors and defense mechanisms  
- ✅ **Machine Learning**: Real-world AI applications in security
- ✅ **Data Visualization**: Interactive dashboards and charts
- ✅ **Business Intelligence**: Executive reporting with Power BI
- ✅ **DevOps Practices**: API development and deployment strategies

---

## 🚨 Security Notice

⚠️ **Educational Use Only**: This system is designed for learning and research purposes. Only run attack simulations on systems you own or have explicit permission to test.

---

## 📖 Documentation

- 📋 **[INSTALLATION.md](docs/INSTALLATION.md)** - Detailed setup guide
- 📚 **[README.md](docs/README.md)** - Complete project documentation  
- 📊 **[Power BI Guide](powerbi/README.txt)** - Business intelligence setup

---

## 🎉 Ready to Start?

1. **Extract** this folder to your preferred location
2. **Follow** the Quick Start guide above
3. **Open** http://localhost:3000 to see the dashboard
4. **Run** attack simulations to see live threat detection
5. **Export** data to Power BI for advanced analytics

---

**🛡️ Welcome to NeuroShield - Your AI-Powered Cyber Defense Laboratory!**

*Built with ❤️ for cybersecurity education and full-stack development learning.*