# Rossmann Pharmaceuticals Sales Forecasting

![alt text](image-1.png)

## Project Overview

This project aims to forecast sales for Rossmann Pharmaceuticals stores across several cities six weeks ahead of time. The finance team relies on these forecasts to make informed decisions. The project involves building and serving an end-to-end product that delivers these predictions to analysts in the finance team.

## Data Sources

The following datasets are used in this project:
- `sample_submission.csv`
- `store.csv`
- `test.csv`
- `train.csv`


## Notebooks

- `Exploration_of_customer_behavior.ipynb`: This notebook contains the exploratory data analysis (EDA) for understanding customer purchasing behavior. It includes data cleaning, visualization, and analysis of various factors affecting sales.

## Scripts

The `scripts` directory contains the following Python scripts used for different analyses:

- `data_cleaning.py`: Functions for handling missing data and outliers.
- `correlation.py`: Functions for analyzing the correlation between sales and the number of customers.
- `effect_of_promotions.py`: Functions for analyzing the effect of promotions on sales.
- `effectiveness_of_promotions.py`: Functions for determining the effectiveness of promotions.
- `customer_behavior.py`: Functions for analyzing customer behavior during store opening and closing times.
- `average_sale_on_weekend.py`: Functions for analyzing average sales on weekends.
- `effect_of_assortment.py`: Functions for analyzing the effect of assortment type on sales.
- `effect_of_distance.py`: Functions for analyzing the effect of distance to competitors on sales.
- `sales_behavior_during_holidays.py`: Functions for analyzing sales behavior during holidays.
- `seasonal_purchase_behaviors.py`: Functions for analyzing seasonal purchase behaviors.

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/rossmann-pharmaceuticals-sales-forecasting.git
    cd rossmann-pharmaceuticals-sales-forecasting
    ```

2. Create and activate a virtual environment:
    ```sh
    python -m venv .venv
    source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`
    ```

3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. Navigate to the [notebooks](http://_vscodecontentref_/5) directory and open the [Exploration_of_customer_behavior.ipynb](http://_vscodecontentref_/6) notebook.
2. Run the cells in the notebook to perform data cleaning, exploratory data analysis, and visualize the results.

## Logging

The project uses the `logging` library in Python for traceability and reproducibility. Logs are generated during the execution of scripts and notebook cells to provide insights into the steps performed and any issues encountered.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License.
![alt text](image.png)