"""
E-Commerce Order Data Cleaning Pipeline
---------------------------------------
This script loads raw order data, handles missing values, 
removes duplicates, and validates business logic (pricing math).

Author: Eman Iqbal
"""

import pandas as pd
import numpy as np

def clean_data(input_file, output_file):
    """
    Loads raw data, cleans it, and saves the final version.
    """
    print(f"Loading data from {input_file}...")
    df = pd.read_excel(input_file)
    print(f"Initial shape: {df.shape}")

    # 1. Handle Missing Data
    # Business logic: Blank coupons mean the customer paid full price.
    # We label them 'NO_COUPON' instead of dropping the rows.
    df['CouponCode'] = df['CouponCode'].fillna('NO_COUPON')
    print("Filled missing CouponCodes with 'NO_COUPON'.")

    # 2. Remove Duplicates
    initial_rows = df.shape[0]
    df = df.drop_duplicates()
    dropped_rows = initial_rows - df.shape[0]
    print(f"Removed {dropped_rows} duplicate rows.")

    # 3. Sanity Check (Business Logic Validation)
    # Verify that Quantity * UnitPrice == TotalPrice
    df['Expected_Total'] = df['Quantity'] * df['UnitPrice']
    errors = df[round(df['Expected_Total'], 2) != round(df['TotalPrice'], 2)]
    
    print(f"Rows with pricing discrepancies: {len(errors)}")
    
    # Drop the helper column so it doesn't end up in the final Excel file
    df = df.drop(columns=['Expected_Total'])

    # 4. Save Cleaned Data
    # index=False prevents Pandas from writing row numbers into the Excel file
    df.to_excel(output_file, index=False)
    print(f"✅ Cleaning complete! Saved to {output_file}")

if __name__ == "__main__":
    # Define file paths
    RAW_DATA = 'Dataset for Data Analytics.xlsx'
    CLEAN_DATA = 'Cleaned_Dataset.xlsx'
    
    # Run the cleaning function
    clean_data(RAW_DATA, CLEAN_DATA)
