# -*- coding: utf-8 -*-
import pandas as pd
import os, sys, re

""" .lst dir save dir"""
dir = sys.argv[1]
save_dir = sys.argv[2]
if not os.path.exists(save_dir):
    os.mkdir(save_dir)

filenames = os.listdir(dir)
characters = []
lexicons = []
vocab = set()
count_sentence = 0
for filename in filenames:
    print("PROCESS", filename)
    f = open(os.path.join(dir, filename))
    while True:
        sentence = f.readline().replace("\n", "")
        if sentence == "":
            break
        sentence = sentence.split("\t")[3]
        sentence = sentence.split()
        for lx in sentence:
            if len(lx)==0:
                continue
            vocab.add(lx)
        count_sentence += 1
        if count_sentence % 3000==0:
            print("--processed:", count_sentence, "--current file:", filename)
    f.close()
f_save = open(os.path.join(save_dir, "vocab.txt"), "w+")
f_save.write("\t".join(list(vocab)))
