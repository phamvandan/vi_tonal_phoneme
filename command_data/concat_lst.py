import pandas as pd
import os
import sys
import re
# from sklearn.utils import shuffle
""" .lst dir save dir"""
lst_dir = sys.argv[1]
save_dir = sys.argv[2]
filenames = []
for path, subdirs, files in os.walk(lst_dir):
    for name in files:
        if ".lst" in name:
            filenames.append(name)
print("len(filenames)", len(filenames))
if not os.path.exists(save_dir):
    os.mkdir(save_dir)
f_command = open(os.path.join(save_dir, "command.lst"), "w+")
train_idx = 0
for filename in filenames:
    print("PROCESS", filename)
    f_lst = open(os.path.join(lst_dir, filename))
    lines = f_lst.readlines()
    length = len(lines)
    for line in lines:
        elements = line.split("\t")
        print(elements)
        if not os.path.exists(elements[1]):
            print("skip")
            continue
        break
    break
        # elements[0] = "train_" + str(train_idx)
        # line = "\t".join(elements)
        # f_command.write(line)
        # train_idx += 1
print("train_idx", train_idx)