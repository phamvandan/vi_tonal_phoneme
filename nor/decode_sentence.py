
def decode_sentence(sentence, check_dict):
    words = sentence.split()
    decode_sentences = []
    for word in words:
        decode_sentences.append(check_dict[word])
    return " ".join(decode_sentences)



f = open("./temp/mapping_table.txt")
error_word = []
correct_word = []
while True:
    text_line = f.readline().replace("\n", "")
    if text_line == "":
        break
    components = text_line.split("\t")
    error_word.append(components[1])
    correct_word.append(components[2])
# error_word = list(pd.read_csv("./temp/error_dict.csv")["word"])
# correct_word = pd.read_csv("./temp/error_dict.csv")["decode"]

check_dict = zip(error_word, correct_word)

check_dict = dict(check_dict)

sentence = "rem4 CƯ2 phong4 tăm5 mơ2"
print(sentence)

print(decode_sentence(sentence, check_dict))