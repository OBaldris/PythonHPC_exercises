import numpy as np
import matplotlib.pyplot as plt

data = np.load("cache_perf_data.npz")
row_perf = data["row_perf"]
col_perf = data["col_perf"]
row_size_kb = data["row_size_kb"]
col_size_kb = data["col_size_kb"]

plt.figure()
plt.loglog(row_size_kb, row_perf, label="Row Doubling")
plt.loglog(col_size_kb, col_perf, label="Column Doubling")
plt.xlabel("Data size (KB)")
plt.ylabel("MFLOP/s")
plt.legend()
plt.grid(True)
plt.title("Cache Performance: Row vs. Column Doubling")
plt.savefig("row_vs_col_perf.png")

# Ratio plot
plt.figure()
plt.loglog(row_size_kb, np.array(row_perf) / np.array(col_perf))
plt.xlabel("Data size (KB)")
plt.ylabel("Row / Column MFLOP/s")
plt.grid(True)
plt.title("Row/Column Performance Ratio")
plt.savefig("performance_ratio.png")
