import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import logging

def seasonal_behavior(train_df):
  # Seasonal Purchase Behaviors

  # Extract month and year from the Date column
  train_df['Month'] = train_df['Date'].dt.month
  train_df['Year'] = train_df['Date'].dt.year

  # Define Christmas and Easter periods
  christmas_period = train_df[(train_df['Month'] == 12) & (train_df['DayOfWeek'] >= 20)]
  easter_period = train_df[(train_df['Date'].isin(pd.to_datetime(['2013-03-31', '2014-04-20', '2015-04-05'])))]

  # Log the extraction of seasonal periods
  logging.info('Seasonal periods (Christmas and Easter) extracted successfully')

  # Calculate mean sales during Christmas and Easter periods
  christmas_sales = christmas_period.groupby('Year')['Sales'].mean().reset_index()
  easter_sales = easter_period.groupby('Year')['Sales'].mean().reset_index()

  # Plot sales behavior during Christmas
  plt.figure(figsize=(12, 6))
  sns.barplot(x='Year', y='Sales', data=christmas_sales, palette='coolwarm')
  plt.title('Average Sales During Christmas')
  plt.xlabel('Year')
  plt.ylabel('Average Sales')
  plt.show()

  # Log the sales behavior during Christmas
  logging.info(f'Sales behavior during Christmas:\n{christmas_sales}')

  # Plot sales behavior during Easter
  plt.figure(figsize=(12, 6))
  sns.barplot(x='Year', y='Sales', data=easter_sales, palette='coolwarm')
  plt.title('Average Sales During Easter')
  plt.xlabel('Year')
  plt.ylabel('Average Sales')
  plt.show()

  # Log the sales behavior during Easter
  logging.info(f'Sales behavior during Easter:\n{easter_sales}')