import numpy as np
import pandas as pd

data = [10,25,64,35,40,7,55]

std_dev_numpy = np.std(data)
print("Standard Deviation using NumPy: ", std_dev_numpy)

df = pd.DataFrame({'values': data})
std_dev_pandas = df['values'].std()
print("Standard Deviation using Pandas: ", std_dev_pandas)