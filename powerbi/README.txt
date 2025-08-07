# Power BI Integration Guide

## Quick Start

1. **Export Data from NeuroShield**
   ```bash
   cd powerbi
   python data_exporter.py
   ```

2. **Import to Power BI Desktop**
   - Open Power BI Desktop
   - Get Data → Text/CSV
   - Import the generated CSV files:
     - threat_logs_powerbi.csv
     - threat_detections_powerbi.csv  
     - blocked_ips_powerbi.csv

3. **Create Visualizations**
   Use these suggested charts:
   - **Threats Over Time**: Line chart (detection_time vs count)
   - **Threat Types**: Pie chart (threat_type distribution)
   - **Top Attacking IPs**: Bar chart (IP addresses vs attack count)
   - **Confidence Scores**: Histogram (confidence_percentage distribution)

## Data Fields

### threat_logs_powerbi.csv
- id: Unique log identifier
- timestamp: When the request occurred
- ip: Source IP address
- method: HTTP method (GET, POST, etc.)
- endpoint: Target URL path
- payload_preview: First 100 characters of attack payload
- response_time: Server response time in ms
- status_code: HTTP response code
- threat_type: Type of attack detected (SQLi, XSS, etc.)
- confidence_percentage: AI confidence score (0-100%)

### threat_detections_powerbi.csv  
- id: Detection record ID
- detection_time: When threat was detected
- threat_type: Attack classification
- confidence_percentage: AI confidence (0-100%)
- ip: Attacking IP address
- endpoint: Target endpoint
- method: HTTP method used

### blocked_ips_powerbi.csv
- ip: Blocked IP address
- reason: Why IP was blocked
- blocked_time: When block was applied
- status: Block status (active/inactive)

## Sample Power BI Dashboard Sections

1. **Executive Summary**
   - Total threats detected (Card)
   - Blocked IPs count (Card) 
   - Average confidence score (Card)
   - Threats by day (Line chart)

2. **Threat Analysis**
   - Threat type distribution (Donut chart)
   - Top attacking countries (Map)
   - Confidence score trends (Line chart)
   - Attack methods breakdown (Bar chart)

3. **Network Security**
   - Blocked IPs table
   - Response time analysis
   - Status code distribution
   - Geographic threat map

4. **AI Model Performance**
   - Confidence score histogram
   - Detection accuracy metrics
   - False positive analysis
   - Model effectiveness trends

## Refresh Data

To update Power BI with latest data:
1. Run `python data_exporter.py` again
2. In Power BI Desktop, click "Refresh" 
3. All charts will update with new data

## Tips for Better Visualizations

- Use filters for date ranges and threat types
- Create drill-down reports from summary to detail
- Add conditional formatting for high-confidence threats
- Use bookmarks for different dashboard views
- Set up automatic data refresh if publishing to Power BI Service