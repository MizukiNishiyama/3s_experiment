import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# CSVファイルを読み込む
df = pd.read_csv('/Users/nishiyamamizuki/plauground/p1/2a/lpf_abch.csv')
c_1 = 'w'
c_2 = 'c1'

def func_lpf_abc(w, R, C):
    T = R*C
    return 20*np.log10(1 / np.sqrt(1 + T**2 * w**2))
w_theory = np.linspace(628, df['w'].max(), 500)
abc_theory = func_lpf_abc(w_theory, 998.5, 93.32*10**-9)
# 点をプロット
plt.figure(figsize=(10, 5))
plt.scatter(df[c_1], df[c_2], color='blue', label='measured value', s=12)
plt.plot(w_theory, abc_theory, color='red', label='Theoretical Curve')  # 理論曲線をプロット

# 横軸を対数スケールに設定
plt.xscale('log')


# タイトルと軸のラベルを設定
plt.xlabel('w(rad/s)')
plt.ylabel('|H|(dB)')
plt.legend()  # 凡例を表示

# グラフを表示
plt.show()
