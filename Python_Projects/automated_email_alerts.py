"""
Project: Automated Email Alerts for Data Anomalies

Description:
This script automates the process of sending email alerts when significant deviations
are detected in data. It integrates with the anomaly detection from `automated_reporting.py`
and sends notifications via email.

Dependencies:
- pandas
- numpy
- smtplib (built-in)
- email (built-in)

To install dependencies, run:
pip install pandas numpy
"""

import pandas as pd
import numpy as np
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def detect_significant_deviations():
    """Detects significant deviations in metric values using rolling averages."""
    data = pd.DataFrame({
        'date': pd.date_range('2024-01-01', periods=30),
        'metric': [100, 110, 95, 120, 115, 118, 123, 125, 130, 128, 132, 135, 140, 138, 145, 148, 150, 155, 160, 158, 162, 165, 170, 172, 175, 172, 178, 180, 182, 185]
    })

    data['rolling_avg'] = data['metric'].rolling(window=7, min_periods=1).mean()
    data['deviation'] = data['metric'] - data['rolling_avg']
    threshold = data['metric'].std() * 1.5
    significant_deviations = data[np.abs(data['deviation']) > threshold]

    if significant_deviations.empty:
        print("No significant deviations detected.")
    else:
        print("Significant Deviations Detected:")
        print(significant_deviations)
        send_email_alert(significant_deviations)

def send_email_alert(deviation_data):
    """Sends an email alert with details of significant deviations."""
    sender_email = "your_email@example.com"
    receiver_email = "recipient@example.com"
    subject = "ALERT: Significant Data Deviation Detected"
    
    # Email content
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject
    
    body = f"""Hello,

Significant deviations in today's metrics have been detected:

{deviation_data.to_string(index=False)}

Please review the details above.

Best,
Automated Alert System"""
    
    msg.attach(MIMEText(body, 'plain'))
    
    # SMTP setup (update with actual SMTP server details)
    try:
        smtp = smtplib.SMTP('smtp.example.com', 587)
        smtp.starttls()
        smtp.login("your_email@example.com", "your_password")
        smtp.sendmail(sender_email, receiver_email, msg.as_string())
        smtp.quit()
        print("Alert email sent successfully.")
    except Exception as e:
        print(f"Error sending email: {e}")

if __name__ == "__main__":
    detect_significant_deviations()
