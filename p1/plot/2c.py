import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# CSVファイルを読み込む
df = pd.read_csv('/Users/nishiyamamizuki/plauground/p1/2c/apf.csv')

# 理論的な関数を定義
def func_apf(t, R, C, V):
    T = R * C
    return 1  # 実際の計算式に置き換える必要があります

# 理論値を計算
time_theory = np.linspace(df['w'].min(), df['w'].max(), 500)
voltage_theory = func_apf(time_theory, 998.5, 93.32*10**-9, 2)

# 点と理論曲線をプロット
plt.figure(figsize=(10, 5))
plt.scatter(df['w'], df['H'], color='blue', label='Experimental Data', s=12)
plt.plot(time_theory, np.ones_like(time_theory), color='red', label='Theoretical Curve')

# 近似直線をプロット
# 対数スケールでのフィッティングのために、xデータを対数に変換
log_w = np.log(df['w'])
# 1次の多項式フィットを行う
coefficients = np.polyfit(log_w, df['H'], 1)
# フィットした多項式から近似値を生成
approximation = np.polyval(coefficients, log_w)
# 対数スケールのxデータをもとに戻してプロット
plt.plot(df['w'], approximation, color='blue', label='Fitted Line')

# タイトルと軸のラベルを設定
plt.xlabel('w (rad/s)')
plt.ylabel('|H| (dB)')
plt.legend()  # 凡例を表示
plt.xscale('log')
plt.ylim(-0.5, 2)

# グラフを表示
plt.show()
