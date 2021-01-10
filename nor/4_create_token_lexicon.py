import pandas as pd
import sys
import os
UNK = "*"
SUR = "|"
root = sys.argv[1]
standard_dict = pd.read_csv(os.path.join(root, "standard.csv"))
tokens = []
lexicons = []

words = standard_dict["word"]
langs = standard_dict["lang"]
i_codes = standard_dict["i_code"]
o_codes = standard_dict["o_code"]
n_codes = standard_dict["n_code"]
c_codes = standard_dict["c_code"]

tokens.append(SUR)
lexicons.append([UNK, "\t", UNK, SUR])
tokens.append(UNK)

for index, word in enumerate(words):
    if langs[index] == "another":
        continue
    else:
        lx = [str(word), "\t", str(i_codes[index]), str(o_codes[index]), str(n_codes[index]), str(c_codes[index]), SUR]
        lexicon = []
        for e in lx:
            if str(e) == "nan":
                continue
            lexicon.append(e)
        lexicons.append(lexicon)
        if i_codes[index] not in tokens:
            tokens.append(i_codes[index])
        if o_codes[index] not in tokens:
            tokens.append(o_codes[index])
        if n_codes[index] not in tokens:
            tokens.append(n_codes[index])
        if c_codes[index] not in tokens:
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