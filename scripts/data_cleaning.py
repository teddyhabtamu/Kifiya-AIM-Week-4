import logging

def handle_missing_data(df):
    # Log the initial state of missing data
    logging.info(f'Initial missing data:\n{df.isnull().sum()}')
    
    # Fill missing values with appropriate strategies
    df.fillna(method='ffill', inplace=True)  # Forward fill for simplicity
    
    # Log the final state of missing data
    logging.info(f'Final missing data:\n{df.isnull().sum()}')
    return df

# Function to detect and handle outliers
def handle_outliers(df, column):
    # Log the initial state of outliers
    logging.info(f'Initial outliers in {column}:\n{df[column].describe()}')
    
    # Remove outliers using IQR method
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    df = df[(df[column] >= lower_bound) & (df[column] <= upper_bound)]
    
    # Log the final state of outliers
    logging.info(f'Final outliers in {column}:\n{df[column].describe()}')
    return df
