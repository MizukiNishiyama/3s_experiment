import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# CSVファイルを読み込む
df = pd.read_csv('/Users/nishiyamamizuki/playground/a1/1/a1.csv')

# 理論的な関数を定義
def func(I_s,q,V,k,T):
    return I_s*(np.exp(q*V/(k*T))-1)

# 理論値を計算
v_theory = np.linspace(0, df['補正電圧(V)'].max(), 500)
i_theory = func(0.0000, 1.6*10**(-19), v_theory,1.38*10**(-23), 292)

# 点と理論曲線をプロット
plt.figure(figsize=(10, 5))
plt.scatter(df['補正電圧(V)'], df['測定電流(uA)'], color='blue', label='Processed Experimental Data', s=8)
plt.scatter(df['補正電圧(内部抵抗考慮なし)(V)'], df['測定電流(uA)'], color='green', label='Raw Experimental Data', s=8)
plt.plot(v_theory, i_theory, color='red', label='Theoretical Curve')  # 理論曲線をプロット

## 縦軸を対数にする
plt.yscale('log')
plt.xlabel('V (V)')
plt.ylabel('I(μA)')
plt.legend()  # 凡例を表示

# グラフを表示
plt.show()
