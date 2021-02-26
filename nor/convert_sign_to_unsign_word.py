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


def convert_unsign_to_sign_character(old_character, tone_type):
    global characters, tones
    char_index = characters.index(old_character)
    return tones[char_index][tone_type]


def reconstruct_word(i_code, n_code, c_code, tone_type):
    I, N, C = i_code, n_code, c_code
    if len(N) == 0:
        if len(C) == 0:
            I = I.replace(
                I[-1], convert_unsign_to_sign_character(I[-1], tone_type))
            return I + N + C
        print(i_code, n_code, c_code)
        try:
            tone_char = ["gi", "a", "â", "ă", "o", "ô", "ơ", "e", "ê", "u", "ư", "i", "y"]
            if C not in tone_char and I in tone_char:
                I = I.replace(
                    I[-1], convert_unsign_to_sign_character(I[-1], tone_type))
            else:
                C = C.replace(
                    C[-1], convert_unsign_to_sign_character(C[-1], tone_type))
        except:
            return None
        return I + N + C
    if tone_type == 0:
        return I + N + C
    if len(C) == 0:
        if len(N) == 2 and N[-1] in ["ê", "ơ"]:
            idx = 1
        elif len(N) <= 2:
            idx = 0
        elif len(N) == 3:
            idx = 1
        try:
            N = N.replace(
                N[idx], convert_unsign_to_sign_character(N[idx], tone_type))
        except:
            print(N)
            return None
    else:
        try:
            N = N.replace(
                N[-1], convert_unsign_to_sign_character(N[-1], tone_type))
        except:
            print(N)
            return None
    return I + N + C
