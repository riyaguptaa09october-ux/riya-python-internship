# Task 3: Data Analysis Project (Pandas)

## Goal
Analyze a dataset, clean it, and generate summary statistics.

## Requirements Met
- ✅ Loads CSV using Pandas (`sales_data.csv`)
- ✅ Cleaning: fills missing Quantity/Price using group-wise median/mean, drops rows with missing dates
- ✅ Filtering & grouping: revenue grouped by Category, by Region, and top products by quantity
- ✅ Generates meaningful insights: total revenue, top category, top region, best-selling product

## How to Run
```bash
pip install pandas
python analyze_sales.py
```

## Sample Output (real run)
```
KEY INSIGHTS
=======================================================
- Total revenue across all orders: ₹340,250.00
- Highest revenue category: Electronics (₹335,800.00)
- Highest revenue region: South (₹220,250.00)
- Best-selling product by units: Pen (45 units)
```

## Deliverables
- ✅ Script (`analyze_sales.py`)
- ✅ Raw dataset (`sales_data.csv`)
- ✅ Cleaned dataset output (`sales_data_cleaned.csv`)
- Graphs: optional, not included
