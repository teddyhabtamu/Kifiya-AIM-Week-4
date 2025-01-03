# Scripts

This directory contains Python scripts used for various analyses and data processing tasks related to the Rossmann Pharmaceuticals sales forecasting project.

## Scripts

### 1. data_cleaning.py
Functions for handling missing data and outliers to ensure the data is clean and ready for analysis.

### 2. correlation.py
Functions for analyzing the correlation between sales and the number of customers.

### 3. effect_of_promotions.py
Functions for analyzing the effect of promotions on sales.

### 4. effectiveness_of_promotions.py
Functions for determining the effectiveness of promotions and identifying which stores should have promotions.

### 5. customer_behavior.py
Functions for analyzing customer behavior during store opening and closing times.

### 6. average_sale_on_weekend.py
Functions for analyzing average sales on weekends for stores that are open on all weekdays.

### 7. effect_of_assortment.py
Functions for analyzing how the assortment type affects sales.

### 8. effect_of_distance.py
Functions for analyzing how the distance to competitors affects sales.

### 9. sales_behavior_during_holidays.py
Functions for analyzing sales behavior before, during, and after holidays.

### 10. seasonal_purchase_behaviors.py
Functions for analyzing seasonal purchase behaviors (e.g., Christmas, Easter).

## Usage

1. Ensure you have the required datasets (`store.csv`, `train.csv`, etc.) in the appropriate directory.
2. Import the necessary functions from the scripts in your Jupyter notebooks or other Python scripts.
3. Use the functions to perform data cleaning, exploratory data analysis, and other analyses as needed.

## Example

Here is an example of how to use a function from one of the scripts:

```python
from scripts.data_cleaning import handle_missing_data

# Load data
train_df = pd.read_csv('train.csv')

# Handle missing data
cleaned_train_df = handle_missing_data(train_df)