import pandas as pd
import json
import os


# Check if we're in the right place
print("Current directory:", os.getcwd()) # Prints the current working directory to help verify that the script is being run from the correct location.

# Check if our data file exists
data_path = "data/sales.csv" # Define the path to the sales data file that we want to check for existence.

# data_path1 = "../data/dhaka_weather.csv" # Define the path to the Dhaka weather data file from the parent directory to check for existence.
# print(f" Found {data_path1}")

if os.path.exists(data_path): # Check if the sales data file exists at the specified path.
    print(f" Found {data_path}")
else:
    print(f" Cannot find. Make sure you're running from the sales-analysis folder! {data_path}")
   

#______________________________________________________________#
# Read the CSV file
df = pd.read_csv('data/sales.csv')
print("CSV Data:")
print(df)
print(f"\nShape: {df.shape[0]} rows, {df.shape[1]} columns")

# Quick operation: calculate total for each row
df['total'] = df['quantity'] * df['price']
print("\nWith totals:")
print(df)

# Group by product and calculate totals
product_totals = (
    df.groupby('product', as_index=False)
      .agg(
          total_quantity=('quantity', 'sum'),
          total_cost=('total', 'sum')
      )
)

print(product_totals)

# Create output directory
os.makedirs('output', exist_ok=True)

# Save as different formats
# 1. JSON format (good for web APIs)
product_totals.to_json('output/sales_data.json', orient='records', indent=2)

# 2. Excel format (good for sharing)
product_totals.to_excel('output/sales_data.xlsx', index=False)

# 3. Updated CSV (with our new total column)
product_totals.to_csv('output/sales_with_totals.csv', index=False)

print("\nFiles saved:") # Print a message indicating that the files have been saved successfully.
print("- output/sales_data.json")
print("- output/sales_data.xlsx") 
print("- output/sales_with_totals.csv")


# analyzer.py
import pandas as pd
from helper import calculate_total, format_currency

# Read data
df = pd.read_csv('data/sales.csv')

# Calculate total for each row
totals = []
for index, row in df.iterrows():
    total = calculate_total(row['quantity'], row['price'])
    totals.append(total)

# Add totals to our data
df['total'] = totals

# Display with formatted totals
print("Sales Data:")
for index, row in df.iterrows():
    formatted_total = format_currency(row['total'])
    print(f"{row['product']}: {formatted_total}")

# Show grand total
grand_total = df['total'].sum()
formatted_grand_total = format_currency(grand_total)
print(f"\nGrand Total: {formatted_grand_total}")
