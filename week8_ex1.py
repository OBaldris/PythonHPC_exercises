import sys
import pandas as pd

def main():
    path = sys.argv[1]
    chunksize = int(sys.argv[2])
    total = 0.0

    for chunk in pd.read_csv(path, chunksize=chunksize):
        # Print columns for debugging (optional)
        # print(chunk.columns)

        # Auto-detect the precipitation column (if known, replace this with direct access)
        if 'precipitation' in chunk.columns:
            col = 'precipitation'
        elif 'Precipitation' in chunk.columns:
            col = 'Precipitation'
        else:
            # If column not found, raise an error
            raise ValueError("Precipitation column not found")

        # Convert to numeric to handle non-numeric entries, if any
        values = pd.to_numeric(chunk[col], errors='coerce')

        # Drop NaN and sum
        total += values.dropna().sum()

    print(total)

if __name__ == "__main__":
    main()
