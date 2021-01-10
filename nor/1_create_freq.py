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
frequency = {}
count_sentence = 0
for filename in filenames:
    print("PROCESS", filename)
    f = open(os.path.join(dir, filename))
    while True:
        sentence = f.readline().replace("\n", "")
        if sentence == "":
            break
        sentence = sentence.split("\t")[3]
        sentence = sentence.split(" ")
        for lx in sentence:
            if lx not in frequency:
                frequency[lx] = 1
            else:
                frequency[lx] += 1
        count_sentence += 1
        if count_sentence % 3000==0:
            print("--processed:", count_sentence, "--current file:", filename)
words = list(frequency.keys())
freqs = list(frequency.values())
# df = pd.read_csv("v_dict.csv")
# word_dicts = df["word"]
f_freq = open(os.path.join(save_dir, "freq.txt"), "w+")
for index, word in enumerate(words):
    f_freq.write(word + "\t" + str(freqs[index]) + "\n")
