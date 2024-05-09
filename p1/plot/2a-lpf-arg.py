import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# CSVファイルを読み込む
df = pd.read_csv('/Users/nishiyamamizuki/plauground/p1/2a/lpf_argh.csv')
c_1 = 'w'
c_2 = 'c1'
df['c3'] = -df['c1']

def func_lpf_arg(w, R, C):
    T = R*C
    return np.arctan(-T*w) * 180 / np.pi
w_theory = np.linspace(1256, df['w'].max(), 500)
abc_theory = func_lpf_arg(w_theory, 998.5, 93.32*10**-9)
# 点をプロット
plt.figure(figsize=(10, 5))
plt.scatter(df[c_1], df[c_2], color='blue', label='measured value', s=12)
plt.scatter(df[c_1], df['c3'], color='green', label='measured value * -1', s=12)
plt.plot(w_theory, abc_theory, color='red', label='Theoretical Curve')  # 理論曲線をプロット

# 横軸を対数スケールに設定
plt.xscale('log')


# タイトルと軸のラベルを設定
plt.xlabel('w(rad/s)')
plt.ylabel('argH(deg)')
plt.legend()  # 凡例を表示

# グラフを表示
plt.show()
