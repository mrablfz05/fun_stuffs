import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time

# -------------CONFIG-------------
n = 70000000
random_number = np.random.randint(0, 1000000, size=n)

# -------------Python-------------
py_list = random_number.tolist()
start_py = time.time()
sorted_py = sorted(py_list)
end_py = time.time()
py_time = end_py - start_py


# -------------Numpy-------------
np_array = random_number.copy()
start_np = time.time()
sorted_np = np_array.sort()
end_np = time.time()
np_time = end_np - start_np


# -------------Pandas-------------
df = pd.DataFrame({"numbers": random_number.copy()})
start_pd = time.time()
sorted_df = df.sort_values("numbers")
end_pd = time.time()
pd_time = end_pd - start_pd


# ---------- RESULTS ----------
print(f"🐍 Built-in sorted() time: {py_time:.4f} sec")
print(f"📦 NumPy np.sort() time: {np_time:.4f} sec")
print(f"🐼 Pandas sort_values() time: {pd_time:.4f} sec")

# ----------PLOT----------
methods = ["python sorted()", "numpy sort()", "pd sort_values()"]
times = [py_time, np_time, pd_time]
colors = ['#FFDD57', '#66CCFF', '#FF9999']
plt.figure(figsize=(8, 5))
plt.bar(methods, times, color=colors)
plt.title('Sorting Performance Comparison', fontsize=16)
plt.xlabel('Tools')
plt.ylabel('Execution Time (seconds)')
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()