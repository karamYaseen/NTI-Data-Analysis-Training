# NumPy, Pandas & Matplotlib in Python - Fourth Day
# This guide covers numerical arrays, DataFrames, and plotting (same structure as earlier day guides)

# ===========================================
# SECTION 1: NUMPY FUNDAMENTALS
# ===========================================

"""
1. NUMPY ARRAYS
NumPy provides the ndarray type: a fast, flexible container for
numerical data.

Why use NumPy instead of Python lists?
- Memory-efficient: stores data in contiguous blocks
- Vectorized operations: work on entire arrays at once
- Rich set of mathematical functions
"""

# ===== ARRAY CREATION =====
"""
COMMON WAYS TO CREATE ARRAYS

1) From a Python list:
   import numpy as np
   arr = np.array([1, 2, 3, 4, 5])

2) Using ranges:
   np.arange(1, 10)        # [1 2 3 4 5 6 7 8 9]

3) Multidimensional arrays:
   arr2 = np.arange(1, 10).reshape(3, 3)

Key ideas:
- shape: dimensions of the array
  arr2.shape  -> (3, 3)
- dtype: data type of elements
  arr2.dtype  -> int64 / float64 / ...
"""

# ===== BASIC OPERATIONS =====
"""
ARRAY ARITHMETIC (VECTORIZATION)

Given:
   arr = np.array([1, 2, 3, 4, 5])

You can perform operations on the entire array:
   arr + 5        -> [ 6  7  8  9 10]
   arr * 2        -> [ 2  4  6  8 10]

Array with array:
   a = np.array([1, 2, 3, 4, 5])
   b = np.array([10, 20, 30, 40, 50])
   a + b          -> [11 22 33 44 55]
   (a + b) / 2    -> [ 5.5 11.  16.5 22.  27.5]

NumPy automatically applies operations element‑wise.
This is what we mean by vectorized operations.
"""

# ===== AGGREGATIONS & AXES =====
"""
AGGREGATION FUNCTIONS

For a 2D array:
   arr2 = np.arange(1, 10).reshape(3, 3)

Global statistics:
   arr2.sum()
   arr2.mean()
   arr2.min()
   arr2.max()
   arr2.std()

Axis argument:
- axis=0  -> column-wise
- axis=1  -> row-wise

Examples:
   arr2.sum(axis=1)   # sum along rows
   arr2.sum(axis=0)   # sum along columns
"""

# ===== INDEXING, SLICING, RESHAPING =====
"""
INDEXING AND SLICING

Given arr2 as 3x3:
   arr2[1]        -> second row
   arr2[:, 2]     -> third column

RESHAPING
   arr2.reshape(1, 9)   # 1 row, 9 columns
   arr2.reshape(9, 1)   # 9 rows, 1 column

Reshape changes the view of the same underlying data
when the total number of elements stays the same.
"""

# ===== PERFORMANCE IDEA =====
"""
PERFORMANCE: LISTS VS NUMPY

In the NumPy task file you compare:
1) Pure Python:
   list1 = list(range(1_000_000))
   list2 = [x**2 for x in list1]

2) NumPy:
   arr = np.arange(1_000_000)
   arr2 = arr ** 2

NumPy uses optimized C loops internally, which usually makes
the second approach faster and more memory efficient.
"""

# ===========================================
# SECTION 2: PANDAS DATA ANALYSIS
# ===========================================

"""
2. PANDAS DATAFRAMES

Pandas provides the DataFrame type:
- Rows: records/observations
- Columns: fields/features

In this module, Pandas is used to analyze sales data from CSV
files stored in the Data/ folder.
"""

# ===== READING CSV FILES =====
"""
READING CSV DATA

Common pattern:
   import pandas as pd
   from pathlib import Path

   base_dir = Path(__file__).resolve().parent
   data_dir = base_dir / "Data"

   sales_path = data_dir / "sales.csv"
   df_sales = pd.read_csv(sales_path)

This approach uses relative paths (based on the script file),
so the code works on any machine without hard‑coded user paths.
"""

# ===== QUICK DATA INSPECTION =====
"""
INSPECTING THE DATAFRAME

Key methods:
   df_sales.head()    # first 5 rows
   df_sales.info()    # columns, dtypes, non‑null counts
   df_sales.describe()# numeric summary (mean, std, min, quartiles, max)

These three give you a fast understanding of the dataset:
- number of rows and columns
- data types
- presence of missing values
- approximate value ranges
"""

# ===== SELECTING & FILTERING =====
"""
SELECTING COLUMNS
   product_price = df_sales[["Product", "Price"]]

FILTERING ROWS
   high_quantity = df_sales[df_sales["Quantity"] > 10]

SORTING
   sorted_sales = df_sales.sort_values(by="Price", ascending=False)

These operations let you extract exactly the rows and columns
you need for your analysis.
"""

# ===== HANDLING MISSING DATA =====
"""
MISSING VALUES

Real‑world data often contains missing values (NaN).
Common strategies:

1) Fill missing numeric values:
   df_sales["Quantity"] = df_sales["Quantity"].fillna(0)

2) Drop rows with missing critical values:
   df_sales.dropna(subset=["Price"], inplace=True)

Which strategy to choose depends on your business problem.
"""

# ===== GROUPING & AGGREGATION =====
"""
GROUP BY AND AGGREGATION

To summarize by product:
   grouped_sales = df_sales.groupby("Product")["Quantity"].agg(["sum", "mean"])

This answers questions like:
- How many units of each product were sold?
- On average, how many units are sold per order for each product?
"""

# ===== DERIVED COLUMNS =====
"""
DERIVED (CALCULATED) COLUMNS

Example: total sale value per row
   df_sales["Total"] = df_sales["Price"] * df_sales["Quantity"]

Then you can filter:
   filtered_sales = (
       df_sales[df_sales["Total"] > 500]
       .sort_values(by="Total", ascending=False)
   )

This is a simple example of feature engineering:
turning existing columns into new, more informative ones.
"""

# ===== MERGING DATASETS =====
"""
MERGING DATAFRAMES

You also load a products table:
   df_products = pd.read_csv(products_path)

Then merge:
   merged_df = pd.merge(
       df_sales,
       df_products,
       left_on="Product",
       right_on="Product_Name",
       how="left",
   )

Now each sales row knows:
- product category
- any other product attributes
"""

# ===== STRING & DATETIME FEATURES =====
"""
STRING OPERATIONS
   merged_df["Category"] = merged_df["Category"].str.upper()
   merged_df["Category_initial"] = merged_df["Category"].str[0]

DATE / TIME OPERATIONS
   merged_df["Sale_Date"] = pd.to_datetime(merged_df["Sale_Date"])
   merged_df["Month"] = merged_df["Sale_Date"].dt.month

These are typical steps when preparing data for reports or
visualizations by category and by time.
"""

# ===========================================
# SECTION 3: MATPLOTLIB PLOTTING BASICS
# ===========================================

"""
3. MATPLOTLIB VISUALIZATIONS

Matplotlib is the base plotting library used here. The goal
of this day is to understand the basic plot types and how to
customize them.
"""

# ===== CORE PLOT TYPES =====
"""
BASIC PLOTS

Given:
   import matplotlib.pyplot as plt
   x = [1, 2, 3, 4, 5]
   y = [10, 20, 25, 30, 50]

Line plot:
   plt.plot(x, y)
   plt.title("Sample Line Plot")
   plt.xlabel("X-axis")
   plt.ylabel("Y-axis")
   plt.show()

Scatter plot:
   plt.scatter(x, y)

Bar chart:
   groups = ["A", "B", "C", "D"]
   values = [10, 15, 7, 12]
   plt.bar(groups, values)

Histogram:
   data = [1,2,2,3,3,3,4,4,6]
   plt.hist(data)
"""

# ===== FIGURE AND SUBPLOTS =====
"""
FIGURE / AXES PATTERN

More control using subplots:
   fig, ax = plt.subplots()
   ax.plot([1, 2, 3], [4, 5, 6])
   ax.set_xlabel("X-axis")
   ax.set_ylabel("Y-axis")
   ax.set_title("Sample Plot with Subplots")

Multiple subplots side by side:
   fig, (ax1, ax2) = plt.subplots(1, 2)
   ax1.plot([1, 2], [10, 20])
   ax2.scatter([1, 2], [5, 15])
"""

# ===== STYLING, GRID, ANNOTATIONS =====
"""
STYLING AND ANNOTATIONS

Styling:
   plt.plot([1,2,3], [4,5,6], color="red", linestyle="--")

Grid:
   plt.grid(True)

Text and annotations:
   plt.text(2, 5, "Hello")
   plt.annotate(
       "Point",
       xy=(2, 5),
       xytext=(2.5, 6),
       arrowprops=dict(facecolor="black", shrink=0.05),
   )

These tools help you tell a clearer story with your plots.
"""

# ===========================================
# SECTION 4: SUMMARY AND PRACTICE
# ===========================================

"""
SUMMARY

NumPy:
- Use arrays for fast numerical operations
- Prefer vectorization over Python loops

Pandas:
- Use DataFrames for tabular data
- Load from CSV, inspect, clean, group, and merge

Matplotlib:
- Start with line/scatter/bar/hist
- Then learn subplots, styling, and annotations

RECOMMENDED PRACTICE
- Open the task files:
  - numpy_task.py
  - pandas_task.py
  - plot_task.py
- Read the code and run them in this order.
- Try to modify them: new columns, new filters, new plots.
"""
