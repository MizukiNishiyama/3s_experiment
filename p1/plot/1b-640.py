import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# CSVファイルを読み込む
df = pd.read_csv('/Users/nishiyamamizuki/plauground/p1/1b/640.csv')

# 理論的な関数を定義
def func_640(t, R, L, C, V):
    a = R / (2 * L)
    b = np.sqrt((R / (2 * L)) ** 2 - 1 / (L * C))
    return R * np.exp(-a * t) * V * t / L

# 理論値を計算
time_theory = np.linspace(0, df['time'].max(), 500)
voltage_theory = func_640(time_theory, 640, 46.6 * 10**-6, 449 * 10**-12, 4.8)

# 点と理論曲線をプロット
plt.figure(figsize=(10, 5))
plt.scatter(df['time'], df['volt'], color='blue', label='Experimental Data', s=8)
plt.plot(time_theory, voltage_theory, color='red', label='Theoretical Curve')  # 理論曲線をプロット

# タイトルと軸のラベルを設定

plt.xlabel('Time (s)')
plt.ylabel('Voltage (V)')
plt.legend()  # 凡例を表示

# グラフを表示
plt.show()
