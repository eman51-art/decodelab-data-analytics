"""
DecodeLab Data Analytics Internship - Task 2: EDA
Professional Chart Edition (Combined Script)
Theme: Custom Blue Palette | Black Outlines | Straight Font | No Grid
Author: Eman Iqbal
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

# ------------------------------------------------------------------
# 1. GLOBAL SETUP & THEME
# ------------------------------------------------------------------
os.makedirs('charts', exist_ok=True)

# Custom 5-Color Blue Palette (Darkest to Lightest)
PALETTE = ['#056583', '#37849c', '#69a3b5', '#9bc1cd', '#cde0e6']
PRIMARY_BLUE = '#056583'

# Global Plot Styling
plt.rcParams['figure.dpi'] = 150
plt.rcParams['savefig.dpi'] = 300
plt.rcParams['font.family'] = 'DejaVu Sans'
plt.rcParams['axes.titleweight'] = 'bold'
plt.rcParams['axes.titlesize'] = 18
plt.rcParams['axes.labelsize'] = 12
plt.rcParams['axes.labelcolor'] = PRIMARY_BLUE
plt.rcParams['xtick.color'] = '#333333'
plt.rcParams['ytick.color'] = '#333333'
plt.rcParams['figure.facecolor'] = 'white'
plt.rcParams['savefig.facecolor'] = 'white'

# ------------------------------------------------------------------
# 2. LOAD DATA
# ------------------------------------------------------------------
print("Loading data...")
df = pd.read_excel('Cleaned_Dataset.xlsx')
df['Date'] = pd.to_datetime(df['Date'])
df['Month'] = df['Date'].dt.month_name()
df['Year'] = df['Date'].dt.year

total_orders = len(df)
print("Data loaded successfully!\n")
print("="*60)
print("GENERATING 8 PROFESSIONAL CHARTS...")
print("="*60)

# ------------------------------------------------------------------
# CHART 1: Top 5 Products by Revenue
# ------------------------------------------------------------------
def chart1_top_revenue():
    top_products = df.groupby('Product')['TotalPrice'].sum().sort_values(ascending=False).head(5)
    fig, ax = plt.subplots(figsize=(10, 6))
    
    bars = ax.barh(top_products.index, top_products.values, color=PALETTE, height=0.6, edgecolor='white', zorder=3)
    for bar, val in zip(bars, top_products.values):
        ax.text(val + (top_products.max() * 0.02), bar.get_y() + bar.get_height() / 2,
                f'${val:,.0f}', va='center', ha='left', fontsize=11, fontweight='bold', color=PRIMARY_BLUE)
    
    ax.set_xlabel('Total Revenue ($)', fontweight='bold', labelpad=10)
    ax.set_yticklabels(top_products.index, fontsize=11)
    ax.set_xticks([])
    ax.grid(False)
    ax.spines['top'].set_visible(False); ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_visible(False); ax.spines['left'].set_color('#cccccc')
    ax.invert_yaxis()
    
    fig.suptitle('Top 5 Products by Revenue', y=0.98)
    fig.text(0.5, 0.92, f"'{top_products.index[0]}' leads with ${top_products.iloc[0]:,.0f} in total sales", 
             ha='center', fontsize=11, color='#666666', style='italic')
    fig.text(0.01, 0.01, 'Source: DecodeLab Cleaned E-Commerce Dataset | Task 2 EDA', fontsize=9, color='#999999')
    
    plt.tight_layout(rect=[0, 0.03, 1, 0.88])
    plt.savefig('charts/top_5_revenue.png', bbox_inches='tight')
    plt.close()
    print("✅ Chart 1 saved: top_5_revenue.png")

# ------------------------------------------------------------------
# CHART 2: Top 5 Products by Quantity
# ------------------------------------------------------------------
def chart2_top_quantity():
    top_products = df.groupby('Product')['Quantity'].sum().sort_values(ascending=False).head(5)
    fig, ax = plt.subplots(figsize=(10, 6))
    
    bars = ax.barh(top_products.index, top_products.values, color=PALETTE, height=0.6, edgecolor='white', zorder=3)
    for bar, val in zip(bars, top_products.values):
        ax.text(val + (top_products.max() * 0.02), bar.get_y() + bar.get_height() / 2,
                f'{val:,} units', va='center', ha='left', fontsize=11, fontweight='bold', color=PRIMARY_BLUE)
    
    ax.set_xlabel('Units Sold', fontweight='bold', labelpad=10)
    ax.set_yticklabels(top_products.index, fontsize=11)
    ax.set_xticks([])
    ax.grid(False)
    ax.spines['top'].set_visible(False); ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_visible(False); ax.spines['left'].set_color('#cccccc')
    ax.invert_yaxis()
    
    fig.suptitle('Top 5 Products by Quantity Sold', y=0.98)
    fig.text(0.5, 0.92, f"'{top_products.index[0]}' dominates volume with {top_products.iloc[0]:,} units", 
             ha='center', fontsize=11, color='#666666', style='italic')
    fig.text(0.01, 0.01, 'Source: DecodeLab Cleaned E-Commerce Dataset | Task 2 EDA', fontsize=9, color='#999999')
    
    plt.tight_layout(rect=[0, 0.03, 1, 0.88])
    plt.savefig('charts/top_5_quantity.png', bbox_inches='tight')
    plt.close()
    print("✅ Chart 2 saved: top_5_quantity.png")

# ------------------------------------------------------------------
# CHART 3: Monthly Order Trend
# ------------------------------------------------------------------
def chart3_monthly_trend():
    month_order = ['January', 'February', 'March', 'April', 'May', 'June', 
                   'July', 'August', 'September', 'October', 'November', 'December']
    monthly_orders = df['Month'].value_counts().reindex(month_order)
    peak_month, peak_val = monthly_orders.idxmax(), monthly_orders.max()
    low_month, low_val = monthly_orders.idxmin(), monthly_orders.min()
    
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.plot(monthly_orders.index, monthly_orders.values, color=PRIMARY_BLUE, linewidth=2.5, 
            marker='o', markersize=8, markerfacecolor='white', markeredgecolor='black', markeredgewidth=1.5, zorder=3)
    ax.fill_between(range(len(monthly_orders)), monthly_orders.values, color=PALETTE[4], alpha=0.4, zorder=1)
    
    ax.annotate(f'Peak: {peak_val} orders', xy=(peak_month, peak_val), xytext=(0, 15), textcoords='offset points', 
                ha='center', fontsize=10, fontweight='bold', color=PRIMARY_BLUE)
    ax.annotate(f'Low: {low_val} orders', xy=(low_month, low_val), xytext=(0, -20), textcoords='offset points', 
                ha='center', fontsize=10, fontweight='bold', color='#666666')
    
    ax.set_xlabel('Month', fontweight='bold', labelpad=10)
    ax.set_ylabel('Number of Orders', fontweight='bold', labelpad=10)
    ax.tick_params(axis='x', rotation=0, labelsize=10) # Straight font
    ax.grid(False)
    ax.spines['top'].set_visible(False); ax.spines['right'].set_visible(False)
    ax.spines['left'].set_color('#cccccc'); ax.spines['bottom'].set_color('#cccccc')
    
    fig.suptitle('Monthly Order Volume Trend', y=0.98)
    fig.text(0.5, 0.92, f"Seasonal dip visible in {low_month} — plan campaigns ahead of Q3 slowdown", 
             ha='center', fontsize=11, color='#666666', style='italic')
    fig.text(0.01, 0.01, 'Source: DecodeLab Cleaned E-Commerce Dataset | Task 2 EDA', fontsize=9, color='#999999')
    
    plt.tight_layout(rect=[0, 0.03, 1, 0.88])
    plt.savefig('charts/monthly_trend.png', bbox_inches='tight')
    plt.close()
    print("✅ Chart 3 saved: monthly_trend.png")

# ------------------------------------------------------------------
# CHART 4: Yearly Order Trend
# ------------------------------------------------------------------
def chart4_yearly_trend():
    yearly_orders = df.groupby('Year').size().sort_index()
    fig, ax = plt.subplots(figsize=(10, 6))
    
    bars = ax.bar(yearly_orders.index.astype(str), yearly_orders.values, color=PALETTE[:3], 
                  edgecolor='black', linewidth=1.2, width=0.5, zorder=3) # Black outline
    
    for bar in bars:
        ax.annotate(f'{bar.get_height():,}', xy=(bar.get_x() + bar.get_width() / 2, bar.get_height()),
                    xytext=(0, 8), textcoords="offset points", ha='center', va='bottom', 
                    fontsize=11, fontweight='bold', color=PRIMARY_BLUE)
    
    ax.set_xlabel('Year', fontweight='bold', labelpad=10)
    ax.set_ylabel('Number of Orders', fontweight='bold', labelpad=10)
    ax.tick_params(axis='x', rotation=0, labelsize=12) # Straight font
    ax.set_ylim(0, yearly_orders.max() * 1.15)
    ax.grid(False)
    ax.spines['top'].set_visible(False); ax.spines['right'].set_visible(False)
    ax.spines['left'].set_color('#cccccc'); ax.spines['bottom'].set_color('#cccccc')
    
    fig.suptitle('Yearly Order Volume Trend', y=0.98)
    fig.text(0.5, 0.92, "Year-over-year order volume analysis (2023–2025)", 
             ha='center', fontsize=11, color='#666666', style='italic')
    fig.text(0.01, 0.01, 'Source: DecodeLab Cleaned E-Commerce Dataset | Task 2 EDA', fontsize=9, color='#999999')
    
    plt.tight_layout(rect=[0, 0.03, 1, 0.88])
    plt.savefig('charts/yearly_trend.png', bbox_inches='tight')
    plt.close()
    print("✅ Chart 4 saved: yearly_trend.png")

# ------------------------------------------------------------------
# CHART 5: Revenue by Referral Source
# ------------------------------------------------------------------
def chart5_referral_revenue():
    referral_revenue = df.groupby('ReferralSource')['TotalPrice'].sum().sort_values(ascending=False)
    fig, ax = plt.subplots(figsize=(10, 6))
    
    bars = ax.bar(referral_revenue.index, referral_revenue.values, color=PALETTE[:len(referral_revenue)], 
                  edgecolor='black', linewidth=1.2, width=0.5, zorder=3) # Black outline
    
    for bar in bars:
        ax.annotate(f'${bar.get_height():,.0f}', xy=(bar.get_x() + bar.get_width() / 2, bar.get_height()),
                    xytext=(0, 8), textcoords="offset points", ha='center', va='bottom', 
                    fontsize=10, fontweight='bold', color=PRIMARY_BLUE)
    
    ax.set_xlabel('Referral Source', fontweight='bold', labelpad=10)
    ax.set_ylabel('Revenue ($)', fontweight='bold', labelpad=10)
    ax.tick_params(axis='x', rotation=0, labelsize=11) # Straight font
    ax.set_ylim(0, referral_revenue.max() * 1.15)
    ax.grid(False)
    ax.spines['top'].set_visible(False); ax.spines['right'].set_visible(False)
    ax.spines['left'].set_color('#cccccc'); ax.spines['bottom'].set_color('#cccccc')
    
    fig.suptitle('Revenue by Referral Source', y=0.98)
    fig.text(0.5, 0.92, f"'{referral_revenue.index[0]}' is the top-performing channel — prioritize ad spend here", 
             ha='center', fontsize=11, color='#666666', style='italic')
    fig.text(0.01, 0.01, 'Source: DecodeLab Cleaned E-Commerce Dataset | Task 2 EDA', fontsize=9, color='#999999')
    
    plt.tight_layout(rect=[0, 0.03, 1, 0.88])
    plt.savefig('charts/referral_revenue.png', bbox_inches='tight')
    plt.close()
    print("✅ Chart 5 saved: referral_revenue.png")

# ------------------------------------------------------------------
# CHART 6: Payment Method Distribution (Donut)
# ------------------------------------------------------------------
def chart6_payment_donut():
    pay_counts = df['PaymentMethod'].value_counts()
    fig, ax = plt.subplots(figsize=(9, 9))
    
    wedges, texts, autotexts = ax.pie(pay_counts.values, labels=None, autopct='%1.1f%%', startangle=90, 
                                      pctdistance=0.85, colors=PALETTE[:len(pay_counts)], 
                                      wedgeprops=dict(width=0.45, edgecolor='black', linewidth=1.5)) # Black outline
    
    for t in autotexts:
        t.set_fontsize(11); t.set_fontweight('bold'); t.set_color('white')
    
    ax.text(0, 0.08, f'{total_orders:,}', ha='center', va='center', fontsize=26, fontweight='bold', color=PRIMARY_BLUE)
    ax.text(0, -0.12, 'Total Orders', ha='center', va='center', fontsize=12, color='#666666')
    
    # Legend (Fixed for older matplotlib)
    ax.legend(wedges, pay_counts.index, loc='center left', bbox_to_anchor=(1.05, 0.5), 
              frameon=False, fontsize=11, title='Payment Method', title_fontsize=12)
    
    fig.suptitle('Payment Method Distribution', y=0.98)
    fig.text(0.5, 0.92, "Most preferred payment methods among customers", 
             ha='center', fontsize=11, color='#666666', style='italic')
    fig.text(0.01, 0.01, 'Source: DecodeLab Cleaned E-Commerce Dataset | Task 2 EDA', fontsize=9, color='#999999')
    
    plt.tight_layout(rect=[0, 0.03, 0.85, 0.88])
    plt.savefig('charts/payment_donut.png', bbox_inches='tight')
    plt.close()
    print("✅ Chart 6 saved: payment_donut.png")

# ------------------------------------------------------------------
# CHART 7: Order Status Distribution (Pie)
# ------------------------------------------------------------------
def chart7_order_status():
    status_counts = df['OrderStatus'].value_counts()
    fig, ax = plt.subplots(figsize=(9, 9))
    
    wedges, texts, autotexts = ax.pie(status_counts.values, labels=None, autopct='%1.1f%%', startangle=90, 
                                      pctdistance=0.85, colors=PALETTE[:len(status_counts)], 
                                      wedgeprops=dict(edgecolor='black', linewidth=1.5)) # Black outline
    
    for t in autotexts:
        t.set_fontsize(11); t.set_fontweight('bold'); t.set_color('white')
    
    # Legend (Fixed for older matplotlib)
    ax.legend(wedges, status_counts.index, loc='center left', bbox_to_anchor=(1.05, 0.5), 
              frameon=False, fontsize=11, title='Order Status', title_fontsize=12)
    
    fig.suptitle('Order Status Distribution', y=0.98)
    fig.text(0.5, 0.92, "Monitor cancellation and return rates for operational health", 
             ha='center', fontsize=11, color='#666666', style='italic')
    fig.text(0.01, 0.01, 'Source: DecodeLab Cleaned E-Commerce Dataset | Task 2 EDA', fontsize=9, color='#999999')
    
    plt.tight_layout(rect=[0, 0.03, 0.85, 0.88])
    plt.savefig('charts/order_status.png', bbox_inches='tight')
    plt.close()
    print("✅ Chart 7 saved: order_status.png")

# ------------------------------------------------------------------
# CHART 8: Coupon Code Effectiveness (Grouped Bar)
# ------------------------------------------------------------------
def chart8_coupon_effectiveness():
    stats = df.groupby('CouponCode').agg(Revenue=('TotalPrice', 'sum'), AOV=('TotalPrice', 'mean')).sort_values('Revenue', ascending=False)
    fig, ax1 = plt.subplots(figsize=(11, 6.5))
    ax2 = ax1.twinx()
    
    x = np.arange(len(stats))
    width = 0.35
    
    # Black outlines on both bar sets
    bars1 = ax1.bar(x - width/2, stats['Revenue'], width, label='Total Revenue', color=PALETTE[0], edgecolor='black', linewidth=1.2, zorder=3)
    bars2 = ax2.bar(x + width/2, stats['AOV'], width, label='Avg Order Value', color=PALETTE[2], edgecolor='black', linewidth=1.2, zorder=3)
    
    for bar in bars1:
        ax1.annotate(f'${bar.get_height():,.0f}', xy=(bar.get_x() + bar.get_width() / 2, bar.get_height()),
                     xytext=(0, 8), textcoords="offset points", ha='center', va='bottom', fontsize=10, fontweight='bold', color=PALETTE[0])
    for bar in bars2:
        ax2.annotate(f'${bar.get_height():,.0f}', xy=(bar.get_x() + bar.get_width() / 2, bar.get_height()),
                     xytext=(0, 8), textcoords="offset points", ha='center', va='bottom', fontsize=10, fontweight='bold', color=PALETTE[2])
    
    ax1.set_ylabel('Total Revenue ($)', fontweight='bold', labelpad=10, color=PALETTE[0])
    ax2.set_ylabel('Average Order Value ($)', fontweight='bold', labelpad=10, color=PALETTE[2])
    ax1.set_xticks(x)
    ax1.set_xticklabels(stats.index, rotation=0, ha='center', fontsize=11) # Straight font
    
    ax1.grid(False); ax2.grid(False)
    ax1.spines['top'].set_visible(False); ax2.spines['top'].set_visible(False)
    ax1.spines['left'].set_color('#cccccc'); ax2.spines['right'].set_color('#cccccc')
    
    # Legend (Fixed for older matplotlib)
    fig.legend([bars1, bars2], ['Total Revenue', 'Avg Order Value'], loc='upper right', bbox_to_anchor=(0.92, 0.90), 
               frameon=False, fontsize=11, title='Metrics', title_fontsize=12)
    
    fig.suptitle('Coupon Code Effectiveness', y=0.98)
    fig.text(0.5, 0.92, "Revenue vs Average Order Value by Coupon", ha='center', fontsize=11, color='#666666', style='italic')
    fig.text(0.01, 0.01, 'Source: DecodeLab Cleaned E-Commerce Dataset | Task 2 EDA', fontsize=9, color='#999999')
    
    plt.tight_layout(rect=[0, 0.03, 1, 0.88])
    plt.savefig('charts/coupon_grouped.png', bbox_inches='tight')
    plt.close()
    print("✅ Chart 8 saved: coupon_grouped.png")

# ------------------------------------------------------------------
# RUN ALL CHARTS
# ------------------------------------------------------------------
if __name__ == "__main__":
    chart1_top_revenue()
    chart2_top_quantity()
    chart3_monthly_trend()
    chart4_yearly_trend()
    chart5_referral_revenue()
    chart6_payment_donut()
    chart7_order_status()
    chart8_coupon_effectiveness()
    
    print("="*60)
    print("🎉 ALL 8 CHARTS GENERATED SUCCESSFULLY IN '/charts' FOLDER!")
    print("="*60)