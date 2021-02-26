import pandas as pd
from convert_sign_to_unsign_word import convert
from word_code_utils import word_to_components, words_componet_to_codes
import sys
root = sys.argv[1]

freq_data = open(root + "freq.txt")
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

n_codes = []
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
        i_code, o_code, n_code, c_code = component
        if i_code == "gi":
            i_code = "d"
        if i_code == "ngh":
            i_code = "ng"
        if i_code == "gh":
            i_code = "g"
        if i_code == "k":
            i_code = "c"
        if i_code == "q":
            if o_code is "u":
                i_code = "qu"
                o_code = ""
        elif o_code == "u" or o_code == "o":
            n_code = o_code + n_code
            o_code = ""
        if n_code == "y":
            n_code = "i"
        
        if n_code not in n_codes:
            n_codes.append(n_code)

n_codes = sorted(n_codes)

for n_code in n_codes:
    print(n_code)