import logging
import pandas as pd

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("data_cleaning.log"),  # Save logs to a file
        logging.StreamHandler()  # Display logs in the console
    ]
)

def handle_missing_data(df: pd.DataFrame, method: str = "ffill") -> pd.DataFrame:
    """
    Handle missing values in the dataset.

    Parameters:
        df (pd.DataFrame): The input dataframe.
        method (str): The method to fill missing values. 
                      Options: 'ffill', 'bfill', 'mean', 'median', 'mode'.

    Returns:
        pd.DataFrame: The cleaned dataframe with missing values handled.
    """
    logging.info(f"Initial missing data:\n{df.isnull().sum()}")

    # Choose missing value handling method
    if method == "mean":
        df.fillna(df.mean(), inplace=True)
    elif method == "median":
        df.fillna(df.median(), inplace=True)
    elif method == "mode":
        df.fillna(df.mode().iloc[0], inplace=True)  # Mode returns a dataframe
    else:
        df.fillna(method=method, inplace=True)  # Uses ffill or bfill

    logging.info(f"Final missing data:\n{df.isnull().sum()}")
    return df

def handle_outliers(df: pd.DataFrame, column: str, method: str = "remove") -> pd.DataFrame:
    """
    Detect and handle outliers in a specified column using the IQR method.

    Parameters:
        df (pd.DataFrame): The input dataframe.
        column (str): The column to check for outliers.
        method (str): The outlier handling method ('remove' or 'cap').

    Returns:
        pd.DataFrame: The dataframe with outliers handled.
    """
    logging.info(f"Initial statistics for {column}:\n{df[column].describe()}")

    # Compute IQR
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR

    if method == "remove":
        df = df[(df[column] >= lower_bound) & (df[column] <= upper_bound)]
    elif method == "cap":
        df[column] = df[column].clip(lower=lower_bound, upper=upper_bound)

    logging.info(f"Final statistics for {column}:\n{df[column].describe()}")
    return df
