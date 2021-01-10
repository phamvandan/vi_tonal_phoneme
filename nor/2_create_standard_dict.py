import pandas as pd
from convert_sign_to_unsign_word import convert
from word_code_utils import word_to_components, words_componet_to_codes

freq_data = pd.read_csv("../freq.csv")

words = freq_data["word"]
freqs = freq_data["freq"]

nor_word_lang = ''
nor_word_code = ''

nor_dict = []
count = 0

for index, word in enumerate(words):
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
pd.DataFrame(nor_dict, columns = ["word", "freq", "lang", "code", "i_code", "o_code", "n_code", "c_code"]).to_csv("../standard.csv")
print("another", count)
