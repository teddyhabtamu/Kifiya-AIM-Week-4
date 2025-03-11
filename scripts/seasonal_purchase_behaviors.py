import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("seasonal_sales_analysis.log"),
        logging.StreamHandler()
    ]
)

def preprocess_seasonal_data(train_df: pd.DataFrame):
    """
    Preprocesses the dataset to extract date-related features for seasonal analysis.

    Parameters:
        train_df (pd.DataFrame): The training dataset.

    Returns:
        pd.DataFrame: Processed dataset with seasonal indicators.
    """
    if 'Date' not in train_df.columns:
        logging.error("Missing 'Date' column in dataset.")
        return None
    if 'Sales' not in train_df.columns:
        logging.error("Missing 'Sales' column in dataset.")
        return None

    train_df['Date'] = pd.to_datetime(train_df['Date'])
    train_df['Year'] = train_df['Date'].dt.year
    train_df['Month'] = train_df['Date'].dt.month
    train_df['Day'] = train_df['Date'].dt.day  # For Christmas filter

    # Define Christmas (December 20–31)
    train_df['IsChristmas'] = (train_df['Month'] == 12) & (train_df['Day'] >= 20)

    # Define Easter Dates
    easter_dates = pd.to_datetime(['2013-03-31', '2014-04-20', '2015-04-05'])
    train_df['IsEaster'] = train_df['Date'].isin(easter_dates)

    logging.info("Seasonal columns (Christmas and Easter) added successfully.")
    return train_df

def analyze_seasonal_sales(train_df: pd.DataFrame):
    """
    Analyzes and visualizes sales behavior during seasonal periods (Christmas & Easter).

    Parameters:
        train_df (pd.DataFrame): The dataset with seasonal indicators.
    """
    if 'IsChristmas' not in train_df.columns or 'IsEaster' not in train_df.columns:
        logging.error("Seasonal columns are missing. Ensure preprocessing is completed first.")
        return

    # Christmas Sales Analysis
    christmas_sales = train_df[train_df['IsChristmas']].groupby('Year')['Sales'].mean().reset_index()
    plt.figure(figsize=(12, 6))
    sns.barplot(x='Year', y='Sales', data=christmas_sales, palette='coolwarm')
    plt.title('Average Sales During Christmas (Dec 20-31)')
    plt.xlabel('Year')
    plt.ylabel('Average Sales')
    plt.show()
    logging.info(f'Sales behavior during Christmas:\n{christmas_sales}')

    # Easter Sales Analysis
    easter_sales = train_df[train_df['IsEaster']].groupby('Year')['Sales'].mean().reset_index()
    plt.figure(figsize=(12, 6))
    sns.barplot(x='Year', y='Sales', data=easter_sales, palette='coolwarm')
    plt.title('Average Sales During Easter')
    plt.xlabel('Year')
    plt.ylabel('Average Sales')
    plt.show()
    logging.info(f'Sales behavior during Easter:\n{easter_sales}')

def analyze_monthly_trends(train_df: pd.DataFrame):
    """
    Visualizes monthly sales trends to capture seasonal patterns.

    Parameters:
        train_df (pd.DataFrame): The dataset with date features.
    """
    monthly_sales = train_df.groupby(['Year', 'Month'])['Sales'].mean().reset_index()

    plt.figure(figsize=(14, 6))
    sns.lineplot(x='Month', y='Sales', hue='Year', data=monthly_sales, marker='o', palette='viridis')
    plt.title('Monthly Sales Trends Over the Years')
    plt.xlabel('Month')
    plt.ylabel('Average Sales')
    plt.xticks(range(1, 13), ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
    plt.legend(title="Year")
    plt.show()

    logging.info(f'Monthly sales trends:\n{monthly_sales}')

def seasonal_behavior(train_df: pd.DataFrame):
    """
    Runs the complete seasonal sales analysis.

    Parameters:
        train_df (pd.DataFrame): The training dataset.
    """
    logging.info("Starting seasonal sales analysis...")
    train_df = preprocess_seasonal_data(train_df)
    if train_df is not None:
        analyze_seasonal_sales(train_df)
        analyze_monthly_trends(train_df)
    logging.info("Seasonal sales analysis completed!")
