import matplotlib.pyplot as plt
import seaborn as sns
import logging

def correlation(train_df):
  # Correlation Between Sales and Number of Customers

  # Calculate the correlation between Sales and Customers
  correlation = train_df[['Sales', 'Customers']].corr().iloc[0, 1]

  # Log the correlation value
  logging.info(f'Correlation between Sales and Customers: {correlation}')

  # Plot the relationship between Sales and Customers
  plt.figure(figsize=(10, 6))
  sns.scatterplot(x='Customers', y='Sales', data=train_df, alpha=0.5)
  plt.title('Correlation Between Sales and Number of Customers')
  plt.xlabel('Number of Customers')
  plt.ylabel('Sales')
  plt.show()

  # Display the correlation value on the plot
  plt.annotate(f'Correlation: {correlation:.2f}', xy=(0.05, 0.95), xycoords='axes fraction', fontsize=12, color='red')

  # Log the completion of the correlation analysis
  logging.info('Correlation analysis between Sales and Customers completed successfully')