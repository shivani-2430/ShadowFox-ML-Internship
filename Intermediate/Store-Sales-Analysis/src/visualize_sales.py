from pathlib import Path
import pandas as pd
import plotly.express as px

PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = PROJECT_ROOT / "data"
REPORTS_DIR = PROJECT_ROOT / "reports"


def create_visualizations():
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
            Profit=("Profit", "sum")
        )
        .reset_index()
    )

    category = (
        df.groupby("Category", as_index=False)
        .agg(Sales=("Sales", "sum"), Profit=("Profit", "sum"))
    )

    segment = (
        df.groupby("Segment", as_index=False)
        .agg(Sales=("Sales", "sum"), Profit=("Profit", "sum"))
    )

    monthly_fig = px.line(
        monthly,
        x="Order Date",
        y=["Sales", "Profit"],
        title="Monthly Sales and Profit Trends",
        markers=True,
        labels={"value": "Amount", "Order Date": "Month", "variable": "Metric"}
    )
    monthly_fig.write_html(
        str(REPORTS_DIR / "monthly_trends.html")
    )

    category_fig = px.bar(
        category,
        x="Category",
        y=["Sales", "Profit"],
        barmode="group",
        title="Sales and Profit by Product Category",
        labels={"value": "Amount", "variable": "Metric"}
    )
    category_fig.write_html(
        str(REPORTS_DIR / "category_performance.html")
    )

    segment_fig = px.bar(
        segment,
        x="Segment",
        y=["Sales", "Profit"],
        barmode="group",
        title="Sales and Profit by Customer Segment",
        labels={"value": "Amount", "variable": "Metric"}
    )
    segment_fig.write_html(
        str(REPORTS_DIR / "segment_performance.html")
    )

    print("Interactive charts created successfully.")

    for filename in [
        "monthly_trends.html",
        "category_performance.html",
        "segment_performance.html"
    ]:
        print(REPORTS_DIR / filename)


if __name__ == "__main__":
    create_visualizations()