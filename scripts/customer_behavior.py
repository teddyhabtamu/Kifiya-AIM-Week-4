import matplotlib.pyplot as plt
import seaborn as sns
import logging

def behavior(train_df):
  # Customer Behavior During Store Opening and Closing Times

  # Convert 'Open' column to categorical type for better analysis
  train_df['Open'] = train_df['Open'].astype('category')

  # Group by 'Open' status and calculate mean sales
  open_sales = train_df.groupby('Open')['Sales'].mean().reset_index()

  # Plot the sales behavior during store opening and closing times
  plt.figure(figsize=(10, 6))
  sns.barplot(x='Open', y='Sales', data=open_sales, palette='viridis')
  plt.title('Sales Behavior During Store Opening and Closing Times')
  plt.xlabel('Store Open Status')
  plt.ylabel('Average Sales')
  plt.show()

  # Log the sales behavior during store opening and closing times
  logging.info(f'Sales behavior during store opening and closing times:\n{open_sales}')

  # Analyze customer behavior during store opening and closing times
  open_customers = train_df.groupby('Open')['Customers'].mean().reset_index()

  # Plot the customer behavior during store opening and closing times
  plt.figure(figsize=(10, 6))
  sns.barplot(x='Open', y='Customers', data=open_customers, palette='viridis')
  plt.title('Customer Behavior During Store Opening and Closing Times')
  plt.xlabel('Store Open Status')
  plt.ylabel('Average Number of Customers')
  plt.show()

  # Log the customer behavior during store opening and closing times
  logging.info(f'Customer behavior during store opening and closing times:\n{open_customers}')
