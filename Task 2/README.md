# 📊 DecodeLab Data Analytics Internship – Task 2: Exploratory Data Analysis (EDA)

## 📌 Overview
This repository contains **Task 2** of the DecodeLab Data Analytics Internship. The objective of this task is to perform **Exploratory Data Analysis (EDA)** on the cleaned e-commerce dataset prepared in Task 1. 

The analysis focuses on identifying meaningful business insights, discovering seasonal trends, and evaluating key performance indicators (KPIs) to support data-driven business decisions.

---

## 🎯 Objectives
* Analyze product and revenue performance to identify top contributors.
* Identify monthly and yearly sales trends for inventory planning.
* Understand customer purchasing behavior and payment preferences.
* Evaluate marketing channel (Referral Source) performance.
* Assess coupon code effectiveness and revenue impact.
* Monitor operational health through order status analysis.

---

## 🛠️ Tools & Technologies
* **Language:** Python 3.x
* **Libraries:** Pandas (Data Manipulation), NumPy (Numerical Operations), Matplotlib/Seaborn (Data Visualization)
* **Environment:** Google Colab / VS Code
* **Version Control:** Git & GitHub

---

## 📈 Key Business Insights

### 📦 1. Product & Revenue Analysis
* **Top 3 Products by Revenue:** 'Chair' ($195,620), 'Printer' ($195,612), and 'Laptop' ($192,126) are the highest revenue generators. The business must ensure optimal inventory for these items to maximize profit.
* **Top 3 Products by Quantity Sold:** 'Chair' (562 units), 'Printer' (542 units), and 'Laptop' (535 units) dominate sales volume. This indicates consistently high demand, requiring proactive stock replenishment.
* **Average Order Value (AOV):** The average customer spends **$[Insert AOV here, e.g., 1,053.50]** per order. *(Calculated as Total Revenue / Total Orders)*.

### 📅 2. Time-Based Trends
* **Monthly Sales Trend:** Order volume shows clear seasonality, peaking in **June (147 orders)** and hitting its lowest point in **September (73 orders)**. Marketing campaigns should be launched in August/September to counter the Q3 slump.
* **Yearly Order Trend:** Order volume shows a year-over-year decline, peaking in **2023 (510 orders)** before dropping in **2024 (459 orders)** and **2025 (231 orders)**. Management should investigate root causes (e.g., reduced marketing spend or customer retention issues).
* **Highest-Selling Product by Month:** While 'Chair' dominates overall volume, specific months show spikes in other categories (e.g., [Insert observation, e.g., 'Laptop' spikes in specific months]), indicating seasonal or B2B demand cycles.

### 👥 3. Customer & Marketing Behavior
* **Top Referral Source by Revenue:** **[Insert Top Source, e.g., Instagram/Google]** drives the highest total revenue. Ad spend should be prioritized on this platform for maximum ROI.
* **Coupon Code Effectiveness:** 'FREESHIP' is the top revenue generator ($335,036) with the highest Average Order Value ($1,070). Interestingly, 'NO_COUPON' is a close second ($322,401), proving that ~25% of customers are loyal enough to buy at full price without needing a discount.
* **Most Preferred Payment Method:** **[Insert Top Method, e.g., Credit Card]** is the most frequently used payment method, indicating the need for a seamless and secure payment gateway experience.

### ⚙️ 4. Operational Health
* **Order Status Distribution:** The majority of orders are successfully processed. However, **[Insert %]** are Cancelled and **[Insert %]** are Returned. Investigating high-return categories (like electronics) could save the business significant revenue and improve customer satisfaction.

---

## 📁 Repository Structure
```text
Task-2-EDA/
│── README.md                 # This file: Project documentation and insights
│── eda_analysis.ipynb        # Jupyter Notebook containing all Python code and visualizations
│── Cleaned_Dataset.xlsx      # The cleaned dataset from Task 1
│── charts/                   # Folder containing generated visualization images
│   ├── top_3_products_revenue.png
│   ├── monthly_sales_trend.png
│   ├── coupon_effectiveness.png
│   └── order_status_distribution.png
