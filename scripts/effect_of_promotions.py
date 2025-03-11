import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("promotion_analysis.log"),
        logging.StreamHandler()
    ]
)

def effect_of_promotion(train_df: pd.DataFrame):
    """
    Analyzes the effect of promotions on sales and customer behavior.

    Parameters:
        train_df (pd.DataFrame): The training dataset.

    Returns:
        None
    """
    # Ensure required columns exist
    required_columns = {'Promo', 'Sales', 'Customers', 'Store'}
    if not required_columns.issubset(train_df.columns):
        missing_cols = required_columns - set(train_df.columns)
        logging.error(f"Missing columns in dataset: {missing_cols}")
        return

    # Effect of Promotions on Sales
    promo_sales = train_df.groupby('Promo')['Sales'].mean().reset_index()
    plt.figure(figsize=(10, 6))
    sns.barplot(x='Promo', y='Sales', data=promo_sales, palette='Blues')
    plt.title('Effect of Promotions on Sales')
    plt.xlabel('Promo')
    plt.ylabel('Average Sales')
    plt.xticks([0, 1], ['No Promo', 'Promo'])
    plt.savefig("effect_of_promotions_sales.png", dpi=300, bbox_inches='tight')
    plt.show()

    logging.info(f'Effect of promotions on sales:\n{promo_sales}')

    # Effect of Promotions on Customer Count
    promo_customers = train_df.groupby('Promo')['Customers'].mean().reset_index()
    plt.figure(figsize=(10, 6))
    sns.barplot(x='Promo', y='Customers', data=promo_customers, palette='Greens')
    plt.title('Effect of Promotions on Number of Customers')
    plt.xlabel('Promo')
    plt.ylabel('Average Number of Customers')
    plt.xticks([0, 1], ['No Promo', 'Promo'])
    plt.savefig("effect_of_promotions_customers.png", dpi=300, bbox_inches='tight')
    plt.show()

    logging.info(f'Effect of promotions on number of customers:\n{promo_customers}')

    # Comparison of Customers With and Without Promotions
    no_promo_customers = train_df[train_df['Promo'] == 0].groupby('Store')['Customers'].mean().reset_index()
    promo_customers = train_df[train_df['Promo'] == 1].groupby('Store')['Customers'].mean().reset_index()

    # Merge dataframes on 'Store'
    comparison_df = pd.merge(no_promo_customers, promo_customers, on='Store', suffixes=('_NoPromo', '_Promo'))
    
    if not comparison_df.empty:
        # Scatter plot to compare customer behavior with and without promotions
        plt.figure(figsize=(10, 6))
        sns.scatterplot(x='Customers_NoPromo', y='Customers_Promo', data=comparison_df, alpha=0.5, color='purple')
        plt.plot([comparison_df['Customers_NoPromo'].min(), comparison_df['Customers_NoPromo'].max()],
                 [comparison_df['Customers_NoPromo'].min(), comparison_df['Customers_NoPromo'].max()],
                 linestyle="--", color="red")  # Diagonal reference line
        plt.title('Comparison of Customers With and Without Promotions')
        plt.xlabel('Customers Without Promo')
        plt.ylabel('Customers With Promo')
        plt.savefig("effect_of_promotions_comparison.png", dpi=300, bbox_inches='tight')
        plt.show()

        logging.info(f'Comparison of customers with and without promotions:\n{comparison_df}')
    else:
        logging.warning("No data available for customer comparison between promo and non-promo stores.")
