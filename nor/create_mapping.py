import pandas as pd
import sys, os
from vn_word import encode_word, decode_word

# dict_txt_path = "./data/final_dict.txt"
# f = open(dict_txt_path)
result = []
error = []
# words = f.readline()
vocab_dir = sys.argv[1]
f = open(os.path.join(vocab_dir, "vocab.txt"))
f_save = open(os.path.join(vocab_dir, "error_dict.txt"), "w+")
f_save2 = open(os.path.join(vocab_dir, "mapping_table.txt"), "w+")
words = f.readline().split("\t")
# words = pd.read_csv("./temp/vocab1.csv")["word"]
idx = -1
temp = False
for index, word in enumerate(words):
    i,n,codas,T = encode_word(word)
    encode_w = i + n + codas
    # print(encode_w, T)
    decode_w = decode_word(encode_w, T)
    if word != decode_w:
        if decode_w is None:
            decode_w = ""
        f_save.write(word + "\t" + encode_w+str(T) + "\t" + decode_w + "\n")
    # print(decode_w)
    f_save2.write(word + "\t" + encode_w+str(T) + "\t" + decode_w + "\n")