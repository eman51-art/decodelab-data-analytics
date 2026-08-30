# 🚀 DecodeLab Data Analytics Internship

Welcome to my official repository for the **Data Analytics Internship** at **DecodeLab**.

**Author:** Eman Iqbal
**Role:** Data Analytics Intern
**Internship:** DecodeLab Data Analytics Internship

This repository showcases my ability to clean, process, analyze, query, and visually communicate insights from real-world e-commerce data using **Python**, **Pandas**, **Matplotlib**, **SQL**, and **PowerPoint**.

---

## 📂 Project Tasks

| Task | Description | Tools Used | Status |
|------|-------------|------------|--------|
| **Task 1** | End-to-End Data Cleaning Pipeline | Python, Pandas | ✅ Complete |
| **Task 2** | Exploratory Data Analysis (EDA) with Professional Visualizations | Python, Pandas, Matplotlib | ✅ Complete |
| **Task 3** | SQL Data Analysis | SQL (SQLite) | ✅ Complete |
| **Task 4** | Data Visualization & Storytelling | PowerPoint, Matplotlib | ✅ Complete |

---

## 🧹 Task 1 — Data Cleaning Pipeline

A Python script that loads raw e-commerce order data and prepares it for analysis.

**Key steps:**
- Filled missing `CouponCode` values with `NO_COUPON` (business rule: blank coupon = full price paid)
- Removed duplicate rows
- Validated business logic by checking `Quantity × UnitPrice == TotalPrice` and flagging pricing discrepancies
- Exported a clean, analysis-ready dataset: `Cleaned_Dataset.xlsx`

**File:** `task1_data_cleaning.py`
**Input:** `Dataset for Data Analytics.xlsx`
**Output:** `Cleaned_Dataset.xlsx`

```bash
python task1_data_cleaning.py
```

---

## 📊 Task 2 — Exploratory Data Analysis (EDA)

A combined script that generates **8 professional, presentation-ready charts** from the cleaned dataset, using a custom blue color palette, black outlines, clean typography, and no gridlines.

**Charts generated:**
1. Top 5 Products by Revenue
2. Top 5 Products by Quantity Sold
3. Monthly Order Volume Trend
4. Yearly Order Volume Trend
5. Revenue by Referral Source
6. Payment Method Distribution (Donut Chart)
7. Order Status Distribution (Pie Chart)
8. Coupon Code Effectiveness (Revenue vs. Avg Order Value)

**File:** `task2_eda_charts.py`
**Output folder:** `charts/`

```bash
python task2_eda_charts.py
```

---

## 🗄️ Task 3 — SQL Data Analysis

A set of SQL queries run against the cleaned dataset (loaded into `ecommerce_data.db`, table `orders`) to answer key business questions.

**Queries included:**
1. Referral source performance (orders, units sold, revenue, AOV) for high-value orders
2. Total orders by order status
3. Total revenue by product
4. Average order value by payment method
5. Lost revenue analysis (cancelled & returned orders)
6. High-value delivered orders (> $1000)

**File:** `task3_sql_analysis.sql`
**Database:** `ecommerce_data.db`

---

## 🎯 Task 4 — Data Visualization & Storytelling

A PowerPoint presentation summarizing the full analysis into a clear business narrative — key insights, trends, and actionable recommendations for stakeholders.

**Project:** E-Commerce Performance Review
**File:** `task4_ecommerce_presentation.pptx`

---

## 🛠️ Tech Stack

- **Python** — Pandas, NumPy, Matplotlib
- **SQL** — SQLite
- **PowerPoint** — Business storytelling & reporting

---

## 📁 Repository Structure

```
├── task1_data_cleaning.py
├── Dataset for Data Analytics.xlsx
├── Cleaned_Dataset.xlsx
├── task2_eda_charts.py
├── charts/
│   ├── top_5_revenue.png
│   ├── top_5_quantity.png
│   ├── monthly_trend.png
│   ├── yearly_trend.png
│   ├── referral_revenue.png
│   ├── payment_donut.png
│   ├── order_status.png
│   └── coupon_grouped.png
├── task3_sql_analysis.sql
├── task4_ecommerce_presentation.pptx
└── README.md
```

---

## 📬 Connect with Me

**Eman Iqbal**
Data Analytics Intern @ DecodeLab

---

*Last Updated: August 2026*
