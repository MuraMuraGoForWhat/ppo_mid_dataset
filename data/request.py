import pandas as pd

# Read the CSV file
df = pd.read_csv('bay_vio_data_03_19.csv')

# Extract the required columns and modify them
df['street_marker'] = df['street_marker'].str.extract('(\d+)').astype(int)
df['aim_marker'] = df['aim_marker'].str.extract('(\d+)').astype(int)
df = df[['street_marker', 'RequestTime', 'aim_marker']]

# Save the modified DataFrame to a new CSV file
df.to_csv('output.csv', index=False)
