import pandas as pd
import sys
import os
UNK = "*"
SUR = "|"
root = sys.argv[1]
tokens = []
lexicons = []
words = []
langs = []
i_codes = []
o_codes = []
n_codes = []
c_codes = []

standard_dict = open(os.path.join(root, "standard.txt"))
while True:
    text_line = standard_dict.readline().replace("\n", "")
    if text_line == "":
        break
    temps = text_line.split("\t")
    words.append(temps[3])
    langs.append(temps[2])
    i_codes.append(temps[4])
    o_codes.append(temps[5])
    n_codes.append(temps[6])
    c_codes.append(temps[7])

tokens.append(SUR)
lexicons.append([UNK, "\t", UNK, SUR])
tokens.append(UNK)

for index, word in enumerate(words):
    if langs[index] == "another":
        continue
    else:
        lexicon = [str(word), "\t", str(i_codes[index]), str(o_codes[index]), str(n_codes[index]), str(c_codes[index]), SUR]
        lexicons.append(lexicon)
        if i_codes[index] is not '' and i_codes[index] not in tokens:
            tokens.append(i_codes[index])
        if o_codes[index] is not '' and o_codes[index] not in tokens:
            tokens.append(o_codes[index])
        if n_codes[index] is not '' and n_codes[index] not in tokens:
            tokens.append(n_codes[index])
        if c_codes[index] is not '' and c_codes[index] not in tokens:
            tokens.append(c_codes[index])

f_tokens = open(os.path.join(root, "tokens.txt"), "w+")
f_lexicons = open(os.path.join(root, "lexicons.txt"), "w+")
for token in tokens:
    f_tokens.write(str(token))
    f_tokens.write("\n")

for lexicon in lexicons:
    f_lexicons.write(lexicon[0])
    f_lexicons.write(lexicon[1])
    lexicon = ' '.join(lexicon[2:])
    print(lexicon)
    f_lexicons.write(lexicon)
    f_lexicons.write("\n")