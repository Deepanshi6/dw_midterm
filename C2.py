import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from tables import sales

# Clean region
sales['region'] = sales['region'].str.strip().str.title()

# Fill missing units
sales['units'] = sales['units'].fillna(sales['units'].median())

# Add revenue
sales['revenue'] = sales['units'] * sales['price']

# Convert date and add month
sales['order_date'] = pd.to_datetime(sales['order_date'])
sales['month_name'] = sales['order_date'].dt.month_name()

# Total revenue per region
region_revenue = sales.groupby('region')['revenue'].sum().sort_values(ascending=False)
print(region_revenue)

'''
output:
region
South    2300.0
East     1480.0
North     300.0
Name: revenue, dtype: float64
'''

# Create pivot table
pivot = pd.pivot_table(
    sales,
    index='region',
    columns='product',
    values='revenue',
    aggfunc='sum',
    fill_value=0
)
print(pivot)

# Plot revenue by region
sns.barplot(x=region_revenue.index, y=region_revenue.values)
plt.xlabel('Region')
plt.ylabel('Total Revenue')
plt.title('Revenue by Region')
plt.show()