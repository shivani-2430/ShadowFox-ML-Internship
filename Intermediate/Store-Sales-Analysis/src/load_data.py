from pathlib import Path
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = PROJECT_ROOT / "data"


def load_sales_data():
    csv_path = DATA_DIR / "Sample - Superstore.csv"

    if not csv_path.exists():
        raise FileNotFoundError(
            f"Original dataset not found: {csv_path}"
        )

    df = pd.read_csv(csv_path, encoding="cp1252")

    print(f"Dataset: {csv_path.name}")
    print(f"Rows: {df.shape[0]}")
    print(f"Columns: {df.shape[1]}")
    print("\nColumn names:")
    print(df.columns.tolist())
    print("\nFirst five rows:")
    print(df.head())
    print("\nMissing values:")
    print(df.isnull().sum())

    return df


if __name__ == "__main__":
    load_sales_data()