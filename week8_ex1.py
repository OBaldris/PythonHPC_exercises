import sys
import pandas as pd

def main():
    path = sys.argv[1]
    chunksize = int(sys.argv[2])
    total = 0.0

    for chunk in pd.read_csv(path, chunksize=chunksize):
        # Use actual parameterId value for precipitation
        precip = chunk[chunk['parameterId'] == 'precip_past1h']
        total += precip['value'].sum()

    print(total)

if __name__ == "__main__":
    main()
