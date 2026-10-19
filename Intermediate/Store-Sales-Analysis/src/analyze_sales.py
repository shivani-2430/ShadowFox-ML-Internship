from pathlib import Path
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = PROJECT_ROOT / "data"
REPORTS_DIR = PROJECT_ROOT / "reports"


def analyze_sales():
    df = pd.read_csv(
        DATA_DIR / "superstore_cleaned.csv",
        parse_dates=["Order Date", "Ship Date"]
    )

    REPORTS_DIR.mkdir(parents=True, exist_ok=True)

    monthly = (
        df.set_index("Order Date")
        .resample("MS")
        .agg(
            Sales=("Sales", "sum"),
            Profit=("Profit", "sum"),
            Orders=("Order ID", "nunique")
        )
        .reset_index()
    )

    category = (
        df.groupby("Category", as_index=False)
        .agg(
            Sales=("Sales", "sum"),
            Profit=("Profit", "sum"),
            Quantity=("Quantity", "sum")
        )
        .sort_values("Sales", ascending=False)
    )

    subcategory = (
        df.groupby(["Category", "Sub-Category"], as_index=False)
        .agg(
            Sales=("Sales", "sum"),
            Profit=("Profit", "sum"),
            Quantity=("Quantity", "sum")
        )
        .sort_values("Profit", ascending=False)
    )

    segment = (
        df.groupby("Segment", as_index=False)
        .agg(
            Sales=("Sales", "sum"),
            Profit=("Profit", "sum"),
            Orders=("Order ID", "nunique")
        )
        .sort_values("Sales", ascending=False)
    )

    monthly.to_csv(REPORTS_DIR / "monthly_sales_profit.csv", index=False)
    category.to_csv(REPORTS_DIR / "category_analysis.csv", index=False)
    subcategory.to_csv(REPORTS_DIR / "subcategory_analysis.csv", index=False)
    segment.to_csv(REPORTS_DIR / "customer_segment_analysis.csv", index=False)

    print("\nMONTHLY SALES AND PROFIT (latest 12 months)")
    print(monthly.tail(12).to_string(index=False, formatters={
        "Sales": "{:,.2f}".format,
        "Profit": "{:,.2f}".format
    }))

    print("\nCATEGORY PERFORMANCE")
    print(category.round(2).to_string(index=False))

    print("\nTOP 10 SUBCATEGORIES BY PROFIT")
    print(subcategory.head(10).round(2).to_string(index=False))

    print("\nCUSTOMER SEGMENT PERFORMANCE")
    print(segment.round(2).to_string(index=False))

    print("\nAnalysis CSV files saved in:", REPORTS_DIR)


if __name__ == "__main__":
    analyze_sales()