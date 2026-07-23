"""
DecodeLab Data Analytics Internship - Task 2: Exploratory Data Analysis (EDA)
-----------------------------------------------------------------------------
This script analyzes the cleaned e-commerce dataset to extract key business 
insights regarding product performance, time-based trends, customer behavior, 
and operational health. It also generates visualizations for the GitHub README.

Author: Eman Iqbal
Role: Data Analytics Intern at DecodeLab
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

# ==========================================
# 0. SETUP & DATA LOADING
# ==========================================
# Create a 'charts' directory to save our visualizations
os.makedirs('charts', exist_ok=True)

# Load the cleaned dataset from Task 1
print("Loading data...")
df = pd.read_excel('Cleaned_Dataset.xlsx')
print(f"Dataset loaded successfully. Shape: {df.shape}\n")

# ==========================================
# 1. PRODUCT & REVENUE ANALYSIS
# ==========================================
print("="*50)
print("1. PRODUCT & REVENUE ANALYSIS")
print("="*50)

# Top 3 Products by Revenue
top_revenue = df.groupby('Product')['TotalPrice'].sum().sort_values(ascending=False).head(3)
print("\n--- Top 3 Products by Revenue ---")
print(top_revenue)

# Top 3 Products by Quantity Sold
top_quantity = df.groupby('Product')['Quantity'].sum().sort_values(ascending=False).head(3)
print("\n--- Top 3 Products by Quantity Sold ---")
print(top_quantity)

# Average Order Value (AOV)
aov = df['TotalPrice'].mean()
print(f"\n--- Average Order Value (AOV) ---")
print(f"AOV: ${aov:.2f}")

# ==========================================
# 2. TIME-BASED TRENDS
# ==========================================
print("\n" + "="*50)
print("2. TIME-BASED TRENDS")
print("="*50)

# Extract Month and Year
df['Month'] = df['Date'].dt.month_name()
df['Year'] = df['Date'].dt.year

# Total Orders by Month (Chronological)
month_order = ['January', 'February', 'March', 'April', 'May', 'June', 
               'July', 'August', 'September', 'October', 'November', 'December']
monthly_orders = df['Month'].value_counts().reindex(month_order)
print("\n--- Total Orders by Month ---")
print(monthly_orders)

# Total Orders by Year
yearly_orders = df['Year'].value_counts().sort_index()
print("\n--- Total Orders by Year ---")
print(yearly_orders)

# Highest-Selling Product by Month
monthly_product_sales = df.groupby(['Month', 'Product'])['Quantity'].sum().reset_index()
top_product_per_month = monthly_product_sales.sort_values(['Month', 'Quantity'], ascending=[True, False]).drop_duplicates('Month')
top_product_per_month['Month'] = pd.Categorical(top_product_per_month['Month'], categories=month_order, ordered=True)
top_product_per_month = top_product_per_month.sort_values('Month')
print("\n--- Highest-Selling Product by Month ---")
print(top_product_per_month[['Month', 'Product', 'Quantity']].to_string(index=False))

# ==========================================
# 3. CUSTOMER & MARKETING BEHAVIOR
# ==========================================
print("\n" + "="*50)
print("3. CUSTOMER & MARKETING BEHAVIOR")
print("="*50)

# Top Referral Source by Revenue
top_referral_revenue = df.groupby('ReferralSource')['TotalPrice'].sum().sort_values(ascending=False)
print("\n--- Top Referral Sources by Revenue ---")
print(top_referral_revenue)

# Coupon Code Effectiveness
coupon_analysis = df.groupby('CouponCode').agg(
    Total_Revenue=('TotalPrice', 'sum'),
    Total_Orders=('OrderID', 'count'),
    Avg_Order_Value=('TotalPrice', 'mean')
).sort_values(by='Total_Revenue', ascending=False)
print("\n--- Coupon Code Effectiveness ---")
print(coupon_analysis)

# Most Preferred Payment Method
top_payment = df['PaymentMethod'].value_counts().head(3)
print("\n--- Top 3 Most Preferred Payment Methods ---")
print(top_payment)

# ==========================================
# 4. OPERATIONAL HEALTH
# ==========================================
print("\n" + "="*50)
print("4. OPERATIONAL HEALTH")
print("="*50)

# Order Status Distribution (%)
order_status_pct = df['OrderStatus'].value_counts(normalize=True) * 100
print("\n--- Order Status Distribution (%) ---")
print(order_status_pct.round(2))


# ==========================================
# 5. DATA VISUALIZATION (For GitHub README)
# ==========================================
print("\n" + "="*50)
print("GENERATING VISUALIZATIONS...")
print("="*50)

# Set style for plots
sns.set_theme(style="whitegrid")
plt.rcParams['figure.figsize'] = (10, 6)

# Chart 1: Top 3 Products by Revenue
plt.figure()
sns.barplot(x=top_revenue.values, y=top_revenue.index, palette="Blues_r")
plt.title('Top 3 Products by Revenue')
plt.xlabel('Total Revenue ($)')
plt.ylabel('Product')
plt.tight_layout()
plt.savefig('charts/top_3_products_revenue.png', dpi=300)
plt.close()

# Chart 2: Monthly Sales Trend
plt.figure()
sns.barplot(x=monthly_orders.index, y=monthly_orders.values, palette="viridis")
plt.title('Total Orders by Month')
plt.xlabel('Month')
plt.ylabel('Number of Orders')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('charts/monthly_sales_trend.png', dpi=300)
plt.close()

# Chart 3: Coupon Code Effectiveness (Revenue)
plt.figure()
sns.barplot(x=coupon_analysis.index, y=coupon_analysis['Total_Revenue'], palette="Greens_r")
plt.title('Total Revenue by Coupon Code')
plt.xlabel('Coupon Code')
plt.ylabel('Total Revenue ($)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('charts/coupon_effectiveness.png', dpi=300)
plt.close()

# Chart 4: Order Status Distribution
plt.figure()
plt.pie(order_status_pct, labels=order_status_pct.index, autopct='%1.1f%%', startangle=140, colors=sns.color_palette("pastel"))
plt.title('Order Status Distribution (%)')
plt.tight_layout()
plt.savefig('charts/order_status_distribution.png', dpi=300)
plt.close()

print("\n✅ Analysis Complete! All charts have been saved to the 'charts/' folder.")
print("✅ Copy the printed numbers above to fill in your README.md blanks.")
