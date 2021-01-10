import pandas as pd
from convert_sign_to_unsign_word import convert
from word_code_utils import word_to_components, words_componet_to_codes
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
        i_code, o_code, n_code, c_code = words_componet_to_codes(component, tone_type)
        w_code = i_code + o_code + n_code + c_code 
        nor_word_code = w_code
    nor_dict.append([word, freqs[index], nor_word_lang, nor_word_code, i_code, o_code, n_code, c_code])

nor_dict = sorted(nor_dict, key = lambda x:x[2])
for e in nor_dict:
    f_nor_dict.write("\t".join(e) + "\n")
print("another", count)
