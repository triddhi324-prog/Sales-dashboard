import pandas as pd

df = pd.read_csv("sales_data.csv")
df['Date'] = pd.to_datetime(df['Date'])

# Create new features
df['Month'] = df['Date'].dt.month
df['Year'] = df['Date'].dt.year
df['Profit_Margin'] = df['Profit'] / df['Sales']

# KPI calculations
kpis = {
    "Total Sales": df['Sales'].sum(),
    "Total Profit": df['Profit'].sum(),
    "Avg Profit Margin": df['Profit_Margin'].mean(),
    "Total Orders": df['OrderID'].nunique()
}

print(kpis)

# Customer segmentation
customer_sales = df.groupby('CustomerName')[
    'Sales'].sum().sort_values(ascending=False)

# Category performance
category_analysis = df.groupby('Category').agg({
    'Sales': 'sum',
    'Profit': 'sum',
    'Quantity': 'sum'
})

# Save processed data
df.to_csv("processed_sales_data.csv", index=False)
