#データを相フォルダに分ける

import pandas as pd
from tqdm import trange, tqdm
import glob
import os
from natsort import natsorted

os.makedirs("phase1/", exist_ok = True)
os.makedirs("phase2/", exist_ok = True)
os.makedirs("phase3_1/", exist_ok = True)
os.makedirs("phase3_2/", exist_ok = True)
os.makedirs("phase3_3/", exist_ok = True)
os.makedirs("phase3_4/", exist_ok = True)

files = glob.glob("position/*.csv")

for file in tqdm(natsorted(files)):

    df = pd.read_csv(file)
    split_name = file.split("_", 3)

    if split_name[3] =="phase1.csv":
        new_file = "phase1/" + file.replace("position\\", "")
        df.to_csv(new_file, index = None)

    if split_name[3] =="phase2.csv":
        new_file = "phase2/" + file.replace("position\\", "")
        df.to_csv(new_file, index = None)

    if split_name[3] =="phase3_1.csv":
        new_file = "phase3_1/" + file.replace("position\\", "")
        df.to_csv(new_file, index = None)

    if split_name[3] =="phase3_2.csv":
        new_file = "phase3_2/" + file.replace("position\\", "")
        df.to_csv(new_file, index = None)

    if split_name[3] =="phase3_3.csv":
        new_file = "phase3_3/" + file.replace("position\\", "")
        df.to_csv(new_file, index = None)

    if split_name[3] =="phase3_4.csv":
        new_file = "phase3_4/" + file.replace("position\\", "")
        df.to_csv(new_file, index = None)

print("終了")