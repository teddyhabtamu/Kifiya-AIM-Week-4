import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import logging

def assortmentEffect(train_df, store_df):
  # Effect of Assortment Type on Sales

  # Merge train_df with store_df to include assortment type information
  train_store_df = pd.merge(train_df, store_df, on='Store')

  # Log the merging of dataframes
  logging.info('Merged train_df with store_df to include assortment type information')

  # Group by Assortment and calculate mean sales
  assortment_sales = train_store_df.groupby('Assortment')['Sales'].mean().reset_index()

  # Plot the effect of assortment type on sales
  plt.figure(figsize=(10, 6))
  sns.barplot(x='Assortment', y='Sales', data=assortment_sales, palette='viridis')
  plt.title('Effect of Assortment Type on Sales')
  plt.xlabel('Assortment Type')
  plt.ylabel('Average Sales')
  plt.show()

  # Log the effect of assortment type on sales
  logging.info(f'Effect of assortment type on sales:\n{assortment_sales}')