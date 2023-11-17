#MotiveとRobotの時間同期
##実験手順のミスで，Motiveを最後に起動した際に使用する

import pandas as pd
from tqdm import trange, tqdm
import os

#サンプリング数
OPTITRACK_SAMPLING_RATE = 200
ROBOT_SAMPLING_RATE = 100

filename = "o_" #ファイル名

file_num = 6 #ファイル数 + 1

condition_num = 11 #条件数 + 1

for k in tqdm(range(2, condition_num)):

    condition = str(k)
    
    for i in tqdm(range(1, file_num)):

        df_position = pd.read_csv("motive/" + filename + condition + "_" + str(i) + ".csv")
        df_robot = pd.read_csv("robot/" + filename + condition + "_" + str(i) + ".csv")
        print( "処理中ファイル", filename + condition + "_" + str(i))

        #MOTIVEでLEDが消えた時間を算出
        df_position_LED = df_position["LED_LED_Position_X"]
        df_position_LED = df_position_LED.fillna(0) #空欄(消えている時間)を0にする
        list_position_LED = df_position_LED.values.tolist() #リスト化
        end_position_LED = list_position_LED.index(min(list_position_LED)) #0(消えた瞬間)が何番目か
        end_position_LED_time = end_position_LED / OPTITRACK_SAMPLING_RATE #消えた時間

        #robotの計測終了を算出
        df_robot_count = df_robot["time[s]"] .count() #データ数を数える
        end_robot_time = (df_robot_count - 1) / ROBOT_SAMPLING_RATE #終了時間

        GAP = int((end_robot_time - end_position_LED_time) * ROBOT_SAMPLING_RATE) #robotとMOTIVEの時間差,サンプリング周波数違うから整数化して妥協
        print(GAP)

        #robotデータを整形    
        df_robot = df_robot.drop(range(GAP)) #GAP時間差だけデータをスキップ
        df_robot = df_robot.drop(columns = ["time[s]"]) #時間をリセット
        
        #時間軸を追加
        offset_time = []
        for step in range(len(df_robot)):
            offset_time.append(step / ROBOT_SAMPLING_RATE)

        df_robot.insert(1, "time[s]", offset_time, True)

        #csv出力
        df_robot.to_csv("adjusted_robot/" + filename + condition + "_" + str(i) + ".csv")