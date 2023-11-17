#データを条件/相フォルダで分ける

import pandas as pd
from tqdm import trange, tqdm
import glob
import os
from natsort import natsorted

os.makedirs("condition2/phase1", exist_ok = True)
os.makedirs("condition2/phase2", exist_ok = True)
os.makedirs("condition2/phase3_1", exist_ok = True)
os.makedirs("condition2/phase3_2", exist_ok = True)
os.makedirs("condition2/phase3_3", exist_ok = True)
os.makedirs("condition2/phase3_4", exist_ok = True)

os.makedirs("condition3/phase1", exist_ok = True)
os.makedirs("condition3/phase2", exist_ok = True)
os.makedirs("condition3/phase3_1", exist_ok = True)
os.makedirs("condition3/phase3_2", exist_ok = True)
os.makedirs("condition3/phase3_3", exist_ok = True)
os.makedirs("condition3/phase3_4", exist_ok = True)

os.makedirs("condition4/phase1", exist_ok = True)
os.makedirs("condition4/phase2", exist_ok = True)
os.makedirs("condition4/phase3_1", exist_ok = True)
os.makedirs("condition4/phase3_2", exist_ok = True)
os.makedirs("condition4/phase3_3", exist_ok = True)
os.makedirs("condition4/phase3_4", exist_ok = True)

os.makedirs("condition5/phase1", exist_ok = True)
os.makedirs("condition5/phase2", exist_ok = True)
os.makedirs("condition5/phase3_1", exist_ok = True)
os.makedirs("condition5/phase3_2", exist_ok = True)
os.makedirs("condition5/phase3_3", exist_ok = True)
os.makedirs("condition5/phase3_4", exist_ok = True)

os.makedirs("condition6/phase1", exist_ok = True)
os.makedirs("condition6/phase2", exist_ok = True)
os.makedirs("condition6/phase3_1", exist_ok = True)
os.makedirs("condition6/phase3_2", exist_ok = True)
os.makedirs("condition6/phase3_3", exist_ok = True)
os.makedirs("condition6/phase3_4", exist_ok = True)

os.makedirs("condition7/phase1", exist_ok = True)
os.makedirs("condition7/phase2", exist_ok = True)
os.makedirs("condition7/phase3_1", exist_ok = True)
os.makedirs("condition7/phase3_2", exist_ok = True)
os.makedirs("condition7/phase3_3", exist_ok = True)
os.makedirs("condition7/phase3_4", exist_ok = True)

os.makedirs("condition8/phase1", exist_ok = True)
os.makedirs("condition8/phase2", exist_ok = True)
os.makedirs("condition8/phase3_1", exist_ok = True)
os.makedirs("condition8/phase3_2", exist_ok = True)
os.makedirs("condition8/phase3_3", exist_ok = True)
os.makedirs("condition8/phase3_4", exist_ok = True)

os.makedirs("condition9/phase1", exist_ok = True)
os.makedirs("condition9/phase2", exist_ok = True)
os.makedirs("condition9/phase3_1", exist_ok = True)
os.makedirs("condition9/phase3_2", exist_ok = True)
os.makedirs("condition9/phase3_3", exist_ok = True)
os.makedirs("condition9/phase3_4", exist_ok = True)

os.makedirs("condition10/phase1", exist_ok = True)
os.makedirs("condition10/phase2", exist_ok = True)
os.makedirs("condition10/phase3_1", exist_ok = True)
os.makedirs("condition10/phase3_2", exist_ok = True)
os.makedirs("condition10/phase3_3", exist_ok = True)
os.makedirs("condition10/phase3_4", exist_ok = True)

files = glob.glob("phase1/*.csv")

print("phase1")
for file in tqdm(natsorted(files)):

    df = pd.read_csv(file)
    split_name = file.split("_", 4)

    if split_name[1] =="2":
        new_file = "condition2/phase1/" + file.replace("phase1\\", "")
        df.to_csv(new_file, index = None)

    if split_name[1] =="3":
        new_file = "condition3/phase1/" + file.replace("phase1\\", "")
        df.to_csv(new_file, index = None)

    if split_name[1] =="4":
        new_file = "condition4/phase1/" + file.replace("phase1\\", "")
        df.to_csv(new_file, index = None)

    if split_name[1] =="5":
        new_file = "condition5/phase1/" + file.replace("phase1\\", "")
        df.to_csv(new_file, index = None)

    if split_name[1] =="6":
        new_file = "condition6/phase1/" + file.replace("phase1\\", "")
        df.to_csv(new_file, index = None)

    if split_name[1] =="7":
        new_file = "condition7/phase1/" + file.replace("phase1\\", "")
        df.to_csv(new_file, index = None)

    if split_name[1] =="8":
        new_file = "condition8/phase1/" + file.replace("phase1\\", "")
        df.to_csv(new_file, index = None)

    if split_name[1] =="9":
        new_file = "condition9/phase1/" + file.replace("phase1\\", "")
        df.to_csv(new_file, index = None)

    if split_name[1] =="10":
        new_file = "condition10/phase1/" + file.replace("phase1\\", "")
        df.to_csv(new_file, index = None)

files = glob.glob("phase2/*.csv")
print("phase2")
for file in tqdm(natsorted(files)):

    df = pd.read_csv(file)
    split_name = file.split("_", 4)

    if split_name[1] =="2":
        new_file = "condition2/phase2/" + file.replace("phase2\\", "")
        df.to_csv(new_file, index = None)

    if split_name[1] =="3":
        new_file = "condition3/phase2/" + file.replace("phase2\\", "")
        df.to_csv(new_file, index = None)

    if split_name[1] =="4":
        new_file = "condition4/phase2/" + file.replace("phase2\\", "")
        df.to_csv(new_file, index = None)

    if split_name[1] =="5":
        new_file = "condition5/phase2/" + file.replace("phase2\\", "")
        df.to_csv(new_file, index = None)

    if split_name[1] =="6":
        new_file = "condition6/phase2/" + file.replace("phase2\\", "")
        df.to_csv(new_file, index = None)

    if split_name[1] =="7":
        new_file = "condition7/phase2/" + file.replace("phase2\\", "")
        df.to_csv(new_file, index = None)

    if split_name[1] =="8":
        new_file = "condition8/phase2/" + file.replace("phase2\\", "")
        df.to_csv(new_file, index = None)

    if split_name[1] =="9":
        new_file = "condition9/phase2/" + file.replace("phase2\\", "")
        df.to_csv(new_file, index = None)

    if split_name[1] =="10":
        new_file = "condition10/phase2/" + file.replace("phase2\\", "")
        df.to_csv(new_file, index = None)

files = glob.glob("phase3_1/*.csv")
print("phase3_1")
for file in tqdm(natsorted(files)):

    df = pd.read_csv(file)
    split_name = file.split("_", 4)

    if split_name[2] =="2":
        new_file = "condition2/phase3_1/" + file.replace("phase3_1\\", "")
        df.to_csv(new_file, index = None)

    if split_name[2] =="3":
        new_file = "condition3/phase3_1/" + file.replace("phase3_1\\", "")
        df.to_csv(new_file, index = None)

    if split_name[2] =="4":
        new_file = "condition4/phase3_1/" + file.replace("phase3_1\\", "")
        df.to_csv(new_file, index = None)

    if split_name[2] =="5":
        new_file = "condition5/phase3_1/" + file.replace("phase3_1\\", "")
        df.to_csv(new_file, index = None)

    if split_name[2] =="6":
        new_file = "condition6/phase3_1/" + file.replace("phase3_1\\", "")
        df.to_csv(new_file, index = None)

    if split_name[2] =="7":
        new_file = "condition7/phase3_1/" + file.replace("phase3_1\\", "")
        df.to_csv(new_file, index = None)

    if split_name[2] =="8":
        new_file = "condition8/phase3_1/" + file.replace("phase3_1\\", "")
        df.to_csv(new_file, index = None)

    if split_name[2] =="9":
        new_file = "condition9/phase3_1/" + file.replace("phase3_1\\", "")
        df.to_csv(new_file, index = None)

    if split_name[2] =="10":
        new_file = "condition10/phase3_1/" + file.replace("phase3_1\\", "")
        df.to_csv(new_file, index = None)

files = glob.glob("phase3_2/*.csv")
print("phase3_2")
for file in tqdm(natsorted(files)):

    df = pd.read_csv(file)
    split_name = file.split("_", 4)

    if split_name[2] =="2":
        new_file = "condition2/phase3_2/" + file.replace("phase3_2\\", "")
        df.to_csv(new_file, index = None)

    if split_name[2] =="3":
        new_file = "condition3/phase3_2/" + file.replace("phase3_2\\", "")
        df.to_csv(new_file, index = None)

    if split_name[2] =="4":
        new_file = "condition4/phase3_2/" + file.replace("phase3_2\\", "")
        df.to_csv(new_file, index = None)

    if split_name[2] =="5":
        new_file = "condition5/phase3_2/" + file.replace("phase3_2\\", "")
        df.to_csv(new_file, index = None)

    if split_name[2] =="6":
        new_file = "condition6/phase3_2/" + file.replace("phase3_2\\", "")
        df.to_csv(new_file, index = None)

    if split_name[2] =="7":
        new_file = "condition7/phase3_2/" + file.replace("phase3_2\\", "")
        df.to_csv(new_file, index = None)

    if split_name[2] =="8":
        new_file = "condition8/phase3_2/" + file.replace("phase3_2\\", "")
        df.to_csv(new_file, index = None)

    if split_name[2] =="9":
        new_file = "condition9/phase3_2/" + file.replace("phase3_2\\", "")
        df.to_csv(new_file, index = None)

    if split_name[2] =="10":
        new_file = "condition10/phase3_2/" + file.replace("phase3_2\\", "")
        df.to_csv(new_file, index = None)

files = glob.glob("phase3_3/*.csv")
print("phase3_3")
for file in tqdm(natsorted(files)):

    df = pd.read_csv(file)
    split_name = file.split("_", 4)

    if split_name[2] =="2":
        new_file = "condition2/phase3_3/" + file.replace("phase3_3\\", "")
        df.to_csv(new_file, index = None)

    if split_name[2] =="3":
        new_file = "condition3/phase3_3/" + file.replace("phase3_3\\", "")
        df.to_csv(new_file, index = None)

    if split_name[2] =="4":
        new_file = "condition4/phase3_3/" + file.replace("phase3_3\\", "")
        df.to_csv(new_file, index = None)

    if split_name[2] =="5":
        new_file = "condition5/phase3_3/" + file.replace("phase3_3\\", "")
        df.to_csv(new_file, index = None)

    if split_name[2] =="6":
        new_file = "condition6/phase3_3/" + file.replace("phase3_3\\", "")
        df.to_csv(new_file, index = None)

    if split_name[2] =="7":
        new_file = "condition7/phase3_3/" + file.replace("phase3_3\\", "")
        df.to_csv(new_file, index = None)

    if split_name[2] =="8":
        new_file = "condition8/phase3_3/" + file.replace("phase3_3\\", "")
        df.to_csv(new_file, index = None)

    if split_name[2] =="9":
        new_file = "condition9/phase3_3/" + file.replace("phase3_3\\", "")
        df.to_csv(new_file, index = None)

    if split_name[2] =="10":
        new_file = "condition10/phase3_3/" + file.replace("phase3_3\\", "")
        df.to_csv(new_file, index = None)

files = glob.glob("phase3_4/*.csv")
print("phase3_4")
for file in tqdm(natsorted(files)):

    df = pd.read_csv(file)
    split_name = file.split("_", 4)

    if split_name[2] =="2":
        new_file = "condition2/phase3_4/" + file.replace("phase3_4\\", "")
        df.to_csv(new_file, index = None)

    if split_name[2] =="3":
        new_file = "condition3/phase3_4/" + file.replace("phase3_4\\", "")
        df.to_csv(new_file, index = None)

    if split_name[2] =="4":
        new_file = "condition4/phase3_4/" + file.replace("phase3_4\\", "")
        df.to_csv(new_file, index = None)

    if split_name[2] =="5":
        new_file = "condition5/phase3_4/" + file.replace("phase3_4\\", "")
        df.to_csv(new_file, index = None)

    if split_name[2] =="6":
        new_file = "condition6/phase3_4/" + file.replace("phase3_4\\", "")
        df.to_csv(new_file, index = None)

    if split_name[2] =="7":
        new_file = "condition7/phase3_4/" + file.replace("phase3_4\\", "")
        df.to_csv(new_file, index = None)

    if split_name[2] =="8":
        new_file = "condition8/phase3_4/" + file.replace("phase3_4\\", "")
        df.to_csv(new_file, index = None)

    if split_name[2] =="9":
        new_file = "condition9/phase3_4/" + file.replace("phase3_4\\", "")
        df.to_csv(new_file, index = None)

    if split_name[2] =="10":
        new_file = "condition10/phase3_4/" + file.replace("phase3_4\\", "")
        df.to_csv(new_file, index = None)

print("終了")