from convert_sign_to_unsign_word import *

I = "b,ch,đ,ph,h,d,k,qu,c,l,m,n,nh,ng,ngh,p,x,s,t,th,tr,v,kh,g,gh,gi,r,cz,ngz,gz"
I = I.split(",")
I = sorted(I, key=lambda x:len(x), reverse=True)
print(I)
C = "m,n,ng,nh,ch,p,t,u,y,i,c,o"
C = C.split(",")
C = sorted(C, key=lambda x:len(x), reverse=True)
print(C)

def rmv_dup_char(chars):
    existed = []
    for c in chars:
        if c not in existed:
            existed.append(c)
    return "".join(existed)

def word_to_components(word):
    i,n,codas = "","",""
    unsign_word, T = convert(word)
    for c in I:
        if unsign_word.startswith(c):
            i = c
            unsign_word = unsign_word[len(c):]
            break
    
    for c in C:
        if unsign_word.endswith(c):
            if c == "y" and len(unsign_word)==1:
                break
            codas = c
            unsign_word = unsign_word[:-len(codas)]
            break
    n = unsign_word
    n = rmv_dup_char(n)
    return i,n,codas,T
0
def encode_i(initial_char):
    if initial_char in ["c","k"]:
        return "cz"
    elif initial_char in ["ng","ngh"]:
        return "ngz"
    elif initial_char in ["g","gh"]:
        return "gz"
    return initial_char

def decode_i(initial_char, word, tone_type):
    # if len(initial_char) == len(word):
    #     return initial_char[:-1]
    after_c = word[len(initial_char):len(initial_char)+1]
    if initial_char == "gz":
        if after_c == "i" and tone_type == 4:
            return "gh"
    if after_c in ["i","y","e","ê"]:
        if initial_char == "cz":
            return "k"
        if initial_char == "ngz":
            return "ngh"
        if initial_char == "gz":
            return "gh"
    if initial_char in ["cz","ngz","gz"]:
        return initial_char[:-1]
    return initial_char

nuclei_map = {  "yê":"iêz",
                "iê":"iêz",
                "ya":"iaz",
                "ia":"iaz",
                "ươ":"ưaz",
                "ưa":"ưaz",
                "uô":"uaz",
                "ua":"uaz",
                "y":"iz" }

def encode_n(nuclei):
    for special_char in nuclei_map.keys():
        if special_char in nuclei:
            return nuclei.replace(special_char, nuclei_map[special_char])
    return nuclei

def decode_n(nuclei, codas, initial_char):
    for special_char in nuclei_map.values():
        if special_char in nuclei:
            if special_char in ["iêz","iaz"]:
                if initial_char == "" and len(codas)>0:
                    return nuclei.replace(special_char,"y" + special_char[1])
                if (initial_char == "" or initial_char[-1] != 'u') and nuclei.startswith(special_char):
                    return nuclei.replace(special_char, special_char[:-1])
                return nuclei.replace(special_char,"y" + special_char[1])
            elif special_char in ["ưaz","uaz"]:
                if codas == "":
                    return nuclei.replace(special_char,special_char[:-1])
                if special_char == "uaz":
                    return nuclei.replace(special_char, "uô")
                return nuclei.replace(special_char, "ươ")
            elif special_char == "iz":
                if (initial_char != "" and initial_char in ["k", "qu"]) or( nuclei != "" and nuclei[0] == "u"):
                    return nuclei.replace(special_char, "y")
                return nuclei.replace(special_char, special_char[:-1])
    return nuclei

def encode_word(word):
    i,n,codas,T = word_to_components(word)
    i = encode_i(i)
    n = encode_n(n)
    return i,n,codas,T

def decode_word(word, tone_type):
    i,n,codas,T = word_to_components(word)
    if i != "":
        i = decode_i(i, word, tone_type)
    if n != "":
        n = decode_n(n, codas, i)
    return reconstruct_word(i,n,codas,tone_type)
# i,n,codas,T = word_to_components["khồng"]

# print(i,n,codas,T)

# result = decode_i["cz", "kiên", 4)
# print(result)

# print(decode_n("uy"))

i,n,codas,T = encode_word("nguýt")

print(i,n,codas,T)

# newword = i + n+ codas
# print(newword)
print(decode_word("ngzuizt", 5))
