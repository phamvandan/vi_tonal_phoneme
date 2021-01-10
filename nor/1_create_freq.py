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
rs = []
for index, word in enumerate(words):
    rs.append([word, freqs[index]])
#     r = re.compile(word, re.IGNORECASE)
#     if any(r.match(str(w)) for w in word_dicts):
#         rs.append([word, freqs[index], "vi"])
#     else:
#         rs.append([word, freqs[index], "another"])

rs = sorted(rs, key=lambda x:x[1], reverse = True)
data = pd.DataFrame(rs, columns=["word", "freq"])
data.to_csv(os.path.join(save_dir, "freq.csv"))