import pandas as pd
import numpy as np

# 処理するファイル番号のリスト
numbers = [100,200, 500, 1000, 1200, 1500, 1700, 2000, 2200, 2500, 3000, 4000, 5000]

# 結果を格納するための空のデータフレーム
results_df = pd.DataFrame()

for number in numbers:
    # 入力ファイルパスを生成
    input_path = f'data/{number}_v1_a.csv'
    
    # CSVファイルを読み込む
    df = pd.read_csv(input_path)
    
    # CH1とCH3の最大値を求める
    max_CH1 = df['CH1'].max()
    max_CH3 = df['CH3'].max()
    
    # 最大値を用いてHを計算（0での除算を避けるために条件をチェック）
    if max_CH1 != 0 and not pd.isnull(max_CH1):
        H = max_CH3 / max_CH1
    else:
        H = np.nan  # CH1が0またはNaNの場合、HはNaN
    
    # 2*PI()*numberを計算
    w = 2 * np.pi * number
    
    # 結果をデータフレームに追加
    results_df = pd.concat([results_df, pd.DataFrame([{'number': number, 'H': H, 'w': w}])], ignore_index=True)

# 結果をCSVファイルに保存
results_df.to_csv('data/combined_results.csv', index=False)

print("Processing completed and results are saved in 'combined_results.csv'.")
