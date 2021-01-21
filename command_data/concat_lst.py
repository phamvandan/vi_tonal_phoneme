import pandas as pd
import os
import sys
import re
import json
# from sklearn.utils import shuffle

# root directory contain json file
lst_dir = sys.argv[1]
# directory for save json file
save_dir = sys.argv[2]



filenames = []
for path, subdirs, files in os.walk(lst_dir):
    for name in files:
        if ".lst" in name:
            filenames.append(name)
print("len(filenames)", len(filenames))
if not os.path.exists(save_dir):
    os.mkdir(save_dir)
f_command = open(os.path.join(save_dir, "command.json"), "w+")
train_idx = 0
data = {}

for filename in filenames:
    print("PROCESS", filename)
    f_lst = open(os.path.join(lst_dir, filename))
    lines = f_lst.readlines()
    length = len(lines)
    for line in lines:
        elements = line.split("\t")
        ## CHECK IF PATH OF THE AUDIO EXISTED
        if not os.path.exists(elements[1]):
            print("skip")
            continue
        data["audio_path"] = elements[1]
        data["duration"] = float(elements[2])
        data["text"] = elements[3]
        json.dump(data, f_command)
        f_command.write("\n")
        train_idx += 1
print("total sentence", train_idx)