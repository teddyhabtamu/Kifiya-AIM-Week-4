import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import logging

def distanceEffect(train_df, store_df):
  # Effect of Distance to Competitors on Sales

  # Merge train_df with store_df to include competitor distance information
  train_store_df = pd.merge(train_df, store_df, on='Store')

  # Log the merging of dataframes
  logging.info('Merged train_df with store_df to include competitor distance information')

  # Handle missing values in the 'CompetitionDistance' column
  train_store_df['CompetitionDistance'].fillna(train_store_df['CompetitionDistance'].median(), inplace=True)

  # Log the handling of missing values in 'CompetitionDistance'
  logging.info('Handled missing values in CompetitionDistance column')

  # Group by CompetitionDistance and calculate mean sales
  competition_distance_sales = train_store_df.groupby('CompetitionDistance')['Sales'].mean().reset_index()

  # Plot the effect of distance to competitors on sales
  plt.figure(figsize=(12, 6))
  sns.lineplot(x='CompetitionDistance', y='Sales', data=competition_distance_sales)
  plt.title('Effect of Distance to Competitors on Sales')
  plt.xlabel('Distance to Competitors (meters)')
  plt.ylabel('Average Sales')
  plt.show()

  # Log the effect of distance to competitors on sales
  logging.info(f'Effect of distance to competitors on sales:\n{competition_distance_sales}')

  # Analyze the effect of distance to competitors in city centers
  city_center_stores = train_store_df[train_store_df['StoreType'] == 'a']  # Assuming 'a' represents city center stores

  # Group by CompetitionDistance and calculate mean sales for city center stores
  city_center_competition_sales = city_center_stores.groupby('CompetitionDistance')['Sales'].mean().reset_index()

  # Plot the effect of distance to competitors on sales for city center stores
  plt.figure(figsize=(12, 6))
  sns.lineplot(x='CompetitionDistance', y='Sales', data=city_center_competition_sales)
  plt.title('Effect of Distance to Competitors on Sales for City Center Stores')
  plt.xlabel('Distance to Competitors (meters)')
  plt.ylabel('Average Sales')
  plt.show()

  # Log the effect of distance to competitors on sales for city center stores
  logging.info(f'Effect of distance to competitors on sales for city center stores:\n{city_center_competition_sales}')