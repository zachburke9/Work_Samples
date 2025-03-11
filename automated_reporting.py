"""
Project: Automated Reporting and Anomaly Detection

Description:
This Python script automates the detection of significant deviations or anomalies in key metrics using rolling averages. 
It dynamically identifies anomalies based on statistical thresholds, providing clear and actionable output.

There are numerous methods, applications, and programming languages that can facilitate automated reporting tasks. 
My expertise primarily includes relational databases such as Microsoft SQL Server (T-SQL), Oracle Database (PL/SQL), 
and workflow management tools like Alteryx, Apache Airflow, and DBT. With this script, I demonstrate proficiency in 
transitioning these reporting processes into Python, enhancing efficiency, readability, and maintainability.

Key Features:
- Rolling average calculation for anomaly detection
- Configurable threshold for deviation sensitivity
- Clear, actionable output for efficient decision-making

Dependencies:
- pandas
- numpy

To install dependencies, run:
pip install pandas numpy
"""


import pandas as pd
import numpy as np

def detect_significant_deviations():
    """Detects significant deviations in metric values using rolling averages."""
    data = pd.DataFrame({
        'date': pd.date_range('2024-01-01', periods=30),
        'metric': [100, 110, 95, 120, 115, 118, 123, 125, 130, 128, 132, 135, 140, 138, 145, 148, 150, 155, 160, 158, 162, 165, 170, 172, 175, 172, 178, 180, 182, 185]
    })

    # Calculate rolling average with a minimum number of periods to avoid NaN values
    data['rolling_avg'] = data['metric'].rolling(window=7, min_periods=1).mean()
    data['deviation'] = data['metric'] - data['rolling_avg']
    threshold = data['metric'].std() * 1.5  # Adjust sensitivity if needed
    significant_deviations = data[np.abs(data['deviation']) > threshold]

    if significant_deviations.empty:
        print("No significant deviations detected.")
    else:
        print("Significant Deviations Detected:")
        print(significant_deviations)

if __name__ == "__main__":
    detect_significant_deviations()
