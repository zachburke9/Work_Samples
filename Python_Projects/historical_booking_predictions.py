"""
Project: Historical Booking Predictions (Machine Learning)

Description:
This script trains a machine learning model to predict booking trends.

Dependencies:
- pandas
- scikit-learn

To install dependencies, run:
pip install pandas scikit-learn
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

def train_booking_model():
    """Trains a simple machine learning model to predict booking trends."""
    data = {
        'lead_time': [7, 20, 29, 15, 11, 5],
        'promo': [0, 0, 0, 1, 0, 1],
        'region': ['East', 'West', 'South', 'East', 'North', 'West'],
        'booked': [0, 0, 0, 0, 1, 1]
    }
    df = pd.DataFrame(data)
    df = pd.get_dummies(df, columns=['region'], drop_first=True)

    X = df.drop('booked', axis=1)
    y = df['booked']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Model Accuracy: {accuracy:.2f}")

if __name__ == "__main__":
    train_booking_model()
