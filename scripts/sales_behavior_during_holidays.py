import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import logging
import numpy as np

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("holiday_sales_analysis.log"),
        logging.StreamHandler()
    ]
)

def preprocess_holiday_data(train_df: pd.DataFrame):
    """
    Preprocesses the training dataset by extracting date features and marking holiday periods.
    
    Parameters:
        train_df (pd.DataFrame): The training dataset.
    
    Returns:
        pd.DataFrame: The processed dataset with holiday-related columns.
    """
    if 'Date' not in train_df.columns:
        logging.error("Missing 'Date' column in dataset.")
        return None
    if 'Sales' not in train_df.columns:
        logging.error("Missing 'Sales' column in dataset.")
        return None

    try:
        train_df['Date'] = pd.to_datetime(train_df['Date'])
    except Exception as e:
        logging.error(f"Error converting 'Date' column to datetime: {e}")
        return None

    # Extract year, month, and day of week
    train_df['Year'] = train_df['Date'].dt.year
    train_df['Month'] = train_df['Date'].dt.month
    train_df['DayOfWeek'] = train_df['Date'].dt.dayofweek

    # Define major holidays
    holidays = ['2013-12-25', '2014-12-25', '2015-12-25',  # Christmas
                '2013-04-01', '2014-04-21', '2015-04-06']  # Easter
    holidays = pd.to_datetime(holidays)

    # Create a column to indicate if a date is a holiday
    train_df['IsHoliday'] = train_df['Date'].isin(holidays)

    # Categorize holiday periods
    train_df['HolidayPeriod'] = np.where(train_df['IsHoliday'], 'During Holiday',
                              np.where(train_df['Date'].isin(holidays - pd.Timedelta(days=1)), 'Before Holiday',
                              np.where(train_df['Date'].isin(holidays + pd.Timedelta(days=1)), 'After Holiday', 'Non-Holiday')))

    logging.info("Holiday-related columns created successfully")
    return train_df

def plot_holiday_sales_behavior(train_df: pd.DataFrame):
    """
    Plots the sales behavior before, during, and after holidays.

    Parameters:
        train_df (pd.DataFrame): The dataset with holiday-related columns.
    """
    if 'HolidayPeriod' not in train_df.columns:
        logging.error("Missing 'HolidayPeriod' column in dataset. Ensure preprocessing is done first.")
        return

    holiday_sales = train_df.groupby(['Year', 'HolidayPeriod'])['Sales'].mean().reset_index()

    plt.figure(figsize=(12, 6))
    sns.barplot(x='HolidayPeriod', y='Sales', hue='Year', data=holiday_sales, palette='viridis')

    plt.title('Sales Behavior Before, During, and After Holidays')
    plt.xlabel('Holiday Period')
    plt.ylabel('Average Sales')
    plt.legend(title="Year")
    plt.show()

    logging.info(f'Sales behavior during holidays:\n{holiday_sales}')

def holiday(train_df: pd.DataFrame):
    """
    Runs the complete holiday sales behavior analysis.

    Parameters:
        train_df (pd.DataFrame): The training dataset.
    """
    logging.info("Starting holiday sales analysis...")
    train_df = preprocess_holiday_data(train_df)
    if train_df is not None:
        plot_holiday_sales_behavior(train_df)
    logging.info("Holiday sales analysis completed!")
