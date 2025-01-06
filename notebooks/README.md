# Notebooks

This directory contains Jupyter notebooks used for exploratory data analysis (EDA) and other analyses related to the Rossmann Pharmaceuticals sales forecasting project.

## Notebooks

### 1. Exploration_of_customer_behavior.ipynb

This notebook contains the exploratory data analysis (EDA) for understanding customer purchasing behavior. It includes the following sections:-

1. **Import Required Libraries**: Import necessary libraries such as pandas, matplotlib, seaborn, and logging.
2. **Load Data**: Load the datasets (`store.csv`, `train.csv`, etc.) into pandas DataFrames.
3. **Data Cleaning**: Handle missing data and outliers to ensure the data is clean and ready for analysis.
4. **Exploratory Data Analysis**:
   - **Distribution of Promotions**: Check the distribution of promotions in both training and test sets.
   - **Sales Behavior During Holidays**: Analyze sales behavior before, during, and after holidays.
   - **Seasonal Purchase Behaviors**: Identify any seasonal purchase behaviors (e.g., Christmas, Easter).
   - **Correlation Between Sales and Number of Customers**: Analyze the correlation between sales and the number of customers.
   - **Effect of Promotions on Sales**: Analyze how promotions affect sales and whether they attract more customers.
   - **Effectiveness of Promotions**: Determine if promotions could be deployed more effectively and identify which stores should have promotions.
   - **Customer Behavior During Store Opening and Closing Times**: Analyze customer behavior during store opening and closing times.
   - **Sales on Weekends for Stores Open on All Weekdays**: Analyze sales on weekends for stores that are open on all weekdays.
   - **Effect of Assortment Type on Sales**: Analyze how the assortment type affects sales.
   - **Effect of Distance to Competitors on Sales**: Analyze how the distance to competitors affects sales.
   - **Effect of Opening or Reopening of Competitors**: Analyze the effect of opening or reopening of competitors on sales.

5. **Logging**: Log the steps using the `logging` library in Python for traceability and reproducibility.

## Usage

1. Ensure you have the required datasets (`store.csv`, `train.csv`, etc.) in the appropriate directory.
2. Open the `Exploration_of_customer_behavior.ipynb` notebook in Jupyter Notebook or JupyterLab.
3. Run the cells in the notebook to perform data cleaning, exploratory data analysis, and visualize the results.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License.
