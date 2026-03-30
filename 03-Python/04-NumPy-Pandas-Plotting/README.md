# Python Data Analysis Topics - Fourth Day

This section contains Python programming materials covering NumPy arrays, Pandas DataFrames, Matplotlib visualizations, and small automation patterns for data workflows.

## Topics Covered

### 1. NumPy Fundamentals
Numerical computing with arrays:
- **Arrays**: Creating 1D and 2D arrays from lists and ranges
- **Vectorized math**: Element-wise operations and broadcasting
- **Aggregations**: sum, mean, min, max, std along axes
- **Indexing and reshaping**: Rows, columns, and reshape
- **Performance**: Comparing pure Python lists with NumPy for large data

### 2. Pandas for Data Analysis
Tabular data with DataFrames:
- **Loading data**: Reading CSV files from the `Data/` folder
- **Inspection**: `head`, `info`, `describe`
- **Selection and filtering**: Columns, conditions, sorting
- **Missing values**: `fillna`, `dropna`
- **Group by**: Aggregations by product or category
- **Derived columns**: Totals and features from existing fields
- **Merging**: Joining sales with products
- **Strings and dates**: `str` accessors and `datetime` parts

### 3. Plotting with Matplotlib
Charts and customization:
- **Plot types**: Line, scatter, bar, histogram
- **Figure and axes**: `subplots` and multiple panels
- **Labels and style**: Titles, axes, colors, line styles
- **Annotations**: Text and arrows on plots

### 4. Programming Exercises and Extras
Practical coding tasks and notebooks:
- **NumPy task**: Arrays, stats, timing vs lists
- **Pandas task**: End-to-end sales analysis on CSV data
- **Plot task**: Matplotlib examples from simple to styled plots
- **Automation sample**: JSON-style records to DataFrame and append to CSV
- **Notebooks** (optional): `Automation.ipynb`, `Regex Metacharacters.ipynb`, `Scarping.ipynb`

## Files in This Folder

- `README.md` - This documentation file
- `numpy_pandas_plotting_guide.py` - Guide for NumPy, Pandas, and Matplotlib (same style as earlier days)
- `numpy_task.py` - Exercise: NumPy arrays, operations, and performance
- `pandas_task.py` - Exercise: Pandas analysis using files in `Data/`
- `plot_task.py` - Exercise: Matplotlib plots and customization
- `Automation.py` - Example: sample data to DataFrame and CSV append
- `Automation.ipynb`, `Regex Metacharacters.ipynb`, `Scarping.ipynb` - Supplementary notebooks

### Data Files (`Data/` folder)

- `customers.csv`, `employees.csv`, `products.csv`
- `sales.csv`, `orders.csv`
- `missing_data.csv`
- `merge_left.csv`, `merge_right.csv`
- `api_example.csv`

## Learning Objectives

After completing this section, you should be able to:

- Create and operate on NumPy arrays for numerical work
- Load, clean, filter, group, and merge tabular data with Pandas
- Build line, scatter, bar, and histogram plots with Matplotlib
- Follow a small automation pattern from records to CSV
- Connect CSV data to analysis and plots in a repeatable way

## Author

Karam Yaseen
