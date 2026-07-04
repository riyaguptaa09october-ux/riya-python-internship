"""
Sales Data Analysis using Pandas
Internship Task 3: Data Analysis Project (Pandas)

Goal:
    Load a CSV, clean it (handle missing values), filter/group the
    data, and generate meaningful summary statistics + insights.

Author: Riya Gupta
"""

import pandas as pd


def load_data(filepath):
    """Load the CSV file into a DataFrame."""
    try:
        df = pd.read_csv(filepath)
        print(f"Loaded '{filepath}' successfully — {len(df)} rows found.\n")
        return df
    except FileNotFoundError:
        print(f"Error: File '{filepath}' not found.")
        return None
    except pd.errors.EmptyDataError:
        print("Error: The CSV file is empty.")
        return None


def clean_data(df):
    """Clean the dataset: handle missing values, fix types."""
    print("Missing values before cleaning:")
    print(df.isnull().sum())
    print()

    # Fill missing Quantity with the median quantity per category
    df["Quantity"] = df.groupby("Category")["Quantity"].transform(
        lambda x: x.fillna(x.median())
    )

    # Fill missing Price with the average price for that product
    df["Price"] = df.groupby("Product")["Price"].transform(
        lambda x: x.fillna(x.mean())
    )

    # Drop rows where OrderDate is missing (can't analyze trends without it)
    df = df.dropna(subset=["OrderDate"])

    # Convert types
    df["Quantity"] = df["Quantity"].astype(int)
    df["OrderDate"] = pd.to_datetime(df["OrderDate"])

    # Add a computed column: total value per order
    df["TotalValue"] = df["Quantity"] * df["Price"]

    print("Missing values after cleaning:")
    print(df.isnull().sum())
    print()

    return df


def analyze_data(df):
    """Generate grouped summaries and insights."""
    print("=" * 55)
    print("SUMMARY STATISTICS")
    print("=" * 55)
    print(df[["Quantity", "Price", "TotalValue"]].describe())
    print()

    print("=" * 55)
    print("REVENUE BY CATEGORY")
    print("=" * 55)
    revenue_by_category = df.groupby("Category")["TotalValue"].sum().sort_values(ascending=False)
    print(revenue_by_category)
    print()

    print("=" * 55)
    print("REVENUE BY REGION")
    print("=" * 55)
    revenue_by_region = df.groupby("Region")["TotalValue"].sum().sort_values(ascending=False)
    print(revenue_by_region)
    print()

    print("=" * 55)
    print("TOP-SELLING PRODUCTS (by quantity)")
    print("=" * 55)
    top_products = df.groupby("Product")["Quantity"].sum().sort_values(ascending=False)
    print(top_products)
    print()

    print("=" * 55)
    print("KEY INSIGHTS")
    print("=" * 55)
    top_category = revenue_by_category.idxmax()
    top_region = revenue_by_region.idxmax()
    top_product = top_products.idxmax()
    total_revenue = df["TotalValue"].sum()

    print(f"- Total revenue across all orders: ₹{total_revenue:,.2f}")
    print(f"- Highest revenue category: {top_category} (₹{revenue_by_category.max():,.2f})")
    print(f"- Highest revenue region: {top_region} (₹{revenue_by_region.max():,.2f})")
    print(f"- Best-selling product by units: {top_product} ({top_products.max()} units)")


def main():
    filepath = "sales_data.csv"
    df = load_data(filepath)

    if df is not None:
        df = clean_data(df)
        analyze_data(df)
        df.to_csv("sales_data_cleaned.csv", index=False)
        print("\nCleaned dataset saved as 'sales_data_cleaned.csv'")


if __name__ == "__main__":
    main()
