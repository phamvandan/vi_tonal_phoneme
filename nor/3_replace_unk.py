import os
import multiprocessing

import pandas as pd
UNK = "*"
unks = []
import sys
root = sys.argv[1]
standard_dict = open(os.path.join(root, "standard.txt"))
s_words = []
s_codes = []
langs = []
while True:
    text_line = standard_dict.readline().replace("\n", "")
    if text_line == "":
        break
    temps = text_line.split("\t")
    s_words.append(temps[0])
    s_codes.append(temps[3])
    langs.append(temps[2])


def load_unks():
    global unks
    for index, word in enumerate(s_words):
        if langs[index] == "another":
            unks.append(word)


load_unks()
def my_process(sentence):
    sentence = sentence.replace("\n", "")
    temp = sentence.split("\t")
    temp = temp[0] + "\t" + temp[1] + "\t" + temp[2]
    sentence = sentence.split("\t")[3]
    words = sentence.split(" ")
    for index, word in enumerate(words):
        if word in unks:
            words[index] = UNK
        else:
            words[index] = s_codes[s_words.index(word)]
    sentence = " ".join(words)
    temp = temp + "\t" + sentence
    return temp


def unk_from_lst(dir, save_dir):
    filenames = os.listdir(dir)
    if not os.path.exists(save_dir):
        os.mkdir(save_dir)
    for filename in filenames:
        pool = multiprocessing.Pool()
        if ".lst" not in filename:
            continue
        print("PROCESS", filename)
        f = open(os.path.join(dir, filename))
        f1 = open(os.path.join(save_dir, filename), "w+")
        sentences = f.readlines()
        temps = pool.map(my_process, sentences)
        for temp in temps:
            f1.write(temp + "\n")
        f.close()
        f1.close()


unk_from_lst(os.path.join(root, "nor_number"), os.path.join(root, "nor_unk"))
