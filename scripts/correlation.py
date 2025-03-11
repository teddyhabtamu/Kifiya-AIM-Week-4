import matplotlib.pyplot as plt
import seaborn as sns
import logging
import pandas as pd

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("correlation_analysis.log"),
        logging.StreamHandler()
    ]
)

def correlation(train_df: pd.DataFrame):
    """
    Computes and visualizes the correlation between Sales and Number of Customers.

    Parameters:
        train_df (pd.DataFrame): The training dataset.

    Returns:
        None
    """
    # Ensure required columns exist
    if 'Sales' not in train_df.columns or 'Customers' not in train_df.columns:
        logging.error("Missing 'Sales' or 'Customers' column in dataset.")
        return

    # Compute correlation
    correlation_value = train_df[['Sales', 'Customers']].corr().at['Sales', 'Customers']
    logging.info(f'Correlation between Sales and Customers: {correlation_value:.4f}')

    # Plot relationship with regression trend
    plt.figure(figsize=(10, 6))
    sns.regplot(x='Customers', y='Sales', data=train_df, scatter_kws={'alpha': 0.5}, line_kws={'color': 'red'})
    plt.title('Correlation Between Sales and Number of Customers')
    plt.xlabel('Number of Customers')
    plt.ylabel('Sales')

    # Display correlation value on plot
    plt.text(
        0.05, 0.9, f'Correlation: {correlation_value:.2f}',
        transform=plt.gca().transAxes, fontsize=12, color='red', bbox=dict(facecolor='white', alpha=0.7)
    )

    # Save and show plot
    plt.savefig("correlation_sales_customers.png", dpi=300, bbox_inches='tight')
    plt.show()

    logging.info('Correlation analysis completed successfully. Plot saved as correlation_sales_customers.png.')
