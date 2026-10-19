# Store Sales and Profit Analysis

## Overview

This project analyzes retail sales and profitability using the Sample Superstore dataset. It uses Python for data preparation and analysis, Pandas for data manipulation, and Plotly for interactive visualizations.

## Objectives

- Prepare and validate retail sales data.
- Analyze monthly sales and profit trends.
- Compare product categories and subcategories.
- Evaluate customer segment contributions.
- Identify profitable and loss-making product subcategories.
- Present findings through interactive charts and a business-insights report.

## Dataset

**File:** `Sample - Superstore.csv`

The dataset contains 9,994 records and 21 columns, including order and shipping dates, customer segments, product categories, sales, quantity, discount, and profit.

## Technologies

- Python 3.11
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Plotly

## Project Structure

```text
Store-Sales-Analysis/
├── data/
├── notebooks/
├── src/
│   ├── load_data.py
│   ├── clean_data.py
│   ├── analyze_sales.py
│   ├── visualize_sales.py
│   ├── analyze_profitability.py
│   └── create_report.py
├── reports/
├── requirements.txt
└── README.md
```

## Setup

Create and activate a virtual environment:

```powershell
py -3.11 -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Install the dependencies:

```powershell
python -m pip install -r requirements.txt
```

## Run the Project

Run the scripts from the project root in this order:

```powershell
python src/load_data.py
python src/clean_data.py
python src/analyze_sales.py
python src/visualize_sales.py
python src/analyze_profitability.py
python src/create_report.py
```

## Key Findings

- Total sales: $2,297,200.86
- Total profit: $286,397.02
- Overall profit margin: 12.47%
- Technology is the highest-profit product category.
- Consumer customers contribute the highest total profit among the customer segments.
- November 2017 has the highest monthly sales in the dataset.
- Tables, Bookcases, and Supplies have negative total profit.

## Outputs

The `reports/` directory contains:

- Data-cleaning report
- Monthly sales and profit summary
- Category, subcategory, and customer segment analysis
- Interactive monthly trend chart
- Interactive category performance chart
- Interactive segment performance chart
- Interactive subcategory profitability chart
- Business-insights report

Open the generated `.html` files in a web browser to explore the interactive visualizations.

## Data Preparation and Outliers

Order and shipping dates are converted to datetime values. Numeric columns are validated, exact duplicates are checked, and rows with invalid required values are removed.

Potential outliers are identified using the interquartile range (IQR) method. Flagged observations are retained for analysis rather than automatically removed.

## Limitations

This project performs descriptive analysis and does not establish causal relationships. Additional investigation is required to determine why particular subcategories have low or negative profit.

## Conclusion

The analysis highlights differences in sales and profitability across product categories, subcategories, months, and customer segments. These findings can guide further investigation into pricing, discounts, costs, and inventory planning.