import pandas as pd
from vn_word import encode_word, decode_word

dict_txt_path = "./data/final_dict.txt"
f = open(dict_txt_path)
result = []
error = []
words = f.readline()
words = words.split("\t")

for word in words:
    print(word)
    i,n,codas,T = encode_word(word)
    encode_w = i + n + codas
    print(encode_w, T)
    decode_w = decode_word(encode_w, T)
    if word != decode_w:
        error.append((word,i,n,codas,str(T), encode_w+str(T), decode_w))
    result.append((word,i,n,codas,str(T), encode_w+str(T), decode_w))
    # print(decode_w)
pd.DataFrame(result).to_csv("./true_dict.csv")
pd.DataFrame(error).to_csv("./error_dict.csv")