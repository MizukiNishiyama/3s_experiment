import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# CSVファイルを読み込む
df = pd.read_csv('/Users/nishiyamamizuki/plauground/p1/1b/30.csv')

def func_30(t, R, L, C, V):
    a = R / (2 * L)
    b = np.sqrt(1 / (L * C) - (R / (2 * L)) ** 2)
    return R * (V / (b * L)) * np.exp(-a * t) * np.sin(b * t)

# 理論値を計算
time_theory = np.linspace(0, df['time'].max(), 500)
voltage_theory = func_30(time_theory, 30, 46.6 * 10**-6, 449 * 10**-12, 4.8)

# 点と理論曲線をプロット
plt.figure(figsize=(10, 5))
plt.scatter(df['time'], df['volt'], color='blue', label='Experimental Data', s=8)
plt.plot(time_theory, voltage_theory, color='red', label='Theoretical Curve')  # 理論曲線をプロット

plt.xlabel('Time (s)')
plt.ylabel('Voltage (V)')
plt.legend()  # 凡例を表示
plt.xticks(np.arange(0, df['time'].max(), 5*10**-8))
# グラフを表示
plt.show()
