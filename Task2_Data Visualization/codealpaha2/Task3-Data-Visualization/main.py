import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv("data/superstore.csv")

print("===== BEFORE CLEANING =====")
print("Rows and columns:", df.shape)

# Remove duplicate rows
df = df.drop_duplicates()

# Convert Order Date to date format
df["Order Date"] = pd.to_datetime(df["Order Date"])

# Convert Ship Date to date format
df["Ship Date"] = pd.to_datetime(df["Ship Date"])

# Make sure numerical columns are numeric
numeric_columns = ["Sales", "Quantity", "Discount", "Profit"]

for column in numeric_columns:
    df[column] = pd.to_numeric(df[column], errors="coerce")

# Check missing values
print("\n===== MISSING VALUES =====")
print(df.isnull().sum())

# Check data types
print("\n===== DATA TYPES =====")
print(df.dtypes)

print("\n===== AFTER CLEANING =====")
print("Rows and columns:", df.shape)

# Show first 5 rows
print("\n===== FIRST 5 ROWS =====")
print(df.head())
print("\n===== SALES STATISTICS =====")

print("Total Sales:", df["Sales"].sum())
print("Total Profit:", df["Profit"].sum())
print("Total Quantity:", df["Quantity"].sum())

print("\nAverage Sales:", df["Sales"].mean())
print("Average Profit:", df["Profit"].mean())

print("\n===== CATEGORY SALES =====")
print(df.groupby("Category")["Sales"].sum().sort_values(ascending=False))

print("\n===== REGION SALES =====")
print(df.groupby("Region")["Sales"].sum().sort_values(ascending=False))
# ===============================
# VISUALIZATION 1: SALES BY CATEGORY
# ===============================

category_sales = df.groupby("Category")["Sales"].sum().sort_values(ascending=False)

plt.figure(figsize=(8, 5))

category_sales.plot(kind="bar")

plt.title("Total Sales by Category")
plt.xlabel("Category")
plt.ylabel("Total Sales")

plt.xticks(rotation=0)
plt.tight_layout()

plt.savefig("images/sales_by_category.png")

plt.show()
# ===============================
# VISUALIZATION 2: SALES BY REGION
# ===============================

region_sales = df.groupby("Region")["Sales"].sum().sort_values(ascending=False)

plt.figure(figsize=(8, 5))

region_sales.plot(kind="bar")

plt.title("Total Sales by Region")
plt.xlabel("Region")
plt.ylabel("Total Sales")

plt.xticks(rotation=0)
plt.tight_layout()

plt.savefig("images/sales_by_region.png")

plt.show()
# ===============================
# VISUALIZATION 3: MONTHLY SALES TREND
# ===============================

df["Month"] = df["Order Date"].dt.to_period("M")

monthly_sales = df.groupby("Month")["Sales"].sum()

plt.figure(figsize=(12, 5))

monthly_sales.plot(kind="line", marker="o")

plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Total Sales")

plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig("images/monthly_sales.png")

plt.show()
# ===============================
# VISUALIZATION 4: PROFIT BY CATEGORY
# ===============================

category_profit = df.groupby("Category")["Profit"].sum().sort_values(ascending=False)

plt.figure(figsize=(8, 5))

category_profit.plot(kind="bar")

plt.title("Total Profit by Category")
plt.xlabel("Category")
plt.ylabel("Total Profit")

plt.xticks(rotation=0)
plt.tight_layout()

plt.savefig("images/profit_by_category.png")

plt.show()
# ===============================
# VISUALIZATION 5: SALES VS PROFIT
# ===============================

plt.figure(figsize=(8, 6))

sns.scatterplot(
    data=df,
    x="Sales",
    y="Profit",
    hue="Category"
)

plt.title("Sales vs Profit")
plt.xlabel("Sales")
plt.ylabel("Profit")

plt.tight_layout()

plt.savefig("images/sales_vs_profit.png")

plt.show()
# ===============================
# VISUALIZATION 6: REGION VS CATEGORY
# ===============================

pivot = pd.pivot_table(
    df,
    values="Sales",
    index="Region",
    columns="Category",
    aggfunc="sum"
)

plt.figure(figsize=(8, 5))

sns.heatmap(
    pivot,
    annot=True,
    fmt=".0f"
)

plt.title("Sales by Region and Category")
plt.xlabel("Category")
plt.ylabel("Region")

plt.tight_layout()

plt.savefig("images/region_category_heatmap.png")

plt.show()