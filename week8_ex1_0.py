import sys
import pandas as pd

def main():
    if len(sys.argv) != 2:
        print("Usage: python describe_dataset.py <path_to_csv>")
        sys.exit(1)

    path = sys.argv[1]
    df = pd.read_csv(path)

    print("=== Dataset Info ===")
    print(f"Shape: {df.shape[0]} rows × {df.shape[1]} columns\n")

    print("=== Column Types ===")
    print(df.dtypes, "\n")

    print("=== Summary Statistics (Numerical Columns) ===")
    print(df.describe(), "\n")

    print("=== Missing Values Per Column ===")
    print(df.isnull().sum())

if __name__ == "__main__":
    main()
