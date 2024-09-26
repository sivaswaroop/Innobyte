
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('/content/Amazon Sale Report.csv')

# Get the first few rows of the dataset
print(df.head())

# Get the column names and data types
print(df.columns)
print(df.dtypes)

# Get the summary statistics of the dataset
print(df.describe())

# Calculate the total sales
total_sales = df['Amount'].sum()
print(f'Total Sales: ${total_sales:,.2f}')

# Calculate the average sales per order
avg_sales_per_order = df['Amount'].mean()
print(f'Average Sales per Order: ${avg_sales_per_order:,.2f}')

# Plot the sales trend over time
plt.figure(figsize=(10, 6))
plt.plot(df['Date'], df['Amount'])
plt.xlabel('Date')
plt.ylabel('Sales')
plt.title('Sales Trend Over Time')
plt.show()

# Get the top 5 product categories by sales
top_categories = df.groupby('Category')['Amount'].sum().sort_values(ascending=False).head(5)
print(top_categories)

# Get the top 5 product sizes by sales
top_sizes = df.groupby('Size')['Amount'].sum().sort_values(ascending=False).head(5)
print(top_sizes)

# Plot the distribution of product quantities sold
plt.figure(figsize=(10, 6))
plt.hist(df['Qty'], bins=50)
plt.xlabel('Quantity')
plt.ylabel('Frequency')
plt.title('Distribution of Product Quantities Sold')
plt.show()

# Get the fulfillment methods used
fulfillment_methods = df['Fulfilment'].unique()
print(fulfillment_methods)

# Calculate the average shipping time for each fulfillment method
avg_shipping_time = df.groupby('Fulfilment')['ship-postal-code'].mean()
print(avg_shipping_time)

# Plot the shipping time distribution for each fulfillment method
plt.figure(figsize=(10, 6))
for method in fulfillment_methods:
    plt.hist(df[df['Fulfilment'] == method]['ship-postal-code'], bins=50, alpha=0.5, label=method)
plt.xlabel('ship-postal-code')
plt.ylabel('Frequency')
plt.title('ship-postal-code Distribution by Fulfillment')
plt.legend()
plt.show()

# Get the top 5 customer locations by sales
top_locations = df.groupby('ship-city')['Amount'].sum().sort_values(ascending=False).head(5)
print(top_locations)

# Plot the customer location distribution
plt.figure(figsize=(10, 6))
plt.bar(top_locations.index, top_locations.values)
plt.xlabel('Customer Location')
plt.ylabel('Sales')
plt.title('Customer Location Distribution')
plt.show()

# Get the top 5 states by sales
top_states = df.groupby('ship-state')['Amount'].sum().sort_values(ascending=False).head(5)
print(top_states)

# Plot the state-wise sales distribution
plt.figure(figsize=(10, 6))
plt.bar(top_states.index, top_states.values)
plt.xlabel('State')
plt.ylabel('Sales')
plt.title('State-wise Sales Distribution')
plt.show()

