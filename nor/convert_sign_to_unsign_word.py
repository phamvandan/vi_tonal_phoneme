characters = []
tones = []

def load_c_and_tone():
    global characters, tones
    f_tone = open("./tone.txt")


    while True:
        text_line = f_tone.readline().replace("\n", "")
        if text_line == "":
            break
        temp = text_line.split("\t")
        characters.append(temp[0])
        tones.append(temp[1].split(" "))

load_c_and_tone()
print(tones)
print(characters)

def convert(old_word):
    old_word = str(old_word)
    tone_type = 0
    new_word = old_word
    for c in old_word:
        for index, tone in enumerate(tones):
            if c in tone:
                tone_type = tone.index(c)
                if tone_type == 0:
                    continue
                new_word = old_word.replace(c, characters[index])
                return new_word, tone_type
    return new_word, tone_type