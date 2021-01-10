import pandas as pd
import os
import sys
import re
from sklearn.utils import shuffle
""" .lst dir save dir"""
lst_dir = sys.argv[1]
save_dir = sys.argv[2]
ratio = 0.8
if not os.path.exists(save_dir):
    os.mkdir(save_dir)
f_train = open(os.path.join(save_dir, "train.lst"), "w+")
f_test = open(os.path.join(save_dir, "test.lst"), "w+")
filenames = os.listdir(lst_dir)
train_idx = 0
test_idx = 0
for filename in filenames:
    print("PROCESS", filename)
    f_lst = open(os.path.join(lst_dir, filename))
    lines = f_lst.readlines()
    length = len(lines)
    index = shuffle(list(range(length)))
    train_idxs = index[:int(length*ratio)]
    test_idxs = index[int(length*ratio):]
    train_lines = [lines[i] for i in train_idxs]
    test_lines = [lines[i] for i in test_idxs]
    for line in train_lines:
        elements = line.split("\t")
        elements[0] = "train_" + str(train_idx)
        line = "\t".join(elements)
        f_train.write(line)
        train_idx += 1
    for line in test_lines:
        elements = line.split("\t")
        elements[0] = "test_" + str(test_idx)
        line = "\t".join(elements)
        f_test.write(line)
        test_idx += 1
    break
print(train_idx)
print(test_idx)