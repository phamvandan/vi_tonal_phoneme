import pandas as pd
from convert_sign_to_unsign_word import convert
from word_code_utils import *
import sys
root = sys.argv[1]

freq_data = open(root + "freq.txt")
f_nor_dict = open(root + "standard.txt", 'w+')
words = []
freqs = []
while True:
    text_line = freq_data.readline().replace("\n", "")
    if text_line == "":
        break
    temps = text_line.split("\t")
    words.append(temps[0])
    freqs.append(temps[1])

nor_word_lang = ''
nor_word_code = ''

nor_dict = []
count = 0

for index, word in enumerate(words):
    word = str(word)
    unsign_word, tone_type = convert(word)
    component, tone_type = word_to_components(unsign_word, tone_type)
    if component is None or freqs[index]==1:
        nor_word_lang = "another"
        nor_word_code = ' '
        i_code, o_code, n_code, c_code = ' ', ' ', ' ', ' '
        count += 1
    else:
        nor_word_lang = "vi"
        # i_code, o_code, n_code, c_code = words_componet_to_codes(component, tone_type)
        i_code, o_code, n_code, c_code = component
        # if i_code == "gi":
        #     i_code = "d"
        # if i_code == "ngh":
        #     i_code = "ng"
        # if i_code == "gh":
        #     i_code = "g"
        # if i_code == "k":
        #     i_code = "c"
        if i_code == "q":
            if o_code is "u":
                i_code = "qu"
                o_code = ""
        elif o_code == "u" or o_code == "o":
            n_code = o_code + n_code
            o_code = ""
        # if n_code == "y":
        #     n_code = "i"
        w_code = i_code + o_code + n_code + c_code + str(tone_type)
        convert_w = reconstruct_word(i_code, o_code, n_code, c_code, tone_type)
        if convert_w is None:
            nor_word_lang = "another"
        nor_word_code = w_code
    nor_dict.append([word, freqs[index], nor_word_lang, nor_word_code, i_code, o_code, n_code, c_code, str(tone_type), str(convert_w)])

nor_dict = sorted(nor_dict, key = lambda x:x[2])
for e in nor_dict:
    f_nor_dict.write("\t".join(e) + "\n")
print("another", count)
