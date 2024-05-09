import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# CSVファイルを読み込む
df = pd.read_csv('/Users/nishiyamamizuki/plauground/p1/1a/abcy.csv')
c_1 = 'w'
c_2 = 'measured_value'
c_3 = 'theoretical_value'

# 点をプロット
plt.figure(figsize=(10, 5))
plt.scatter(df[c_1], df[c_2], color='red', label='measured_value', s=8)
plt.scatter(df[c_1], df[c_3], color='blue', label='theoretical_value', s=8)
# 横軸を対数スケールに設定
plt.xscale('log')

# タイトルと軸のラベルを設定
plt.xlabel('w(rad/s)')
plt.ylabel('|Y|(1/Ω)')
plt.legend()  # 凡例を表示

# グラフを表示
plt.show()
