from pathlib import Path
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = PROJECT_ROOT / "data"
REPORTS_DIR = PROJECT_ROOT / "reports"


def clean_sales_data():
    csv_path = DATA_DIR / "Sample - Superstore.csv"
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)

    df = pd.read_csv(csv_path, encoding="cp1252")

    initial_rows = len(df)

    df["Order Date"] = pd.to_datetime(
        df["Order Date"], errors="coerce"
    )
    df["Ship Date"] = pd.to_datetime(
        df["Ship Date"], errors="coerce"
    )

    invalid_dates = df[
        df["Order Date"].isna() | df["Ship Date"].isna()
    ].shape[0]

    duplicate_rows = int(df.duplicated().sum())

    numeric_columns = [
        "Sales",
        "Quantity",
        "Discount",
        "Profit"
    ]

    for column in numeric_columns:
        df[column] = pd.to_numeric(
            df[column], errors="coerce"
        )

    missing_after_conversion = int(
        df[numeric_columns + ["Order Date", "Ship Date"]]
        .isna()
        .sum()
        .sum()
    )

    df = df.drop_duplicates().copy()

    df = df.dropna(
        subset=numeric_columns + ["Order Date", "Ship Date"]
    ).copy()

    df["Order Year"] = df["Order Date"].dt.year
    df["Order Month"] = df["Order Date"].dt.month
    df["Order Month Name"] = df["Order Date"].dt.strftime("%B")
    df["Order Year-Month"] = df["Order Date"].dt.to_period("M").astype(str)

    cleaned_path = DATA_DIR / "superstore_cleaned.csv"
    df.to_csv(cleaned_path, index=False)

    outlier_summary = {}

    for column in ["Sales", "Quantity", "Discount", "Profit"]:
        q1 = df[column].quantile(0.25)
        q3 = df[column].quantile(0.75)
        iqr = q3 - q1
        lower_bound = q1 - 1.5 * iqr
        upper_bound = q3 + 1.5 * iqr

        outlier_summary[column] = int(
            ((df[column] < lower_bound) |
             (df[column] > upper_bound)).sum()
        )

    report_lines = [
        "SUPERSTORE DATA CLEANING REPORT",
        "=" * 35,
        f"Initial rows: {initial_rows}",
        f"Exact duplicate rows found: {duplicate_rows}",
        f"Rows with invalid dates before cleaning: {invalid_dates}",
        f"Missing values after type conversion: {missing_after_conversion}",
        f"Rows after cleaning: {len(df)}",
        f"Rows removed: {initial_rows - len(df)}",
        "",
        "IQR outlier counts (flagged, not removed):"
    ]

    for column, count in outlier_summary.items():
        report_lines.append(f"{column}: {count}")

    report_path = REPORTS_DIR / "cleaning_report.txt"
    report_path.write_text(
        "\n".join(report_lines),
        encoding="utf-8"
    )

    print("\n".join(report_lines))
    print(f"\nCleaned dataset saved to: {cleaned_path}")
    print(f"Cleaning report saved to: {report_path}")

    return df


if __name__ == "__main__":
    clean_sales_data()