import numpy as np
import time
import matplotlib.pyplot as plt

def measure_time(op, repeat=1000):
    start = time.perf_counter()
    for _ in range(repeat):
        op()
    end = time.perf_counter()
    return (end - start) / repeat

sizes = np.logspace(3, 7, num=20, dtype=int)  # Sizes from 1KB to ~10MB
row_perf = []
col_perf = []
row_size_kb = []
col_size_kb = []

for SIZE in sizes:
    mat = np.random.rand(SIZE, SIZE)

    row_time = measure_time(lambda: 2 * mat[0, :])
    col_time = measure_time(lambda: 2 * mat[:, 0])

    num_ops = SIZE  # One multiply per element

    row_perf.append((num_ops / row_time) / 1e6)  # MFLOP/s
    col_perf.append((num_ops / col_time) / 1e6)

    row_size_kb.append(mat[0, :].nbytes / 1024)
    col_size_kb.append(mat[:, 0].nbytes / 1024)

# Save to file for plotting
np.savez("cache_perf_data.npz", row_perf=row_perf, col_perf=col_perf,
         row_size_kb=row_size_kb, col_size_kb=col_size_kb)
