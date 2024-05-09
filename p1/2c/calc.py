import pandas as pd

# 処理するファイル番号のリスト
file_numbers = [100, 200, 500, 1000, 1200, 1500, 1700, 2000, 2200, 2500, 3000, 4000, 5000]

for number in file_numbers:
    # ファイルパスを生成
    v1_path = f'data/{number}_v1.csv'
    v1_path_a = f'data/{number}_v1_a.csv'
    v2_path = f'data/{number}_v2.csv'
    
    # v2 CSVファイルを読み込む
    df_v2 = pd.read_csv(v2_path)
    
    # CH1とCH2の差を計算
    df_v2['CH1'] = pd.to_numeric(df_v2['CH1'], errors='coerce')
    df_v2['CH2'] = pd.to_numeric(df_v2['CH2'], errors='coerce')
    df_v2['CH3'] = df_v2['CH1'] - df_v2['CH2']
    
    # v1 CSVファイルを読み込む
    df_v1 = pd.read_csv(v1_path)
    
    # 新しいカラムをv1データフレームに追加
    df_v1['CH3'] = df_v2['CH3']
    
    # CH2カラムを削除
    if 'CH2' in df_v1.columns:
        df_v1.drop('CH2', axis=1, inplace=True)
    
    # 結果をCSVファイルに保存
    df_v1.to_csv(v1_path_a, index=False)
