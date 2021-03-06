# -*- coding: utf-8 -*-
import pandas as pd
import os, sys, re

""" .lst dir; save dir; mapping_table_dir"""
dir = sys.argv[1]
save_dir = sys.argv[2]
if not os.path.exists(save_dir):
    os.mkdir(save_dir)
mapping_table_dir = sys.argv[3]
f = open(os.path.join(mapping_table_dir, "mapping_table.txt"))
error_word = []
correct_word = []
while True:
    text_line = f.readline().replace("\n", "")
    if text_line == "":
        break
    components = text_line.split("\t")
    error_word.append(components[0])
    correct_word.append(components[1])
# error_word = list(pd.read_csv("./temp/error_dict.csv")["word"])
# correct_word = pd.read_csv("./temp/error_dict.csv")["decode"]

check_dict = zip(error_word, correct_word)

check_dict = dict(check_dict)

filenames = os.listdir(dir)
characters = []
lexicons = []
count_sentence = 0

for filename in filenames:
    print("PROCESS", filename)
    f = open(os.path.join(dir, filename))
    f_save = open(os.path.join(save_dir, filename), "w+")
    while True:
        sentence = f.readline().replace("\n", "")
        if sentence == "":
            break
        sentences = sentence.split("\t")
        sentence = sentences[3].split(" ")
        for index, lx in enumerate(sentence):
            if len(lx)==0:
                continue
            # if lx in words:
            sentence[index] = check_dict[lx]
        count_sentence += 1
        try:
            sentences[3] = " ".join(sentence)
        except:
            continue
        sentences = "\t".join(sentences)
        f_save.write(sentences + "\n")
        if count_sentence % 3000==0:
            print("--processed:", count_sentence, "--current file:", filename)
    f.close()
    f_save.close()

# pd.DataFrame(sorted(list(vocab)), columns=["word"]).to_csv(os.path.join(save_dir, "vocab.csv"))
