import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# CSVファイルを読み込む
df = pd.read_csv('/Users/nishiyamamizuki/plauground/p1/1a/arg_y.csv')

def rlc(w, R, C, L):
    return - np.arctan(((w*L-(1/(w*C))) / R)) * 180 / np.pi
w_theory = np.linspace(df['w'].min(), df['w'].max(), 500)
abc_theory = rlc(w_theory, 29.91, 4.49*10**-10, 4.46*10**-5)
# 点をプロット
plt.figure(figsize=(10, 5))
plt.scatter(df['w'], df['arg'], color='blue', label='measured value', s=12)
plt.plot(w_theory, abc_theory, color='red', label='Theoretical Curve')  # 理論曲線をプロット

# 横軸を対数スケールに設定
plt.xscale('log')

# タイトルと軸のラベルを設定
plt.xlabel('w(rad/s)')
plt.ylabel('argY(deg)')
plt.legend()  # 凡例を表示

# グラフを表示
plt.show()
