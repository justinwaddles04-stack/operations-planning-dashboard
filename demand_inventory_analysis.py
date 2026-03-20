import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# Load dataset
df = pd.read_csv('..\\data\\monthly_demand.csv')

# Convert Month to datetime
df['Month'] = pd.to_datetime(df['Month'])

# Preview data
print(df.head())
# Calculate average demand per product
avg_demand = df.groupby('Product')['Demand'].mean().reset_index()

# Get lead time per product
lead_time = df.groupby('Product')['Lead_Time_Days'].mean().reset_index()

# Merge data
inventory_df = pd.merge(avg_demand, lead_time, on='Product')

# Safety stock (simple version)
inventory_df['Safety_Stock'] = inventory_df['Demand'] * 0.2

# Reorder point = (avg demand * lead time) + safety stock
inventory_df['Reorder_Point'] = (inventory_df['Demand'] * inventory_df['Lead_Time_Days']) + inventory_df['Safety_Stock']

print("\nInventory Planning Summary:")
print(inventory_df)
# Add current inventory by product
current_inventory = df.groupby('Product')['Current_Inventory'].first().reset_index()
inventory_df = pd.merge(inventory_df, current_inventory, on='Product')

# Inventory status flag
inventory_df['Inventory_Status'] = np.where(
    inventory_df['Current_Inventory'] <= inventory_df['Reorder_Point'],
    'Reorder Needed',
    'Sufficient Inventory'
)

print("\nInventory Status Check:")
print(inventory_df[['Product', 'Current_Inventory', 'Reorder_Point', 'Inventory_Status']])
# Plot demand trends
for product in df['Product'].unique():
    product_data = df[df['Product'] == product]
    plt.plot(product_data['Month'], product_data['Demand'], label=product)

plt.title('Monthly Demand Trends by Product')
plt.xlabel('Month')
plt.ylabel('Demand')
plt.legend()
plt.xticks(rotation=45)

plt.tight_layout()
plt.savefig('../output/demand_trends.png')
plt.show()
# Save inventory summary to CSV
inventory_df.to_csv('../output/inventory_summary.csv', index=False)

print("\nFiles created:")
print("- demand_trends.png")
print("- inventory_summary.csv")