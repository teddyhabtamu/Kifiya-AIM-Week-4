import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("visualization.log"),  # Save logs to a file
        logging.StreamHandler()  # Display logs in the console
    ]
)

def plot_promo_distribution(df: pd.DataFrame, dataset_name: str):
    """
    Plots the distribution of promotions in the given dataset.

    Parameters:
        df (pd.DataFrame): The input dataframe.
        dataset_name (str): Name of the dataset (Train/Test).
    """
    if 'Promo' not in df.columns:
        logging.error(f"Column 'Promo' not found in {dataset_name} dataset.")
        return

    plt.figure(figsize=(10, 6))
    ax = sns.countplot(x='Promo', data=df, palette="Blues")
    
    # Annotate bars with percentage
    total = len(df)
    for p in ax.patches:
        height = p.get_height()
        percentage = f"{100 * height / total:.1f}%"
        ax.annotate(percentage, (p.get_x() + p.get_width() / 2., height), ha='center', va='bottom')

    plt.title(f'Distribution of Promotions in {dataset_name} Set')
    plt.xlabel('Promo')
    plt.ylabel('Count')
    plt.show()

    # Log distribution
    promo_distribution = df['Promo'].value_counts(normalize=True)
    logging.info(f'Distribution of Promotions in {dataset_name} Set:\n{promo_distribution}')

def compare_promo_distributions(train_df: pd.DataFrame, test_df: pd.DataFrame):
    """
    Compares the distribution of promotions between the training and test datasets.

    Parameters:
        train_df (pd.DataFrame): The training dataset.
        test_df (pd.DataFrame): The test dataset.
    """
    if 'Promo' not in train_df.columns or 'Promo' not in test_df.columns:
        logging.error("Column 'Promo' not found in one or both datasets.")
        return

    # Compute distributions
    promo_train_distribution = train_df['Promo'].value_counts(normalize=True)
    promo_test_distribution = test_df['Promo'].value_counts(normalize=True)

    promo_comparison_df = pd.DataFrame({
        'Training Set': promo_train_distribution,
        'Test Set': promo_test_distribution
    }).reset_index().rename(columns={'index': 'Promo'})

    # Plot comparison
    promo_comparison_df.plot(kind='bar', x='Promo', figsize=(10, 6), color=["blue", "orange"])
    plt.title('Comparison of Promotion Distribution Between Training and Test Sets')
    plt.xlabel('Promo')
    plt.ylabel('Proportion')
    plt.legend(["Training Set", "Test Set"])
    plt.show()

    # Log comparison
    logging.info(f'Comparison of Promotion Distribution Between Training and Test Sets:\n{promo_comparison_df}')

def vis(train_df: pd.DataFrame, test_df: pd.DataFrame):
    """
    Visualizes the distribution of promotions in training and test sets.

    Parameters:
        train_df (pd.DataFrame): The training dataset.
        test_df (pd.DataFrame): The test dataset.
    """
    logging.info("Starting Promotion Distribution Visualization...")
    plot_promo_distribution(train_df, "Training")
    plot_promo_distribution(test_df, "Test")
    compare_promo_distributions(train_df, test_df)
    logging.info("Visualization Completed!")
