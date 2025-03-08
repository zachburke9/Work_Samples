"""
Project: Mentorship & Technical Leadership

Description:
This script contains training examples for junior analysts, covering data validation
and structured coding techniques.

Dependencies:
- pandas

To install dependencies, run:
pip install pandas
"""

import pandas as pd

def sales_analysis_example():
    """Demonstrates grouping and summing in pandas for mentorship purposes."""
    data = {
        'Category': ['A', 'B', 'A', 'C', 'B'],
        'Sales': [100, 200, 150, 300, 250]
    }
    df = pd.DataFrame(data)
    sales_by_category = df.groupby('Category')['Sales'].sum().reset_index()
    print("Total sales by category:")
    print(sales_by_category)

def data_validation_example():
    """Basic data validation checks for missing values, duplicates, and out-of-range values."""
    data = {
        'id': [1, 2, 3, 4, 5, 5],
        'age': [25, 37, 19, 52, -1, 44],
        'name': ['Alice', 'Bob', None, 'Diana', 'Ethan', 'Frank']
    }
    df = pd.DataFrame(data)

    if df.isnull().values.any():
        print("Warning: Missing values detected")
        print(df[df.isnull().any(axis=1)])

    duplicate_rows = df[df.duplicated('id', keep=False)]
    if not duplicate_rows.empty:
        print("Warning: Duplicate IDs found:")
        print(duplicate_rows)

    invalid_ages = df[df['age'] < 0]
    if not invalid_ages.empty:
        print("Warning: Invalid age values detected:")
        print(invalid_ages)

if __name__ == "__main__":
    sales_analysis_example()
    data_validation_example()
