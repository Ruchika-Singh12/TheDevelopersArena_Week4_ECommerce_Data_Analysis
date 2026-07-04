# ================================================================
# Week 4 Project: Complete Data Analysis Project
# Topic: Data Visualization & Your First Complete Project
# Dataset: E-commerce Sales Analysis (Option 4)
# ================================================================

import pandas as pd
import matplotlib
matplotlib.use('Agg')   # non-interactive backend (no display needed)
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import os

# ----------------------------------------------------------------
# CONFIGURATION
# ----------------------------------------------------------------
DATA_PATH = 'sales_data (1).csv'
VIZ_FOLDER  = 'visualizations'
os.makedirs(VIZ_FOLDER, exist_ok=True)

print("=" * 62)
print("   WEEK 4 — E-COMMERCE COMPLETE DATA ANALYSIS PROJECT")
print("=" * 62)

# ================================================================
# STEP 1 : LOAD DATA
# ================================================================
print("\n📂 STEP 1: Loading Dataset...")
try:
    df = pd.read_csv(DATA_PATH)
    print(f"   ✅ Data loaded  →  {df.shape[0]} rows × {df.shape[1]} columns")
except FileNotFoundError:
    print(f"   ❌ File not found: {DATA_PATH}")
    raise

# ================================================================
# STEP 2 : EXPLORE DATA
# ================================================================
print("\n🔍 STEP 2: Exploring Dataset")
print("-" * 45)
print(f"  Shape      : {df.shape}")
print(f"  Columns    : {list(df.columns)}")
print("\n  Data Types:\n", df.dtypes.to_string())
print("\n  First 5 Rows:")
print(df.head().to_string(index=False))

# ================================================================
# STEP 3 : CLEAN DATA
# ================================================================
print("\n🧹 STEP 3: Data Cleaning")
print("-" * 45)
missing = df.isnull().sum()
print("  Missing Values:\n", missing.to_string())

if missing.sum() == 0:
    print("\n  ✅ No missing values — data is perfectly clean!")
else:
    numeric_cols = df.select_dtypes(include='number').columns
    df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())
    df.dropna(inplace=True)
    print(f"\n  ✅ Cleaned: filled numeric NaNs with mean, dropped remaining.")

# Remove duplicates
before = len(df)
df.drop_duplicates(inplace=True)
print(f"  Duplicates removed : {before - len(df)}")

# ================================================================
# STEP 4 : ANALYSIS — 5 METRICS
# ================================================================
print("\n📊 STEP 4: Sales Analysis")
print("=" * 62)

# Metric 1 — Total Revenue
total_rev = df['Total_Sales'].sum()
print(f"\n  💰 Metric 1 — Total Revenue        : ₹{total_rev:>14,.2f}")

# Metric 2 — Best Product by Revenue
product_rev = df.groupby('Product')['Total_Sales'].sum().sort_values(ascending=False)
best_product = product_rev.idxmax()
print(f"\n  🏆 Metric 2 — Best Product (Revenue): {best_product}")
print("     All Products:")
for p, v in product_rev.items():
    marker = " ← BEST" if p == best_product else ""
    print(f"       {p:<15} ₹{v:>12,.2f}{marker}")

# Metric 3 — Best Region
region_rev = df.groupby('Region')['Total_Sales'].sum().sort_values(ascending=False)
best_region = region_rev.idxmax()
print(f"\n  🌍 Metric 3 — Best Region           : {best_region}")
print("     All Regions:")
for r, v in region_rev.items():
    marker = " ← TOP" if r == best_region else ""
    print(f"       {r:<10} ₹{v:>12,.2f}{marker}")

# Metric 4 — Order Stats
avg_order = df['Total_Sales'].mean()
max_sale  = df['Total_Sales'].max()
min_sale  = df['Total_Sales'].min()
print(f"\n  📈 Metric 4 — Order Statistics:")
print(f"       Average : ₹{avg_order:>12,.2f}")
print(f"       Maximum : ₹{max_sale:>12,.2f}")
print(f"       Minimum : ₹{min_sale:>12,.2f}")

# Metric 5 — Quantity Sold
product_qty = df.groupby('Product')['Quantity'].sum().sort_values(ascending=False)
print(f"\n  📦 Metric 5 — Units Sold by Product:")
for p, q in product_qty.items():
    print(f"       {p:<15} {q:>3} units")

# Monthly Revenue
df['Date']  = pd.to_datetime(df['Date'], errors='coerce')
df['Month'] = df['Date'].dt.strftime('%b')
month_order = ['Jan','Feb','Mar','Apr','May','Jun',
               'Jul','Aug','Sep','Oct','Nov','Dec']
monthly_rev = (df.groupby('Month')['Total_Sales']
               .sum()
               .reindex([m for m in month_order if m in df['Month'].unique()]))

# ================================================================
# STEP 5 : VISUALIZATIONS
# ================================================================
print("\n🎨 STEP 5: Creating Visualizations...")

COLORS_BAR  = ['#2196F3','#4CAF50','#FF9800','#E91E63','#9C27B0']
COLORS_PIE  = ['#42A5F5','#66BB6A','#FFA726','#EC407A','#AB47BC']
BG          = '#0D1117'
FG          = 'white'

def style_ax(ax, title, xlabel='', ylabel=''):
    ax.set_facecolor('#161B22')
    ax.set_title(title, color=FG, fontsize=13, fontweight='bold', pad=12)
    ax.set_xlabel(xlabel, color=FG, fontsize=10)
    ax.set_ylabel(ylabel, color=FG, fontsize=10)
    ax.tick_params(colors=FG)
    for spine in ax.spines.values():
        spine.set_edgecolor('#30363D')

# ── CHART 1 : Bar Chart — Sales by Product ──────────────────────
fig, ax = plt.subplots(figsize=(9, 5))
fig.patch.set_facecolor(BG)
bars = ax.bar(product_rev.index, product_rev.values / 1e6,
              color=COLORS_BAR, width=0.55, zorder=3)
ax.yaxis.set_major_formatter(mticker.FormatStrFormatter('₹%.2f M'))
ax.grid(axis='y', color='#30363D', linestyle='--', alpha=0.6, zorder=0)
for bar, val in zip(bars, product_rev.values):
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.01,
            f'₹{val/1e6:.2f}M', ha='center', va='bottom',
            color=FG, fontsize=9, fontweight='bold')
style_ax(ax, '📊 Sales Revenue by Product Category',
         'Product', 'Revenue (Millions ₹)')
plt.tight_layout()
chart1_path = f'{VIZ_FOLDER}/chart1_bar_product_sales.png'
plt.savefig(chart1_path, dpi=150, bbox_inches='tight', facecolor=BG)
plt.close()
print(f"   ✅ Chart 1 saved → {chart1_path}")

# ── CHART 2 : Pie Chart — Region-wise Revenue ───────────────────
fig, ax = plt.subplots(figsize=(8, 7))
fig.patch.set_facecolor(BG)
wedges, texts, autotexts = ax.pie(
    region_rev.values,
    labels=region_rev.index,
    autopct='%1.1f%%',
    colors=COLORS_PIE,
    startangle=140,
    pctdistance=0.78,
    wedgeprops={'linewidth': 1.5, 'edgecolor': BG}
)
for t in texts:
    t.set_color(FG); t.set_fontsize(11)
for a in autotexts:
    a.set_color(BG); a.set_fontsize(9); a.set_fontweight('bold')
ax.set_title('🥧 Region-wise Revenue Distribution',
             color=FG, fontsize=13, fontweight='bold', pad=15)
ax.set_facecolor(BG)
plt.tight_layout()
chart2_path = f'{VIZ_FOLDER}/chart2_pie_region_sales.png'
plt.savefig(chart2_path, dpi=150, bbox_inches='tight', facecolor=BG)
plt.close()
print(f"   ✅ Chart 2 saved → {chart2_path}")

# ── CHART 3 : Line Chart — Monthly Revenue Trend ────────────────
fig, ax = plt.subplots(figsize=(11, 5))
fig.patch.set_facecolor(BG)
ax.plot(monthly_rev.index, monthly_rev.values / 1e6,
        color='#2196F3', linewidth=2.5, marker='o',
        markersize=7, markerfacecolor='#FF9800',
        markeredgecolor=FG, markeredgewidth=1.2, zorder=3)
ax.fill_between(range(len(monthly_rev)), monthly_rev.values / 1e6,
                alpha=0.15, color='#2196F3')
ax.set_xticks(range(len(monthly_rev)))
ax.set_xticklabels(monthly_rev.index, rotation=30, ha='right')
ax.yaxis.set_major_formatter(mticker.FormatStrFormatter('₹%.2f M'))
ax.grid(color='#30363D', linestyle='--', alpha=0.5, zorder=0)
for i, (m, v) in enumerate(zip(monthly_rev.index, monthly_rev.values)):
    ax.annotate(f'₹{v/1e6:.2f}M', (i, v/1e6),
                textcoords='offset points', xytext=(0, 10),
                ha='center', color=FG, fontsize=7.5)
style_ax(ax, '📈 Monthly Revenue Trend (2024)',
         'Month', 'Revenue (Millions ₹)')
plt.tight_layout()
chart3_path = f'{VIZ_FOLDER}/chart3_line_monthly_trend.png'
plt.savefig(chart3_path, dpi=150, bbox_inches='tight', facecolor=BG)
plt.close()
print(f"   ✅ Chart 3 saved → {chart3_path}")

# ── CHART 4 : Horizontal Bar — Units Sold ───────────────────────
fig, ax = plt.subplots(figsize=(9, 5))
fig.patch.set_facecolor(BG)
bars = ax.barh(product_qty.index[::-1], product_qty.values[::-1],
               color=COLORS_BAR[::-1], height=0.55, zorder=3)
ax.grid(axis='x', color='#30363D', linestyle='--', alpha=0.6, zorder=0)
for bar, val in zip(bars, product_qty.values[::-1]):
    ax.text(bar.get_width() + 1, bar.get_y() + bar.get_height()/2,
            f'{val} units', va='center', color=FG, fontsize=9, fontweight='bold')
style_ax(ax, '📦 Units Sold by Product', 'Units Sold', 'Product')
plt.tight_layout()
chart4_path = f'{VIZ_FOLDER}/chart4_hbar_units_sold.png'
plt.savefig(chart4_path, dpi=150, bbox_inches='tight', facecolor=BG)
plt.close()
print(f"   ✅ Chart 4 saved → {chart4_path}")

# ================================================================
# STEP 6 : FINAL REPORT SUMMARY
# ================================================================
print("\n" + "=" * 62)
print("             📝 FINAL ANALYSIS REPORT SUMMARY")
print("=" * 62)
print(f"  Total Transactions  : {len(df)}")
print(f"  Total Revenue       : ₹{total_rev:,.2f}")
print(f"  Best-Selling Product: {best_product}  (₹{product_rev[best_product]:,.2f})")
print(f"  Top Region          : {best_region}  (₹{region_rev[best_region]:,.2f})")
print(f"  Avg Order Value     : ₹{avg_order:,.2f}")
print(f"  Highest Single Sale : ₹{max_sale:,.2f}")
print(f"  Lowest Single Sale  : ₹{min_sale:,.2f}")
print(f"  Charts Generated    : 4 (Bar, Pie, Line, Horizontal Bar)")
print("=" * 62)
print("\n✅ All steps completed successfully!")
print("   Visualizations saved in →", VIZ_FOLDER)
