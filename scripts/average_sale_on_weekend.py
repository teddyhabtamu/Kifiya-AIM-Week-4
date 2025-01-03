import matplotlib.pyplot as plt
import seaborn as sns
import logging

def weekendSale(train_df):
  # Sales on Weekends for Stores Open on All Weekdays

  # Identify stores that are open on all weekdays
  weekdays_open_stores = train_df[train_df['Open'] == 1]['Store'].unique()

  # Filter the training data for these stores
  weekdays_open_sales = train_df[train_df['Store'].isin(weekdays_open_stores)]

  # Extract day of the week from the Date column
  weekdays_open_sales['DayOfWeek'] = weekdays_open_sales['Date'].dt.dayofweek

  # Filter for weekend sales (Saturday and Sunday)
  weekend_sales = weekdays_open_sales[weekdays_open_sales['DayOfWeek'].isin([5, 6])]

  # Group by store and day of the week to calculate mean sales
  weekend_sales_mean = weekend_sales.groupby(['Store', 'DayOfWeek'])['Sales'].mean().reset_index()

  # Plot the average weekend sales for stores open on all weekdays
  plt.figure(figsize=(12, 6))
  sns.barplot(x='DayOfWeek', y='Sales', data=weekend_sales_mean, palette='viridis')
  plt.title('Average Weekend Sales for Stores Open on All Weekdays')
  plt.xlabel('Day of the Week')
  plt.ylabel('Average Sales')
  plt.xticks(ticks=[0, 1], labels=['Saturday', 'Sunday'])
  plt.show()

  # Log the average weekend sales for stores open on all weekdays
  logging.info(f'Average weekend sales for stores open on all weekdays:\n{weekend_sales_mean}')
  