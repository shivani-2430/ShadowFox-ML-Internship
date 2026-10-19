from pathlib import Path
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parents[1]
REPORTS_DIR = PROJECT_ROOT / "reports"


def create_report():
    category = pd.read_csv(REPORTS_DIR / "category_analysis.csv")
    segment = pd.read_csv(REPORTS_DIR / "customer_segment_analysis.csv")
    subcategory = pd.read_csv(REPORTS_DIR / "subcategory_profitability.csv")
    monthly = pd.read_csv(REPORTS_DIR / "monthly_sales_profit.csv")

    total_sales = category["Sales"].sum()
    total_profit = category["Profit"].sum()
    overall_margin = total_profit / total_sales * 100

    best_category = category.loc[category["Profit"].idxmax()]
    best_segment = segment.loc[segment["Profit"].idxmax()]
    best_month = monthly.loc[monthly["Sales"].idxmax()]

    loss_making = (
        subcategory[subcategory["Profit"] < 0]
        .sort_values("Profit")
    )

    low_positive_profit = (
        subcategory[subcategory["Profit"] >= 0]
        .sort_values("Profit")
        .head(5)
    )

    lines = [
        "# Superstore Sales and Profit Analysis",
        "",
        "## 1. Executive Summary",
        f"- Total sales: ${total_sales:,.2f}",
        f"- Total profit: ${total_profit:,.2f}",
        f"- Overall profit margin: {overall_margin:.2f}%",
        "",
        "## 2. Category Performance",
        f"- Highest-profit category: {best_category['Category']}",
        f"- Category profit: ${best_category['Profit']:,.2f}",
        "",
        "## 3. Customer Segment Analysis",
        f"- Highest-profit segment: {best_segment['Segment']}",
        f"- Segment profit: ${best_segment['Profit']:,.2f}",
        "",
        "## 4. Monthly Sales Trends",
        f"- Highest-sales month: {best_month['Order Date']}",
        f"- Sales in that month: ${best_month['Sales']:,.2f}",
        "",
        "## 5. Loss-Making Subcategories",
        ""
    ]

    if loss_making.empty:
        lines.append("No subcategories have negative total profit.")
    else:
        for _, row in loss_making.iterrows():
            lines.append(
                f"- **{row['Sub-Category']}**: "
                f"profit ${row['Profit']:,.2f}, "
                f"margin {row['Profit Margin (%)']:.2f}%"
            )

    lines.extend([
        "",
        "## 6. Lowest Positive-Profit Subcategories",
        ""
    ])

    if low_positive_profit.empty:
        lines.append("No subcategories have non-negative profit.")
    else:
        for _, row in low_positive_profit.iterrows():
            lines.append(
                f"- **{row['Sub-Category']}**: "
                f"profit ${row['Profit']:,.2f}, "
                f"margin {row['Profit Margin (%)']:.2f}%"
            )

    lines.extend([
        "",
        "## 7. Business Recommendations",
        "- Investigate pricing, discounting, and costs for loss-making subcategories.",
        "- Review Furniture performance because its profit is low relative to sales.",
        "- Examine the drivers of strong Copier and Paper profitability before expanding inventory.",
        "- Use monthly sales patterns to support inventory and promotional planning.",
        "- Continue monitoring customer segments by both sales and profit.",
        "",
        "## 8. Limitations",
        "- This is descriptive analysis and does not establish causal relationships.",
        "- Potential outliers were flagged but were not automatically removed.",
        "- Further investigation is needed to explain losses and margin differences."
    ])

    output_path = REPORTS_DIR / "business_insights.md"
    output_path.write_text("\n".join(lines) + "\n", encoding="utf-8")

    print(f"Business report saved to: {output_path}")
    print("\n".join(lines))


if __name__ == "__main__":
    create_report()