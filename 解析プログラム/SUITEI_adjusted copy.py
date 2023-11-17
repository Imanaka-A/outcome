#ファイルをまとめて処理可能
#整形

import pandas as pd
import os
import glob

OFFSET_FRAMES = 5 #LEDの認識遅延
OPTITRACK_SAMPLING_RATE = 200 #[Hz]
os.makedirs("adjusted/", exist_ok=True)#データ保存用フォルダがなかったら作成する。
raw_position_files = glob.glob("raw/*.csv")

for file in raw_position_files:
        df_raw = pd.read_csv(file, skiprows = 2, header = None)

        #変数名格納用のリストを用意
        varNames_Modified = []

        #変数名だけのデータフレームを作成
        df_varNamesRaw = df_raw.iloc[1:5, 2:]

        #データフレームの要素から変数名を作成して，変数リストに格納する．
        for col in range(len(df_varNamesRaw.columns)):
                varName_Modified = str(df_varNamesRaw.iloc[0, col]) + "_" + str(df_varNamesRaw.iloc[2, col]) + "_" + str(df_varNamesRaw.iloc[3, col])
                varName_Modified = varName_Modified.replace(":", "_")
                varNames_Modified.append(varName_Modified)

        varNames_Modified.insert(0, "Time")

        #print(varNames_Modified)#変数リスト表示
        #print(len(varNames_Modified))#変数リストのサイズ

        df_mod = df_raw.iloc[5:, 1:]
        df_mod.columns = varNames_Modified
        df_mod = df_mod.reset_index(drop=True)#整形後データ完成
        data_name = file.replace("raw\\", "")
        new_data_name = "adjusted/" + data_name
        df_mod.to_csv(new_data_name, index = None)

files  = glob.glob("adjusted/*.csv")
for file in files:
        df_mod = pd.read_csv(file)
        row = 0
        list_led = df_mod["LED_LED_Position_X"].tolist()
        for row in range(1, len(df_mod)):
                if pd.notna(list_led[row - 1])==False and pd.notna(list_led[row])==True:
                #print(row)#点灯する瞬間
                        start_frames = (row - OFFSET_FRAMES)  #LEDの認識遅延より，5ステップ前のデータを採用する．

        for row in range(1, len(df_mod)):
                if pd.notna(list_led[row - 1])==True and pd.notna(list_led[row])==False:
                        stop_frames = (row - OFFSET_FRAMES)

        df_Split = df_mod.iloc[start_frames:stop_frames, 1:]
        df_Split = df_Split.reset_index(drop=True)

        offset_time = []
        for step in range(len(df_Split)):
                offset_time.append(step/OPTITRACK_SAMPLING_RATE)

        df_Split.insert(0, "Time[s]", offset_time, True)

        file_split = file
        df_Split.to_csv(file_split, index = True)

