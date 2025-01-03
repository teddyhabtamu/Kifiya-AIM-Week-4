import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import logging


def vis(train_df, test_df):
  # Distribution of Promotions

  # Check for distribution of promotions in the training set
  plt.figure(figsize=(10, 6))
  sns.countplot(x='Promo', data=train_df)
  plt.title('Distribution of Promotions in Training Set')
  plt.xlabel('Promo')
  plt.ylabel('Count')
  plt.show()

  # Log the distribution of promotions in the training set
  promo_train_distribution = train_df['Promo'].value_counts(normalize=True)
  logging.info(f'Distribution of Promotions in Training Set:\n{promo_train_distribution}')

  # Check for distribution of promotions in the test set
  plt.figure(figsize=(10, 6))
  sns.countplot(x='Promo', data=test_df)
  plt.title('Distribution of Promotions in Test Set')
  plt.xlabel('Promo')
  plt.ylabel('Count')
  plt.show()

  # Log the distribution of promotions in the test set
  promo_test_distribution = test_df['Promo'].value_counts(normalize=True)
  logging.info(f'Distribution of Promotions in Test Set:\n{promo_test_distribution}')

  # Compare the distribution of promotions between training and test sets
  promo_comparison_df = pd.DataFrame({
      'Training Set': promo_train_distribution,
      'Test Set': promo_test_distribution
  }).reset_index().rename(columns={'index': 'Promo'})

  # Plot the comparison
  promo_comparison_df.plot(kind='bar', x='Promo', figsize=(10, 6))
  plt.title('Comparison of Promotion Distribution Between Training and Test Sets')
  plt.xlabel('Promo')
  plt.ylabel('Proportion')
  plt.show()

  # Log the comparison of promotion distribution
  logging.info(f'Comparison of Promotion Distribution Between Training and Test Sets:\n{promo_comparison_df}')