import React, { useState, useEffect } from 'react';
import { Chart as ChartJS, CategoryScale, LinearScale, BarElement, ArcElement, Title, Tooltip, Legend, PointElement, LineElement } from 'chart.js';
import { Bar, Pie, Line } from 'react-chartjs-2';
import axios from 'axios';

ChartJS.register(CategoryScale, LinearScale, BarElement, ArcElement, PointElement, LineElement, Title, Tooltip, Legend);

const API_BASE_URL = 'http://localhost:5000/api';

const Dashboard = () => {
    const [dashboardData, setDashboardData] = useState({
        logs: [],
        stats: {},
        blockedIPs: [],
        loading: true
    });
    const [currentTime, setCurrentTime] = useState(new Date());

    useEffect(() => {
        fetchData();
        const interval = setInterval(() => {
            fetchData();
            setCurrentTime(new Date());
        }, 5000);

        return () => clearInterval(interval);
    }, []);

    const fetchData = async () => {
        try {
            const [logsRes, statsRes, blockedRes] = await Promise.all([
                axios.get(`${API_BASE_URL}/logs?per_page=10`),
                axios.get(`${API_BASE_URL}/stats`),
                axios.get(`${API_BASE_URL}/blocked-ips`)
            ]);

            setDashboardData({
                logs: logsRes.data.logs || [],
                stats: statsRes.data || {},
                blockedIPs: blockedRes.data || [],
                loading: false
            });
        } catch (error) {
            console.error('Error fetching data:', error);
            setDashboardData(prev => ({ ...prev, loading: false }));
        }
    };

    const exportData = async (format) => {
        try {
            const response = await axios.get(`${API_BASE_URL}/export/${format}`, {
                responseType: 'blob'
            });

            const url = window.URL.createObjectURL(new Blob([response.data]));
            const link = document.createElement('a');
            link.href = url;
            link.setAttribute('download', `neuroshield_export_${new Date().toISOString().split('T')[0]}.${format}`);
            document.body.appendChild(link);
            link.click();
            link.remove();
        } catch (error) {
            console.error('Export error:', error);
            alert('Export failed. Please try again.');
        }
    };

    // Chart configurations
    const threatDistributionData = {
        labels: Object.keys(dashboardData.stats.threat_distribution || {}),
        datasets: [{
            label: 'Threats Detected',
            data: Object.values(dashboardData.stats.threat_distribution || {}),
            backgroundColor: [
                'rgba(255, 99, 132, 0.8)',
                'rgba(255, 159, 64, 0.8)',
                'rgba(255, 205, 86, 0.8)',
                'rgba(75, 192, 192, 0.8)',
                'rgba(54, 162, 235, 0.8)'
            ],
            borderColor: [
                'rgba(255, 99, 132, 1)',
                'rgba(255, 159, 64, 1)',
                'rgba(255, 205, 86, 1)',
                'rgba(75, 192, 192, 1)',
                'rgba(54, 162, 235, 1)'
            ],
            borderWidth: 2
        }]
    };

    const chartOptions = {
        responsive: true,
        plugins: {
            legend: { 
                position: 'top',
                labels: { color: '#fff' }
            },
            title: { 
                display: true, 
                text: 'Threat Distribution',
                color: '#fff'
            }
        },
        scales: {
            y: { 
                beginAtZero: true,
                ticks: { color: '#fff' },
                grid: { color: '#444' }
            },
            x: {
                ticks: { color: '#fff' },
                grid: { color: '#444' }
            }
        }
    };

    if (dashboardData.loading) {
        return (
            <div className="loading-container">
                <div className="loading-spinner"></div>
                <p>Loading NeuroShield Dashboard...</p>
            </div>
        );
    }

    return (
        <div className="dashboard">
            {/* Header */}
            <header className="dashboard-header">
                <div className="header-content">
                    <h1 className="main-title">
                        <i className="fas fa-shield-alt"></i>
                        NeuroShield: AI-Powered Cyber Defense System
                    </h1>
                    <div className="status-indicators">
                        <div className="status-item online">
                            <i className="fas fa-circle"></i>
                            <span>System Online</span>
                        </div>
                        <div className="status-item threats">
                            <i className="fas fa-exclamation-triangle"></i>
                            <span>{dashboardData.stats.total_threats || 0} Threats Detected</span>
                        </div>
                        <div className="status-item defense">
                            <i className="fas fa-ban"></i>
                            <span>{dashboardData.stats.blocked_ips || 0} IPs Blocked</span>
                        </div>
                        <div className="timestamp">
                            <i className="fas fa-clock"></i>
                            <span>{currentTime.toLocaleTimeString()}</span>
                        </div>
                    </div>
                </div>
            </header>

            {/* Main Dashboard Grid */}
            <main className="dashboard-main">
                {/* Live Threat Monitor */}
                <section className="panel threat-monitor">
                    <div className="panel-header">
                        <h3><i className="fas fa-eye"></i> Live Threat Monitor</h3>
                        <div className="live-indicator">
                            <span className="pulse"></span>
                            LIVE
                        </div>
                    </div>
                    <div className="threat-list">
                        {dashboardData.logs.filter(log => log.threat_type).slice(0, 8).map(threat => (
                            <div key={threat.id} className="threat-item">
                                <div className="threat-icon">
                                    {threat.threat_type === 'SQLi' && <i className="fas fa-database"></i>}
                                    {threat.threat_type === 'XSS' && <i className="fas fa-code"></i>}
                                    {threat.threat_type === 'Brute Force' && <i className="fas fa-key"></i>}
                                    {threat.threat_type === 'Port Scan' && <i className="fas fa-search"></i>}
                                </div>
                                <div className="threat-info">
                                    <div className="threat-type">{threat.threat_type || 'Unknown'}</div>
                                    <div className="threat-details">
                                        <span className="threat-ip">IP: {threat.ip}</span>
                                        <span className="threat-endpoint">→ {threat.endpoint}</span>
                                    </div>
                                    <div className="threat-time">
                                        {new Date(threat.timestamp).toLocaleTimeString()}
                                    </div>
                                </div>
                                <div className="threat-confidence">
                                    {((threat.confidence_score || 0) * 100).toFixed(0)}%
                                </div>
                            </div>
                        ))}
                    </div>
                </section>

                {/* Metrics Cards */}
                <section className="panel metrics-grid">
                    <h3><i className="fas fa-chart-bar"></i> System Metrics</h3>
                    <div className="metrics-cards">
                        <div className="metric-card">
                            <div className="metric-icon">
                                <i className="fas fa-file-alt"></i>
                            </div>
                            <div className="metric-content">
                                <div className="metric-value">{dashboardData.stats.total_logs || 0}</div>
                                <div className="metric-label">Total Logs</div>
                            </div>
                        </div>
                        <div className="metric-card threat">
                            <div className="metric-icon">
                                <i className="fas fa-exclamation-triangle"></i>
                            </div>
                            <div className="metric-content">
                                <div className="metric-value">{dashboardData.stats.total_threats || 0}</div>
                                <div className="metric-label">Threats</div>
                            </div>
                        </div>
                        <div className="metric-card blocked">
                            <div className="metric-icon">
                                <i className="fas fa-ban"></i>
                            </div>
                            <div className="metric-content">
                                <div className="metric-value">{dashboardData.stats.blocked_ips || 0}</div>
                                <div className="metric-label">Blocked IPs</div>
                            </div>
                        </div>
                        <div className="metric-card accuracy">
                            <div className="metric-icon">
                                <i className="fas fa-bullseye"></i>
                            </div>
                            <div className="metric-content">
                                <div className="metric-value">98.3%</div>
                                <div className="metric-label">Accuracy</div>
                            </div>
                        </div>
                    </div>
                </section>

                {/* Threat Analytics */}
                <section className="panel threat-analytics">
                    <h3><i className="fas fa-chart-pie"></i> Threat Analytics</h3>
                    <div className="chart-container">
                        {Object.keys(dashboardData.stats.threat_distribution || {}).length > 0 ? (
                            <Pie data={threatDistributionData} options={chartOptions} />
                        ) : (
                            <div className="no-data">
                                <i className="fas fa-chart-pie"></i>
                                <p>No threat data available</p>
                                <small>Run attack simulations to see analytics</small>
                            </div>
                        )}
                    </div>
                </section>

                {/* Defense Actions */}
                <section className="panel defense-actions">
                    <h3><i className="fas fa-shield-alt"></i> Defense Actions</h3>
                    <div className="actions-list">
                        {dashboardData.blockedIPs.slice(0, 6).map((ip, index) => (
                            <div key={index} className="action-item">
                                <div className="action-icon">
                                    <i className="fas fa-ban"></i>
                                </div>
                                <div className="action-details">
                                    <div className="action-primary">Blocked: {ip.ip}</div>
                                    <div className="action-secondary">{ip.reason}</div>
                                    <div className="action-time">
                                        {new Date(ip.blocked_at).toLocaleString()}
                                    </div>
                                </div>
                                <div className="action-status active">ACTIVE</div>
                            </div>
                        ))}
                        {dashboardData.blockedIPs.length === 0 && (
                            <div className="no-data">
                                <i className="fas fa-shield-alt"></i>
                                <p>No blocked IPs</p>
                                <small>System is monitoring for threats</small>
                            </div>
                        )}
                    </div>
                </section>

                {/* Recent Logs */}
                <section className="panel recent-logs">
                    <h3><i className="fas fa-list"></i> Recent Activity</h3>
                    <div className="logs-table">
                        <table>
                            <thead>
                                <tr>
                                    <th>Time</th>
                                    <th>IP</th>
                                    <th>Method</th>
                                    <th>Endpoint</th>
                                    <th>Status</th>
                                    <th>Type</th>
                                </tr>
                            </thead>
                            <tbody>
                                {dashboardData.logs.slice(0, 10).map(log => (
                                    <tr key={log.id} className={log.threat_type ? 'threat-row' : 'normal-row'}>
                                        <td>{new Date(log.timestamp).toLocaleTimeString()}</td>
                                        <td>{log.ip}</td>
                                        <td>
                                            <span className={`method ${log.method?.toLowerCase()}`}>
                                                {log.method}
                                            </span>
                                        </td>
                                        <td title={log.endpoint}>{log.endpoint}</td>
                                        <td>
                                            <span className={`status status-${Math.floor(log.status_code / 100)}`}>
                                                {log.status_code}
                                            </span>
                                        </td>
                                        <td>
                                            {log.threat_type ? (
                                                <span className="threat-badge">{log.threat_type}</span>
                                            ) : (
                                                <span className="normal-badge">Normal</span>
                                            )}
                                        </td>
                                    </tr>
                                ))}
                            </tbody>
                        </table>
                    </div>
                </section>
            </main>

            {/* Export Controls */}
            <footer className="dashboard-footer">
                <div className="export-controls">
                    <button onClick={() => exportData('csv')} className="export-btn">
                        <i className="fas fa-download"></i> Export CSV
                    </button>
                    <button onClick={() => exportData('json')} className="export-btn">
                        <i className="fas fa-download"></i> Export JSON
                    </button>
                    <button onClick={() => window.print()} className="export-btn">
                        <i className="fas fa-print"></i> Print Report
                    </button>
                    <button onClick={fetchData} className="refresh-btn">
                        <i className="fas fa-sync-alt"></i> Refresh
                    </button>
                </div>
            </footer>
        </div>
    );
};

export default Dashboard;