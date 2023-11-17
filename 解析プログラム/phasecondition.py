import pandas as pd
from tqdm import trange, tqdm
import glob
import os
from natsort import natsorted

os.makedirs("phase3_1/condition2"+ "/", exist_ok = True)
os.makedirs("phase3_2/condition2"+ "/", exist_ok = True)
os.makedirs("phase3_3/condition2"+ "/", exist_ok = True)
os.makedirs("phase3_4/condition2"+ "/", exist_ok = True)

os.makedirs("phase3_1/condition3"+ "/", exist_ok = True)
os.makedirs("phase3_2/condition3"+ "/", exist_ok = True)
os.makedirs("phase3_3/condition3"+ "/", exist_ok = True)
os.makedirs("phase3_4/condition3"+ "/", exist_ok = True)

os.makedirs("phase3_1/condition4"+ "/", exist_ok = True)
os.makedirs("phase3_2/condition4"+ "/", exist_ok = True)
os.makedirs("phase3_3/condition4"+ "/", exist_ok = True)
os.makedirs("phase3_4/condition4"+ "/", exist_ok = True)

os.makedirs("phase3_1/condition5"+ "/", exist_ok = True)
os.makedirs("phase3_2/condition5"+ "/", exist_ok = True)
os.makedirs("phase3_3/condition5"+ "/", exist_ok = True)
os.makedirs("phase3_4/condition5"+ "/", exist_ok = True)

os.makedirs("phase3_1/condition6"+ "/", exist_ok = True)
os.makedirs("phase3_2/condition6"+ "/", exist_ok = True)
os.makedirs("phase3_3/condition6"+ "/", exist_ok = True)
os.makedirs("phase3_4/condition6"+ "/", exist_ok = True)

os.makedirs("phase3_1/condition7"+ "/", exist_ok = True)
os.makedirs("phase3_2/condition7"+ "/", exist_ok = True)
os.makedirs("phase3_3/condition7"+ "/", exist_ok = True)
os.makedirs("phase3_4/condition7"+ "/", exist_ok = True)

os.makedirs("phase3_1/condition8"+ "/", exist_ok = True)
os.makedirs("phase3_2/condition8"+ "/", exist_ok = True)
os.makedirs("phase3_3/condition8"+ "/", exist_ok = True)
os.makedirs("phase3_4/condition8"+ "/", exist_ok = True)

os.makedirs("phase3_1/condition9"+ "/", exist_ok = True)
os.makedirs("phase3_2/condition9"+ "/", exist_ok = True)
os.makedirs("phase3_3/condition9"+ "/", exist_ok = True)
os.makedirs("phase3_4/condition9"+ "/", exist_ok = True)

os.makedirs("phase3_1/condition10"+ "/", exist_ok = True)
os.makedirs("phase3_2/condition10"+ "/", exist_ok = True)
os.makedirs("phase3_3/condition10"+ "/", exist_ok = True)
os.makedirs("phase3_4/condition10"+ "/", exist_ok = True)

files = glob.glob("phase3_1/*.csv")
print("phase3_1")
for file in tqdm(natsorted(files)):

    df = pd.read_csv(file)
    split_name = file.split("_", 4)

    if split_name[2] =="2":
        new_file = "phase3_1/condition2/" + file.replace("phase3_1\\", "")
        df.to_csv(new_file, index = None)

    if split_name[2] =="3":
        new_file = "phase3_1/condition3/" + file.replace("phase3_1\\", "")
        df.to_csv(new_file, index = None)

    if split_name[2] =="4":
        new_file = "phase3_1/condition4/" + file.replace("phase3_1\\", "")
        df.to_csv(new_file, index = None)

    if split_name[2] =="5":
        new_file = "phase3_1/condition5/" + file.replace("phase3_1\\", "")
        df.to_csv(new_file, index = None)

    if split_name[2] =="6":
        new_file = "phase3_1/condition6/" + file.replace("phase3_1\\", "")
        df.to_csv(new_file, index = None)

    if split_name[2] =="7":
        new_file = "phase3_1/condition7/" + file.replace("phase3_1\\", "")
        df.to_csv(new_file, index = None)

    if split_name[2] =="8":
        new_file = "phase3_1/condition8/" + file.replace("phase3_1\\", "")
        df.to_csv(new_file, index = None)

    if split_name[2] =="9":
        new_file = "phase3_1/condition9/" + file.replace("phase3_1\\", "")
        df.to_csv(new_file, index = None)

    if split_name[2] =="10":
        new_file = "phase3_1/condition10/" + file.replace("phase3_1\\", "")
        df.to_csv(new_file, index = None)

files = glob.glob("phase3_2/*.csv")
print("phase3_2")
for file in tqdm(natsorted(files)):

    df = pd.read_csv(file)
    split_name = file.split("_", 4)

    if split_name[2] =="2":
        new_file = "phase3_2/condition2/" + file.replace("phase3_2\\", "")
        df.to_csv(new_file, index = None)

    if split_name[2] =="3":
        new_file = "phase3_2/condition3/" + file.replace("phase3_2\\", "")
        df.to_csv(new_file, index = None)

    if split_name[2] =="4":
        new_file = "phase3_2/condition4/" + file.replace("phase3_2\\", "")
        df.to_csv(new_file, index = None)

    if split_name[2] =="5":
        new_file = "phase3_2/condition5/" + file.replace("phase3_2\\", "")
        df.to_csv(new_file, index = None)

    if split_name[2] =="6":
        new_file = "phase3_2/condition6/" + file.replace("phase3_2\\", "")
        df.to_csv(new_file, index = None)

    if split_name[2] =="7":
        new_file = "phase3_2/condition7/" + file.replace("phase3_2\\", "")
        df.to_csv(new_file, index = None)

    if split_name[2] =="8":
        new_file = "phase3_2/condition8/" + file.replace("phase3_2\\", "")
        df.to_csv(new_file, index = None)

    if split_name[2] =="9":
        new_file = "phase3_2/condition9/" + file.replace("phase3_2\\", "")
        df.to_csv(new_file, index = None)

    if split_name[2] =="10":
        new_file = "phase3_2/condition10/" + file.replace("phase3_2\\", "")
        df.to_csv(new_file, index = None)

files = glob.glob("phase3_3/*.csv")
print("phase3_3")
for file in tqdm(natsorted(files)):

    df = pd.read_csv(file)
    split_name = file.split("_", 4)

    if split_name[2] =="2":
        new_file = "phase3_3/condition2/" + file.replace("phase3_3\\", "")
        df.to_csv(new_file, index = None)

    if split_name[2] =="3":
        new_file = "phase3_3/condition3/" + file.replace("phase3_3\\", "")
        df.to_csv(new_file, index = None)

    if split_name[2] =="4":
        new_file = "phase3_3/condition4/" + file.replace("phase3_3\\", "")
        df.to_csv(new_file, index = None)

    if split_name[2] =="5":
        new_file = "phase3_3/condition5/" + file.replace("phase3_3\\", "")
        df.to_csv(new_file, index = None)

    if split_name[2] =="6":
        new_file = "phase3_3/condition6/" + file.replace("phase3_3\\", "")
        df.to_csv(new_file, index = None)

    if split_name[2] =="7":
        new_file = "phase3_3/condition7/" + file.replace("phase3_3\\", "")
        df.to_csv(new_file, index = None)

    if split_name[2] =="8":
        new_file = "phase3_3/condition8/" + file.replace("phase3_3\\", "")
        df.to_csv(new_file, index = None)

    if split_name[2] =="9":
        new_file = "phase3_3/condition9/" + file.replace("phase3_3\\", "")
        df.to_csv(new_file, index = None)

    if split_name[2] =="10":
        new_file = "phase3_3/condition10/" + file.replace("phase3_3\\", "")
        df.to_csv(new_file, index = None)

files = glob.glob("phase3_4/*.csv")
print("phase3_4")
for file in tqdm(natsorted(files)):

    df = pd.read_csv(file)
    split_name = file.split("_", 4)

    if split_name[2] =="2":
        new_file = "phase3_4/condition2/" + file.replace("phase3_4\\", "")
        df.to_csv(new_file, index = None)

    if split_name[2] =="3":
        new_file = "phase3_4/condition3/" + file.replace("phase3_4\\", "")
        df.to_csv(new_file, index = None)

    if split_name[2] =="4":
        new_file = "phase3_4/condition4/" + file.replace("phase3_4\\", "")
        df.to_csv(new_file, index = None)

    if split_name[2] =="5":
        new_file = "phase3_4/condition5/" + file.replace("phase3_4\\", "")
        df.to_csv(new_file, index = None)

    if split_name[2] =="6":
        new_file = "phase3_4/condition6/" + file.replace("phase3_4\\", "")
        df.to_csv(new_file, index = None)

    if split_name[2] =="7":
        new_file = "phase3_4/condition7/" + file.replace("phase3_4\\", "")
        df.to_csv(new_file, index = None)

    if split_name[2] =="8":
        new_file = "phase3_4/condition8/" + file.replace("phase3_4\\", "")
        df.to_csv(new_file, index = None)

    if split_name[2] =="9":
        new_file = "phase3_4/condition9/" + file.replace("phase3_4\\", "")
        df.to_csv(new_file, index = None)

    if split_name[2] =="10":
        new_file = "phase3_4/condition10/" + file.replace("phase3_4\\", "")
        df.to_csv(new_file, index = None)