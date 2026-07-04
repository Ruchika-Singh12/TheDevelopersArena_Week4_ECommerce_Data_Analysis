# Sales Data Analysis Report
## Week 4: Complete Data Analysis Project

**Date:** July 2026  
**Dataset:** sales_data.csv (100 rows, 7 columns)  
**Tools Used:** Python, Pandas, Matplotlib

---

## 1. Project Overview

This report documents a complete data analysis performed on an E-commerce sales dataset. The goal was to extract meaningful business insights and visualize them through professional charts.

**Columns in Dataset:**
| Column | Type | Description |
|--------|------|-------------|
| Date | String | Transaction date |
| Product | String | Product category |
| Quantity | Integer | Units sold |
| Price | Integer | Price per unit (Rs) |
| Customer_ID | String | Unique customer ID |
| Region | String | Sales region |
| Total_Sales | Integer | Quantity × Price |

---

## 2. Data Cleaning Summary

- **Missing Values:** 0 (dataset was clean)
- **Duplicate Rows:** 0 removed
- **Final Dataset:** 100 rows × 7 columns ready for analysis

---

## 3. Analysis Findings

### Metric 1: Total Revenue
> **Rs 1,23,65,048** (approx Rs 1.24 Crore)

Total revenue generated from 100 transactions across the year 2024.

---

### Metric 2: Best-Selling Product by Revenue

| Rank | Product | Revenue (Rs) | Share |
|------|---------|-------------|-------|
| 1 | **Laptop** | 38,89,210 | 31.5% |
| 2 | Tablet | 28,84,340 | 23.3% |
| 3 | Phone | 28,59,394 | 23.1% |
| 4 | Headphones | 13,84,033 | 11.2% |
| 5 | Monitor | 13,48,071 | 10.9% |

**Insight:** Laptop generates the highest revenue despite not being the cheapest product. This shows customers are willing to spend more on high-value electronics.

---

### Metric 3: Best Performing Region

| Rank | Region | Revenue (Rs) | Share |
|------|--------|-------------|-------|
| 1 | **North** | 39,83,635 | 32.2% |
| 2 | South | 37,37,852 | 30.2% |
| 3 | East | 25,19,639 | 20.4% |
| 4 | West | 21,23,922 | 17.2% |

**Insight:** North and South together account for 62.4% of all sales. West region has significant growth potential.

---

### Metric 4: Order Value Statistics

| Statistic | Value (Rs) |
|-----------|-----------|
| Average Order Value | 1,23,650 |
| Highest Single Sale | 3,73,932 |
| Lowest Single Sale | 6,540 |

**Insight:** There is high variance between the max and min sale values, indicating a wide customer spending range.

---

### Metric 5: Units Sold by Product

| Product | Units Sold |
|---------|-----------|
| Laptop | 136 units |
| Tablet | 127 units |
| Phone | 101 units |
| Monitor | 66 units |
| Headphones | 48 units |

**Insight:** Laptop leads in both revenue AND units sold — making it the clear star product of this dataset.

---

## 4. Visualizations Created

### Chart 1: Bar Chart — Sales Revenue by Product
- **File:** `visualizations/chart1_bar_product_sales.png`
- **Type:** Vertical Bar Chart
- **Purpose:** Compares total revenue across all 5 product categories
- **Key Finding:** Laptop bar is clearly the tallest

### Chart 2: Pie Chart — Region-wise Revenue Distribution
- **File:** `visualizations/chart2_pie_region_sales.png`
- **Type:** Pie Chart with percentage labels
- **Purpose:** Shows what fraction of total sales each region contributes
- **Key Finding:** North (32.2%) and South (30.2%) dominate

### Chart 3: Line Chart — Monthly Revenue Trend
- **File:** `visualizations/chart3_line_monthly_trend.png`
- **Type:** Line Chart with filled area
- **Purpose:** Shows how revenue changes month to month across 2024
- **Key Finding:** Revenue is not consistent — peaks and valleys exist

### Chart 4: Horizontal Bar — Units Sold by Product
- **File:** `visualizations/chart4_hbar_units_sold.png`
- **Type:** Horizontal Bar Chart
- **Purpose:** Compares quantity sold for each product
- **Key Finding:** Laptop and Tablet lead in quantity; Headphones are lowest

---

## 5. Key Business Insights

1. **Laptop is the star product** — Highest revenue (Rs 38.9L) and most units sold (136). Marketing should focus more on laptops.

2. **North region needs more investment** — It is the top region but only marginally ahead of South. Both regions should get priority stock allocation.

3. **West region is underperforming** — Only 17.2% of sales. Could benefit from targeted promotions or increased sales rep presence.

4. **Headphones have low sales volume** — Only 48 units sold. Consider pricing review or bundling with other products.

5. **Monthly trend shows inconsistency** — Some months significantly outperform others. Seasonal campaigns could smooth revenue.

---

## 6. How Technical Requirements Were Met

| Requirement | Implementation |
|-------------|---------------|
| Load data with pandas | `pd.read_csv('data/sales_data.csv')` |
| Handle missing values | `df.isnull().sum()` + `df.fillna(mean)` |
| Calculate 3+ metrics | 5 metrics: revenue, best product, best region, order stats, qty sold |
| Create 2+ chart types | 4 chart types: Bar, Pie, Line, Horizontal Bar |
| Professional formatting | Dark theme, labels, value annotations on all charts |
| Error handling | try/except on file load, validation checks |
| Written insights | Section 5 above with 5 business insights |

---

*Report generated as part of Week 4 project submission.*
