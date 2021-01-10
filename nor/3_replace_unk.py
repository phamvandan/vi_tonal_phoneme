import os

import pandas as pd
UNK = "*"
unks = []


def load_unks():
    global unks
    standard_dict = pd.read_csv("../standard.csv")
    words = standard_dict["word"]
    langs = standard_dict["lang"]
    for index, word in enumerate(words):
        if langs[index] == "another":
            unks.append(word)


load_unks()


def unk_from_lst(dir, save_dir):
    filenames = os.listdir(dir)
    if not os.path.exists(save_dir):
        os.mkdir(save_dir)
    for filename in filenames:
        if ".lst" not in filename:
            continue
        print("PROCESS", filename)
        f = open(os.path.join(dir, filename))
        f1 = open(os.path.join(save_dir, filename), "w+")
        while True:
            sentence = f.readline().replace("\n", "")
            if sentence == "":
                break
            temp = sentence.split("\t")
            temp = temp[0] + "\t" + temp[1] + "\t" + temp[2]
            sentence = sentence.split("\t")[3]
            words = sentence.split(" ")
            for index, word in enumerate(words):
                if word in unks:
                    words[index] = UNK
            sentence = " ".join(words)
            temp = temp + "\t" + sentence
            f1.write(temp + "\n")
        f.close()
        f1.close()


unk_from_lst("../../prepare_all/temp", "../../prepare_all/nor_unk")
