# ==== Pandas vs Pure Python Matrix Operations ====
# This script compares statistical calculations and performance
# between Pandas and pure Python for a large random integer matrix.
# - Pandas: Uses DataFrame for stats and timing.
# - Pure Python: Uses nested lists and manual calculations.

#      .-"""-.
#     / .===. \
#     \/ 6 6 \/
#     ( \___/ )
# ___ooo__V__ooo___
# 🐼
import numpy as np
import pandas as pd
import time

rows = 1000000
cols = 170

np_matrix = np.random.randint(1, 100, size= (rows, cols))

start_pd = time.time()

df = pd.DataFrame(np_matrix)
pd_stats = {
    "mean": df.mean().mean(),
    "std": df.std().mean(),
    "min": df.min(),
    "max": df.max()
}

end_pd = time.time()
pd_time = end_pd - start_pd

# --------------------------
# 3. Pure Python Calculation
# --------------------------
#    /^\/^\ 
#    _|__|  O| 
# \/     /~  \ 
#  \____|____| 
#       \/     
#      /  \    
#     /    \   
#    /      \  
#   /        \ 
#  /          \
# 🐍

start_python = time.time()

data_list = np_matrix.tolist()
flattened = [item for sublist in data_list for item in sublist]

mean_py = sum(flattened) / len(flattened)
min_py = min(flattened)
max_py = max(flattened)
std_py = (sum((x - mean_py)**2 for x in flattened) / len(flattened))**0.5

python_stats = {
    'mean': mean_py,
    'std': std_py,
    'min': min_py,
    'max': max_py
}

end_python = time.time()
python_time = end_python - start_python

# --------------------------
# 4. Show Results
# --------------------------
print("📊 Pandas Stats:", pd_stats)
print("🐍 Python Stats:", python_stats)
print(f"⏱️ Pandas Time: {pd_time:.2f} sec")
print(f"⏱️ Pure Python Time: {python_time:.2f} sec")

# --------------------------
# 4. Show Results
# --------------------------
import matplotlib.pyplot as plt

times = [pd_time, python_time]
labels = ["Pandas", "Pure Python"]
colors = ["#1f77b4", "#ff7f0e"]

plt.figure(figsize=(6, 5))
plt.bar(labels, times, color=colors)
plt.xlabel("Method(for Matrix)")
plt.ylabel("Execution Time (seconds)")
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.show()


# =============================================================================
# 📝 Benchmark Report: Pandas vs Pure Python Matrix Stats
# -----------------------------------------------------------------------------
# Test Overview:
# - A 1,000,000 x 170 integer matrix was generated.
# - Statistical metrics (mean, std, min, max) were computed using both:
#     ▸ Pandas DataFrame methods
#     ▸ Pure Python list comprehensions and loops
#
# Results:
# - Execution Time (approx):
#     ▸ Pandas      : ⏱️ ~{pd_time:.2f} sec (for me 14 sec)
#     ▸ Pure Python : ⏱️ ~{python_time:.2f} sec (for me 80 sec)
#
# Key Observations:
# ✅ Pandas significantly outperformed pure Python in terms of runtime.
# ✅ Code with Pandas is more concise and readable for numerical operations.
# ⚠️ Pure Python becomes inefficient at high volumes due to lack of vectorization.
#
# Conclusion:
# For large-scale numeric data processing, especially when working with tabular 
# structures, Pandas is strongly preferred over nested lists or raw Python loops.
# However, learning both approaches is useful for understanding optimization trade-offs.
#
# Visualization:
# A simple bar plot was used to compare execution times visually.
# =============================================================================
