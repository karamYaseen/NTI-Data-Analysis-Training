import pandas as pd 

df_sales = pd.read_csv('Data\\sales.csv')

print("First 5 rows:")
print(df_sales.head()) 

print("\nBasic info")
print(df_sales.info())

print("\nStatistics:")
print(df_sales.describe())


product_price = df_sales[['Product', 'Price']]
print("\nProduct Price:")
print(product_price)

high_quantity = df_sales[df_sales['Quantity'] > 10]
print("\nHigh Quantity Sales:") 
print(high_quantity)

sorted_sales = df_sales.sort_values(by='Price', ascending=False)
print("\nSales sorted by Price (descending):")
print(sorted_sales)

df_sales['Quantity'] = df_sales['Quantity'].fillna(0)
df_sales = df_sales.dropna(subset=['Price'], inplace=True)
print("\nData after handling missing values:")
print(df_sales)

grouped_sales = df_sales.groupby('Product')['Quantity'].agg(['sum', 'mean'])
print("\nGrouped Sales by Product:")
print(grouped_sales)

df_sales['Total'] = df_sales['Price'] * df_sales['Quantity']
filtered_sales = df_sales[df_sales['Total'] > 500].sort_values(by='Total', ascending=False)
print("\nFiltered and Sorted Sales:")
print(filtered_sales)

# -*-*-*-*-*--*
df_products = pd.read_csv('Data\\products.csv')
print("\nProducts Data:")
print(df_products.head())

merged_df = pd.merge(df_sales, df_products, on='Product', how='left')
print("\nMerged Data:")
print(merged_df.head())


merged_df['Category'] = merged_df['Category'].str.upper()
merged_df['SupplierInitial'] = merged_df['Supplier'].str[0]
print("\nData after string operations:")
print(merged_df.head())

merged_df['Date'] = pd.to_datetime(merged_df['Date'])
merged_df['Month'] = merged_df['Date'].dt.month
print("\nData after date conversion and month extraction:")
print(merged_df.head())

grouped_df = merged_df.groupby(['Category', 'Month'])['Total'].sum()
print("\nGrouped Data:")
print(grouped_df)