import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import logging
import numpy as np


def holiday(train_df):
  # Sales Behavior During Holidays

  # Convert Date column to datetime
  train_df['Date'] = pd.to_datetime(train_df['Date'])

  # Extract year, month, and day of week from Date
  train_df['Year'] = train_df['Date'].dt.year
  train_df['Month'] = train_df['Date'].dt.month
  train_df['DayOfWeek'] = train_df['Date'].dt.dayofweek

  # Define holidays
  holidays = ['2013-12-25', '2014-12-25', '2015-12-25',  # Christmas
              '2013-04-01', '2014-04-21', '2015-04-06']  # Easter

  # Convert holidays to datetime
  holidays = pd.to_datetime(holidays)

  # Create a column to indicate if a date is a holiday
  train_df['IsHoliday'] = train_df['Date'].isin(holidays)

  # Create a column to indicate the period relative to holidays
  train_df['HolidayPeriod'] = np.where(train_df['IsHoliday'], 'During Holiday',
                                      np.where(train_df['Date'].isin(holidays - pd.Timedelta(days=1)), 'Before Holiday',
                                                np.where(train_df['Date'].isin(holidays + pd.Timedelta(days=1)), 'After Holiday', 'Non-Holiday')))

  # Log the creation of holiday-related columns
  logging.info('Holiday-related columns created successfully')

  # Group by HolidayPeriod and calculate mean sales
  holiday_sales = train_df.groupby('HolidayPeriod')['Sales'].mean().reset_index()

  # Plot sales behavior during holidays
  plt.figure(figsize=(12, 6))
  sns.barplot(x='HolidayPeriod', y='Sales', data=holiday_sales, palette='viridis')
  plt.title('Sales Behavior Before, During, and After Holidays')
  plt.xlabel('Holiday Period')
  plt.ylabel('Average Sales')
  plt.show()

  # Log the sales behavior during holidays
  logging.info(f'Sales behavior during holidays:\n{holiday_sales}')