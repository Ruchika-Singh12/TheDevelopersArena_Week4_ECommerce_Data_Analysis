# Week 4: Complete Data Analysis Project
## E-Commerce Sales Analysis with Data Visualization

---

## Project Overview and Objectives

This project performs a **complete end-to-end data analysis** on an E-commerce sales dataset. It covers the full data analysis pipeline:

1. **Load** — Read CSV data using Pandas
2. **Clean** — Handle missing values and duplicates
3. **Analyze** — Calculate 5 different business metrics
4. **Visualize** — Create 4 professional charts using Matplotlib
5. **Report** — Generate a structured markdown report with insights

**Dataset:** `sales_data.csv` (100 rows × 7 columns)  
**Topic:** Option 4 — E-commerce Sales Analysis

---

## Setup and Installation Instructions

### Step 1: Install Python
Download from [python.org](https://python.org) and install.

### Step 2: Install Required Libraries
```bash
pip install -r requirements.txt
```

### Step 3: Project Folder Structure
```
week4_project/
├── main.py                  ← Main analysis script
├── README.md                ← This file
├── requirements.txt         ← Library dependencies
├── data/
│   └── sales_data.csv       ← Dataset
├── visualizations/
│   ├── chart1_bar_product_sales.png
│   ├── chart2_pie_region_sales.png
│   ├── chart3_line_monthly_trend.png
│   └── chart4_hbar_units_sold.png
└── report/
    └── analysis_report.md   ← Detailed findings report
```

### Step 4: Run the Project
```bash
python main.py
```

That's it! All 4 charts will be saved in the `visualizations/` folder.

---

## Code Structure Explanation

| Section | Code | What it Does |
|---------|------|-------------|
| Step 1 | `pd.read_csv()` | Loads CSV dataset into DataFrame |
| Step 2 | `.shape`, `.dtypes`, `.head()` | Explores structure of data |
| Step 3 | `.isnull()`, `.fillna()`, `.drop_duplicates()` | Cleans dirty/missing data |
| Step 4 | `.groupby()`, `.sum()`, `.mean()` | Calculates 5 sales metrics |
| Step 5 | `plt.bar()`, `plt.pie()`, `plt.plot()` | Creates 4 chart types |
| Step 6 | `print()` formatted output | Prints final summary report |

---

## Technical Requirements Met

| Requirement | Status | How |
|-------------|--------|-----|
| Complete pipeline (load, clean, analyze, visualize) | ✅ | All 6 steps in `main.py` |
| At least 2 different chart types | ✅ | 4 charts: Bar, Pie, Line, Horizontal Bar |
| Meaningful insights written | ✅ | See `report/analysis_report.md` |
| Professional formatting | ✅ | Dark-themed charts with labels |
| Error handling and validation | ✅ | try/except for file load, missing value check |

---

## Key Insights

- **Laptop** is the top-revenue product (31.5% of total sales)
- **North region** leads with ₹39.8 Lakh in revenue
- Sales show **peaks in January and July**
- Average transaction value is **₹1,23,650**

---

## Screenshots
<img width="1334" height="732" alt="chart1_bar_product_sales" src="https://github.com/user-attachments/assets/f851811c-0c4d-40c1-8fed-a3b0bfa418a4" />
<img width="982" height="1034" alt="chart2_pie_region_sales" src="https://github.com/user-attachments/assets/d6da455f-a734-4cbe-8706-ed4b8ddcde43" />
<img width="1634" height="731" alt="chart3_line_monthly_trend" src="https://github.com/user-attachments/assets/9f9771bb-bcd6-4d8c-9479-8b16bcec1ed6" />
<img width="1333" height="732" alt="chart4_hbar_units_sold" src="https://github.com/user-attachments/assets/b0ca5d2f-7eeb-4728-a1d1-03342108f50d" />

---

*Project by: Ruchika Singh
