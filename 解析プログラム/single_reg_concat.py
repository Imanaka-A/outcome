#single_regression_analyを使用後に用いる
#算出した値をcsvの後ろに結合できる


import pandas as pd
import glob
import os
from natsort import natsorted
from tqdm import trange, tqdm

os.makedirs("after/", exist_ok = True)

files = glob.glob("raw/*.csv")

position1 = "RUlna"
position2 = "RRadius"
#ULna
Xa = 0.99894317
Xb = -0.08940948
Ya = 0.85890341
Yb = 0.15504923
Za = 0.77482297
Zb = 0.07145345

#Radius
xa = 0.99165389
xb = -0.06361618
ya = 0.86966047
yb = 0.13706182
za = 0.88998471
zb = -0.02419595


for file in tqdm(natsorted(files)): 
    df = pd.read_csv(file)
    df_1 = df.fillna(0)
    
    #ULna
    X = Xa * df_1["Body_RHand_Position_X"] + Xb
    Y = Ya * df_1["Body_RHand_Position_Y"] + Yb
    Z = Za * df_1["Body_RHand_Position_Z"] + Zb
    #Radius
    x = xa * df_1["Body_RHand_Position_X"] + xb
    y = ya * df_1["Body_RHand_Position_Y"] + yb
    z = za * df_1["Body_RHand_Position_Z"] + zb

    POSITION = pd.DataFrame({"Body_" + position1 + "_Position_X":X,
                            "Body_" + position1 + "_Position_Y":Y,
                            "Body_" + position1 + "_Position_Z":Z,
                            "Body_" + position2 + "_Position_X":x,
                            "Body_" + position2 + "_Position_Y":y,
                            "Body_" + position2 + "_Position_Z":z})

    new_df = pd.concat([df, POSITION], axis = 1)                        

    new_file = "after/" + file.replace("raw\\","")

    new_df.to_csv(new_file, index = None )