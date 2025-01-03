import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 
import logging

def effect_of_promotion(train_df):
  # Effect of Promotions on Sales

  # Group by Promo and calculate mean sales
  promo_sales = train_df.groupby('Promo')['Sales'].mean().reset_index()

  # Plot the effect of promotions on sales
  plt.figure(figsize=(10, 6))
  sns.barplot(x='Promo', y='Sales', data=promo_sales, palette='viridis')
  plt.title('Effect of Promotions on Sales')
  plt.xlabel('Promo')
  plt.ylabel('Average Sales')
  plt.show()

  # Log the effect of promotions on sales
  logging.info(f'Effect of promotions on sales:\n{promo_sales}')

  # Analyze if promotions attract more customers
  promo_customers = train_df.groupby('Promo')['Customers'].mean().reset_index()

  # Plot the effect of promotions on the number of customers
  plt.figure(figsize=(10, 6))
  sns.barplot(x='Promo', y='Customers', data=promo_customers, palette='viridis')
  plt.title('Effect of Promotions on Number of Customers')
  plt.xlabel('Promo')
  plt.ylabel('Average Number of Customers')
  plt.show()

  # Log the effect of promotions on the number of customers
  logging.info(f'Effect of promotions on number of customers:\n{promo_customers}')

  # Analyze the effect of promotions on existing customers
  existing_customers = train_df[train_df['Promo'] == 0].groupby('Store')['Customers'].mean().reset_index()
  promo_customers = train_df[train_df['Promo'] == 1].groupby('Store')['Customers'].mean().reset_index()

  # Merge the dataframes to compare
  comparison_df = pd.merge(existing_customers, promo_customers, on='Store', suffixes=('_NoPromo', '_Promo'))

  # Plot the comparison of customers with and without promotions
  plt.figure(figsize=(10, 6))
  sns.scatterplot(x='Customers_NoPromo', y='Customers_Promo', data=comparison_df, alpha=0.5)
  plt.title('Comparison of Customers With and Without Promotions')
  plt.xlabel('Customers Without Promo')
  plt.ylabel('Customers With Promo')
  plt.show()

  # Log the comparison of customers with and without promotions
  logging.info(f'Comparison of customers with and without promotions:\n{comparison_df}')