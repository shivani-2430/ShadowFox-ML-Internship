from pathlib import Path
import pandas as pd
import plotly.express as px

PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = PROJECT_ROOT / "data"
REPORTS_DIR = PROJECT_ROOT / "reports"


def analyze_profitability():
    df = pd.read_csv(DATA_DIR / "superstore_cleaned.csv")

    REPORTS_DIR.mkdir(parents=True, exist_ok=True)

    subcategory = (
        df.groupby(["Category", "Sub-Category"], as_index=False)
        .agg(
            Sales=("Sales", "sum"),
            Profit=("Profit", "sum"),
            Quantity=("Quantity", "sum")
        )
    )

    subcategory["Profit Margin (%)"] = (
        subcategory["Profit"] / subcategory["Sales"] * 100
    )

    subcategory = subcategory.sort_values(
        "Profit", ascending=False
    )

    subcategory.to_csv(
        REPORTS_DIR / "subcategory_profitability.csv",
        index=False
    )

    chart = px.bar(
        subcategory.sort_values("Profit"),
        x="Profit",
        y="Sub-Category",
        color="Category",
        orientation="h",
        hover_data=["Sales", "Quantity", "Profit Margin (%)"],
        title="Profitability by Product Subcategory"
    )

    chart.write_html(
        str(REPORTS_DIR / "subcategory_profitability.html")
    )

    print("\nTOP 10 SUBCATEGORIES BY PROFIT")
    print(
        subcategory.head(10).round(2).to_string(index=False)
    )

    print("\nBOTTOM 10 SUBCATEGORIES BY PROFIT")
    print(
        subcategory.sort_values("Profit", ascending=True)
        .head(10)
        .round(2)
        .to_string(index=False)
    )

    print("\nOverall sales:", round(df["Sales"].sum(), 2))
    print("Overall profit:", round(df["Profit"].sum(), 2))
    print(
        "Overall profit margin (%):",
        round(df["Profit"].sum() / df["Sales"].sum() * 100, 2)
    )

    print("\nSaved subcategory analysis and interactive chart.")


if __name__ == "__main__":
    analyze_profitability()