import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# CSVファイルを読み込む
df = pd.read_csv('/Users/nishiyamamizuki/plauground/p1/2b/lpf-2.csv')

# 理論的な関数を定義
def func_lpf(t, R, C, V):
    T = R*C
    return 1 - V * np.exp(-t / T)

# 理論値を計算
time_theory = np.linspace(0, df['time'].max(), 500)
voltage_theory = func_lpf(time_theory, 998.5, 93.32*10**-9, 2)

# 点と理論曲線をプロット
plt.figure(figsize=(10, 5))
plt.scatter(df['time'], df['h'], color='blue', label='Experimental Data', s=8)
plt.plot(time_theory, voltage_theory, color='red', label='Theoretical Curve')  # 理論曲線をプロット

# タイトルと軸のラベルを設定

plt.xlabel('Time (s)')
plt.ylabel('s(t)(V)')
plt.legend()  # 凡例を表示

# グラフを表示
plt.show()
