#データの試行数を1~4の連番にする
#解析用csvの際に使用する

import pandas as pd
import glob
import os
from tqdm import trange, tqdm
from natsort import natsorted

#変更するファイル
task = "position"

os.makedirs("after_" + task + "/", exist_ok = True)
files = glob.glob(task + "/*.csv")

for i, file in tqdm(enumerate(natsorted(files), 1)):
    df = pd.read_csv(file)
    split_name = file.split("_",3)
    mod = i % 4

    if mod == 1:
        new = file.replace(split_name[2], "1").replace(task + "\\", "") + ".csv"

    if mod == 2:
        new = file.replace(split_name[2], "2").replace(task + "\\", "") + ".csv"

    if mod == 3:
        new = file.replace(split_name[2], "3").replace(task + "\\", "") + ".csv"

    if mod == 0:
        new = file.replace(split_name[2], "4").replace(task + "\\", "") + ".csv"

    new_file = "after_" + task + "/"+ new
    df.to_csv(new_file, index = None)
print("終了")