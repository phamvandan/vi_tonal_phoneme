from convert_sign_to_unsign_word import convert, convert_unsign_to_sign_character


def load_encode(file_name):
    f = open(file_name)
    codes = []
    chars = []
    while True:
        text_line = f.readline().replace("\n", "")
        if text_line == "":
            break
        temp = text_line.split("\t")
        codes.append(temp[0])
        chars.append(temp[1])
    codes, chars = zip(
        *sorted(zip(codes, chars), key=lambda x: len(x[1]), reverse=True))
    # print(codes, chars)
    return codes, chars


i_codes, i_chars = load_encode("./initial.txt")
o_codes, o_chars = load_encode("./onset.txt")
n_codes, n_chars = load_encode("./nuclei.txt")
c_codes, c_chars = load_encode("./codas.txt")


def word_to_components(unsign_word, tone_type):
    I = ''
    C = ''
    O = ''
    N = ''
    w_temp = unsign_word
    # print(unsign_word)
    for c in i_chars:
        if unsign_word.startswith(c):
            I = c
            unsign_word = unsign_word[len(c):]
            break

    for c in c_chars:
        if unsign_word.endswith(c):
            if c not in ['o', 'ơ', 'ư', 'u', 'i', 'y']:
                C = c
                unsign_word = unsign_word[:-len(c)]
                break
            else:
                if len(unsign_word) > 1:
                    C = c
                    unsign_word = unsign_word[:-len(c)]
                    break
    if len(unsign_word) > 1:
        if (unsign_word[0] == 'u' and (unsign_word[1] not in ['a', 'ô'])) or unsign_word[0] == 'o':
            O = unsign_word[0]
            unsign_word = unsign_word[1:]
    if unsign_word in n_chars:
        N = unsign_word
    # print(I, O, N, C)
    if w_temp != I + O + N + C:
        return None, tone_type
    else:
        return [I, O, N, C], tone_type


def words_componet_to_codes(component, tone_type):
    I, O, N, C = component
    i_code = ''
    o_code = ''
    n_code = ''
    c_code = ''
    tone_type = "_" + str(tone_type)
    if component[0] != '':
        i_code = i_codes[i_chars.index(component[0])]
    if component[1] != '':
        o_code = o_codes[o_chars.index(component[1])] + tone_type
    if component[2] != '':
        n_code = n_codes[n_chars.index(component[2])]
        if N == 'a':
            if C in ['c', 'ch', 'ng', 'nh']:
                n_code = n_code + "1"
            elif C in ['u', 'y']:
                n_code = n_code + "3"
            else:
                n_code = n_code + "2"
        if N == 'o':
            if C in ['c', 'ch', 'ng', 'nh']:
                n_code = n_code + "1"
            else:
                n_code = n_code + "2"
        n_code = n_code + tone_type

    if component[3] != '':
        c_code = c_codes[c_chars.index(component[3])] + tone_type

    return i_code, o_code, n_code, c_code


def reconstruct_word(i_code, n_code, c_code, tone_type):
    I, N, C = i_code, n_code, c_code
    if len(N) == 0:
        print(i_code, n_code, c_code)
        try:
            I = I.replace(I[-1], convert_unsign_to_sign_character(I[-1], tone_type))
        except:
            return None
        return I + O + N + C
    if tone_type == 0:
        return I + O + N + C
    if len(C) == 0:
        if len(N) <= 2:
            idx = 0
        elif len(N) == 3:
            idx = 1
        try:
            N = N.replace(N[idx], convert_unsign_to_sign_character(N[idx], tone_type))
        except:
            print(N)
            return None
    else:
        try:
            N = N.replace(N[-1], convert_unsign_to_sign_character(N[-1], tone_type))
        except:
            print(N)
            return None
    return I + N + C
# def word_code_to_word_component(word_code):


# word = "nản"
# unsign_word, tone_type = convert(word)
# print(unsign_word)
# component, tone_type = word_to_components(unsign_word, tone_type)
# print(component)
# print(words_componet_to_codes(component, tone_type))
