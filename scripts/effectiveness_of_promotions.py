import matplotlib.pyplot as plt
import seaborn as sns
import logging

def effectiviness(train_df):
  # Effectiveness of Promotions

  # Determine if promotions could be deployed more effectively and identify which stores should have promotions

  # Calculate the average sales per store with and without promotions
  store_promo_sales = train_df.groupby(['Store', 'Promo'])['Sales'].mean().unstack().reset_index()
  store_promo_sales.columns = ['Store', 'NoPromo_Sales', 'Promo_Sales']

  # Calculate the difference in sales due to promotions
  store_promo_sales['Sales_Difference'] = store_promo_sales['Promo_Sales'] - store_promo_sales['NoPromo_Sales']

  # Log the average sales per store with and without promotions
  logging.info(f'Average sales per store with and without promotions:\n{store_promo_sales}')

  # Identify stores where promotions have the highest impact
  top_promo_stores = store_promo_sales.sort_values(by='Sales_Difference', ascending=False).head(10)

  # Plot the top stores where promotions have the highest impact
  plt.figure(figsize=(12, 6))
  sns.barplot(x='Store', y='Sales_Difference', data=top_promo_stores, palette='viridis')
  plt.title('Top 10 Stores Where Promotions Have the Highest Impact')
  plt.xlabel('Store')
  plt.ylabel('Sales Difference Due to Promotions')
  plt.show()

  # Log the top stores where promotions have the highest impact
  logging.info(f'Top 10 stores where promotions have the highest impact:\n{top_promo_stores}')

  # Identify stores where promotions have the least impact
  bottom_promo_stores = store_promo_sales.sort_values(by='Sales_Difference', ascending=True).head(10)

  # Plot the bottom stores where promotions have the least impact
  plt.figure(figsize=(12, 6))
  sns.barplot(x='Store', y='Sales_Difference', data=bottom_promo_stores, palette='viridis')
  plt.title('Top 10 Stores Where Promotions Have the Least Impact')
  plt.xlabel('Store')
  plt.ylabel('Sales Difference Due to Promotions')
  plt.show()

  # Log the bottom stores where promotions have the least impact
  logging.info(f'Top 10 stores where promotions have the least impact:\n{bottom_promo_stores}')

  # Determine if promotions could be deployed more effectively
  # Calculate the average sales difference across all stores
  average_sales_difference = store_promo_sales['Sales_Difference'].mean()

  # Log the average sales difference
  logging.info(f'Average sales difference due to promotions across all stores: {average_sales_difference}')

  # Identify stores where promotions are less effective than the average
  less_effective_promo_stores = store_promo_sales[store_promo_sales['Sales_Difference'] < average_sales_difference]

  # Log the stores where promotions are less effective than the average
  logging.info(f'Stores where promotions are less effective than the average:\n{less_effective_promo_stores}')

  # Plot the stores where promotions are less effective than the average
  plt.figure(figsize=(12, 6))
  sns.barplot(x='Store', y='Sales_Difference', data=less_effective_promo_stores, palette='viridis')
  plt.title('Stores Where Promotions Are Less Effective Than Average')
  plt.xlabel('Store')
  plt.ylabel('Sales Difference Due to Promotions')
  plt.show()

  # Log the completion of the effectiveness of promotions analysis
  logging.info('Effectiveness of promotions analysis completed successfully')