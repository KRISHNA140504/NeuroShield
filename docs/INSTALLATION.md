# 🚀 NeuroShield Installation Guide

This guide provides step-by-step instructions for setting up and running the NeuroShield cybersecurity platform on your local machine.

## 📋 Prerequisites

Before starting, ensure you have the following installed:

### Required Software
- **Python 3.8 or higher** - [Download Python](https://www.python.org/downloads/)
- **Node.js 14 or higher** - [Download Node.js](https://nodejs.org/)
- **Git** (optional) - [Download Git](https://git-scm.com/)

### System Requirements
- **RAM**: Minimum 4GB, Recommended 8GB
- **Storage**: 2GB free space
- **OS**: Windows 10/11, macOS 10.14+, or Linux Ubuntu 18.04+

## 🔍 Verify Prerequisites

Open your terminal/command prompt and verify installations:

```bash
# Check Python version
python --version
# Should show Python 3.8.x or higher

# Check Node.js version  
node --version
# Should show v14.x.x or higher

# Check npm version
npm --version
# Should show 6.x.x or higher
```

## 📁 Extract Project Files

1. Extract the "Main Project" folder to your desired location
2. Open terminal/command prompt
3. Navigate to the project directory:

```bash
cd "path/to/Main Project"
# Replace "path/to/" with your actual path
```

## 🐍 Backend Setup (Python Flask)

### Step 1: Navigate to Backend Directory

```bash
cd backend
```

### Step 2: Create Virtual Environment

**Windows:**
```bash
python -m venv neuroshield_env
neuroshield_env\Scripts\activate
```

**macOS/Linux:**
```bash
python3 -m venv neuroshield_env
source neuroshield_env/bin/activate
```

You should see `(neuroshield_env)` in your terminal prompt.

### Step 3: Install Python Dependencies

```bash
pip install -r requirements.txt
```

This will install:
- Flask (web framework)
- Flask-CORS (cross-origin requests)
- Flask-SQLAlchemy (database)
- pandas (data manipulation)
- numpy (numerical computing)
- scikit-learn (machine learning)
- requests (HTTP requests)

### Step 4: Start Backend Server

```bash
python app.py
```

You should see output like:
```
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:5000
 * Running on http://[::1]:5000
```

**✅ Backend is now running!** Leave this terminal open.

### Test Backend (Optional)

Open browser and visit: http://localhost:5000/api/health

You should see: `{"status":"healthy","timestamp":"...","version":"1.0.0"}`

## ⚛️ Frontend Setup (React.js)

### Step 1: Open New Terminal

Keep the backend terminal running and open a **new terminal window**.

### Step 2: Navigate to Frontend Directory

```bash
cd "path/to/Main Project/frontend"
```

### Step 3: Install Node.js Dependencies

```bash
npm install
```

This will install:
- React (frontend framework)
- Chart.js (data visualization)
- Axios (HTTP client)
- React Chart.js 2 (React Chart.js wrapper)

### Step 4: Start Frontend Server

```bash
npm start
```

You should see:
```
Compiled successfully!

You can now view neuroshield-frontend in the browser.

  Local:            http://localhost:3000
  On Your Network:  http://192.168.x.x:3000
```

Your browser should automatically open to http://localhost:3000

**✅ Frontend is now running!** You should see the NeuroShield dashboard.

## 🎯 Attack Simulators Setup

### Step 1: Open Third Terminal

Keep both backend and frontend running, open a **new terminal window**.

### Step 2: Navigate to Simulators Directory

```bash
cd "path/to/Main Project/simulators"
```

### Step 3: Install Simulator Dependencies

**If using same Python as backend:**
```bash
# Activate the same virtual environment
# Windows:
..\backend\neuroshield_env\Scripts\activate
# macOS/Linux:  
source ../backend/neuroshield_env/bin/activate

pip install -r requirements.txt
```

**Or create separate environment:**
```bash
python -m venv sim_env
# Windows:
sim_env\Scripts\activate
# macOS/Linux:
source sim_env/bin/activate

pip install -r requirements.txt
```

### Step 4: Run Attack Simulations

**Run all simulations:**
```bash
python run_all_simulations.py
```

**Or run individual simulators:**
```bash
python sql_injection.py
python xss_simulator.py  
python brute_force.py
python port_scanner.py
python normal_traffic.py
```

**✅ Simulators are now running!** You should see attack data appearing on the dashboard.

## 🎉 Verification Steps

### 1. Check Backend Health
Visit: http://localhost:5000/api/health
Should return: `{"status": "healthy", ...}`

### 2. Check Dashboard
Visit: http://localhost:3000
Should show NeuroShield dashboard with:
- System Online status
- Threat monitoring panels  
- Real-time metrics
- Export buttons

### 3. Check Database
Visit: http://localhost:5000/api/stats
Should return JSON with threat statistics

### 4. Test Attack Simulation
Run: `python simulators/sql_injection.py`
Check dashboard for new threats appearing

## 🛠 Troubleshooting

### Backend Issues

**Error: "Python not found"**
- Install Python from python.org
- Add Python to system PATH
- Use `python3` instead of `python`

**Error: "Port 5000 already in use"**
- Stop other services using port 5000
- Change port in `backend/app.py`: `app.run(port=5001)`
- Update frontend API URL accordingly

**Error: "Module not found"**  
- Ensure virtual environment is activated
- Reinstall dependencies: `pip install -r requirements.txt`
- Check Python version compatibility

### Frontend Issues

**Error: "npm not found"**
- Install Node.js from nodejs.org
- Restart terminal after installation
- Add npm to system PATH

**Error: "Port 3000 already in use"**
- Choose different port when prompted
- Or stop other services on port 3000

**Error: "Failed to compile"**
- Delete `node_modules` folder
- Delete `package-lock.json`
- Run `npm install` again

### Simulator Issues

**Error: "Connection refused"**
- Ensure backend is running on localhost:5000
- Check firewall settings
- Verify virtual environment activation

**Error: "Import error"**
- Install missing dependencies: `pip install requests pandas`
- Ensure proper Python environment

### Dashboard Not Updating

**No data showing:**
- Run attack simulators to generate data
- Check browser developer console for errors
- Verify backend API endpoints responding

**Charts not displaying:**
- Check browser console for Chart.js errors
- Ensure all npm dependencies installed
- Try refreshing the page

## 💡 Usage Tips

### Daily Workflow
1. **Start Backend**: `cd backend && python app.py`
2. **Start Frontend**: `cd frontend && npm start` (new terminal)
3. **Run Simulators**: `cd simulators && python run_all_simulations.py` (new terminal)
4. **Monitor Dashboard**: Visit http://localhost:3000

### Stopping Services
- **Backend**: Press `Ctrl+C` in backend terminal
- **Frontend**: Press `Ctrl+C` in frontend terminal
- **Simulators**: Press `Ctrl+C` in simulator terminal

### Data Export
- Use dashboard "Export CSV" or "Export JSON" buttons
- Files saved in `backend/exports/` directory
- Import into Excel, Power BI, or other tools

## 📊 Power BI Setup (Optional)

### 1. Export Data
Click "Export CSV" button in dashboard to generate data files.

### 2. Import to Power BI
1. Open Power BI Desktop
2. Get Data → Text/CSV  
3. Select exported CSV file
4. Create visualizations using the data

### 3. Refresh Data
- Re-export CSV from dashboard for updated data
- Refresh data source in Power BI

## 🔄 Updates and Maintenance

### Update Dependencies
```bash
# Backend
cd backend
pip install -r requirements.txt --upgrade

# Frontend  
cd frontend
npm update
```

### Reset Database
Stop backend and delete `backend/neuroshield.db`, then restart backend.

### Clear Browser Cache
If dashboard not updating, clear browser cache or use incognito mode.

## 🎯 Next Steps

1. **Explore Dashboard**: Navigate through all panels and features
2. **Run More Simulations**: Try different attack types
3. **Customize System**: Modify code for your specific needs  
4. **Export Reports**: Generate Power BI dashboards
5. **Learn and Experiment**: Use as educational platform

## 📞 Getting Help

If you encounter issues:
1. **Check Error Messages**: Read terminal output carefully
2. **Verify Prerequisites**: Ensure correct Python/Node.js versions
3. **Check Documentation**: Review this guide and README.md
4. **Test Components**: Verify each part works individually
5. **Start Fresh**: Try clean installation if needed

---

**🎉 Congratulations!** You now have a fully functional AI-powered cybersecurity monitoring system running locally. Enjoy exploring NeuroShield!