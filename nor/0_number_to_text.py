import re, os

def check(dir):
    filenames = os.listdir(dir)
    for filename in filenames:
        print("PROCESS", filename)
        f = open(os.path.join(dir, filename))
        uniChars = "àáảãạâầấẩẫậăằắẳẵặèéẻẽẹêềếểễệđìíỉĩịòóỏõọôồốổỗộơờớởỡợùúủũụưừứửữựỳýỷỹỵÀÁẢÃẠÂẦẤẨẪẬĂẰẮẲẴẶÈÉẺẼẸÊỀẾỂỄỆĐÌÍỈĨỊÒÓỎÕỌÔỒỐỔỖỘƠỜỚỞỠỢÙÚỦŨỤƯỪỨỬỮỰỲÝỶỸỴÂĂĐÔƠƯ"
        rg = r"[^a-zA-Z " + uniChars + "]+"
        while True:
            sentence = f.readline().replace("\n", "")
            if sentence == "":
                break
            sentence = sentence.split("\t")[3]
            if re.search(rg, sentence):
                print(sentence)

def get_unvalid_from_lst(dir, save_dir):
    filenames = os.listdir(dir)
    uniChars = "àáảãạâầấẩẫậăằắẳẵặèéẻẽẹêềếểễệđìíỉĩịòóỏõọôồốổỗộơờớởỡợùúủũụưừứửữựỳýỷỹỵÀÁẢÃẠÂẦẤẨẪẬĂẰẮẲẴẶÈÉẺẼẸÊỀẾỂỄỆĐÌÍỈĨỊÒÓỎÕỌÔỒỐỔỖỘƠỜỚỞỠỢÙÚỦŨỤƯỪỨỬỮỰỲÝỶỸỴÂĂĐÔƠƯ"
    rg = r"[^a-zA-Z "+uniChars+"]+"
    for filename in filenames:
        if ".lst" not in filename:
            continue
        print("PROCESS", filename)
        f = open(os.path.join(dir, filename))
        f1 = open(os.path.join(save_dir, filename), "w+")
        while True:
            sentence = f.readline().replace("\n", "")
            t = sentence
            if sentence == "":
                break
            try:
                temp = sentence.split("\t")
                temp = temp[0] + "\t" + temp[1] + "\t" + temp[2]
                sentence = sentence.split("\t")[3]
                # if "<unk>" in sentence:
                #     sentence = sentence.replace("<unk>", "")
                sentence = sentence.lower()
                sentence = re.sub(rg, lambda x:read_number_and_normalize_text(x.group()).strip(), sentence)
                sentence = " ".join(sentence.split()).strip()
                if len(sentence)==0:
                    print("skip", temp, sentence)
                    continue
                # if re.search(rg, sentence):
                #     print("SKIP", sentence)
                #     continue
                temp = temp + "\t" + sentence
                f1.write(temp + "\n")
            except:
                print("here", t, "here")
                break
        f.close()
        f1.close()

def one_number_process(number):
    one_number = {
        "0": "không",
        "1": "một",
        "2": "hai",
        "3": "ba",
        "4": "bốn",
        "5": "năm",
        "6": "sáu",
        "7": "bảy",
        "8": "tám",
        "9": "chín"
    }
    return one_number[number]

def two_number_process(number):
    chuc = ""
    donvi = ""
    if number == "00":
        return ""
    if number == "10":
        return "mười"
    if number[0] == "1":
        chuc = "mười"
    else:
        chuc = one_number_process(number[0]) + " mươi"
    if number[1] == "0":
        donvi = ""
    elif number[1] == "1":
        donvi = "mốt"
    elif number[1] == "5":
        donvi = "lăm"
    else:
        donvi = one_number_process(number[1])
    return chuc + " " + donvi

def three_number_process(number):
    if number == "000":
        return ""
    if number[1] == "0" and number[2] != "0":
        return one_number_process(number[0]) + " trăm lẻ " + one_number_process(number[2])
    return one_number_process(number[0]) + " trăm " + two_number_process(number[1:])

def four_number_process(number):
    return one_number_process(number[0]) + " nghìn " + three_number_process(number[1:])

def five_number_process(number):
    return two_number_process(number[:2]) + " nghìn " + three_number_process(number[2:])

def six_number_process(number):
    if "000000" in number:
        return ""
    return three_number_process(number[:3]) + " nghìn " + three_number_process(number[3:])

def mili_number_process(number):
    if not re.search("[^0]+", number):
        return ""
    if len(number) == 7:
        return one_number_process(number[0]) + " triệu " + six_number_process(number[1:])
    if len(number) == 8:
        return two_number_process(number[:2]) + " triệu " + six_number_process(number[2:])
    if len(number) == 9:
        return three_number_process(number[:3]) + " triệu " + six_number_process(number[3:])

def bili_number_process(number):
    if len(number) == 10:
        return one_number_process(number[0]) + " tỉ " + mili_number_process(number[1:])
    if len(number) == 11:
        return two_number_process(number[:2]) + " tỉ " + mili_number_process(number[2:])
    if len(number) == 12:
        return three_number_process(number[:3]) + " tỉ " + mili_number_process(number[3:])


def number_text(number):
    if re.search("[^0-9]", number):
        return number
    if len(number) == 1:
        return one_number_process(number)
    elif len(number) == 2:
        return two_number_process(number)
    elif len(number) == 3:
        return three_number_process(number)
    elif len(number) == 4:
        return four_number_process(number)
    elif len(number) == 5:
        return five_number_process(number)
    elif len(number) == 6:
        return six_number_process(number)
    elif 7<=len(number)<=9:
        return mili_number_process(number)
    elif 10<=len(number)<=12:
        return bili_number_process(number)
    return number

from collections import Counter
import pandas as pd

def read_number_and_normalize(filename="./token_result.txt"):
    rs = []
    f = open(filename)
    while True:
        invalid = f.readline().replace("\n","").strip()
        if invalid == "":
            break
        if invalid == "&":
            rs.append([invalid, "và"])
            continue
        if invalid == "@":
            rs.append([invalid, "a còng"])
            continue
        if invalid == "=":
            rs.append([invalid, "bằng"])
            continue
        if len(invalid) == 1 and re.search("['*+-./]", invalid):
            rs.append([invalid, ""])
            continue
        numbers = None
        text = ""
        temp = invalid
        if "-" in invalid[0]:
            invalid = invalid.replace("-", "âm ")
        if "," in invalid or "." in invalid:
            invalid = invalid.replace(",", " phẩy ").replace(".", " phẩy ")
        if "₫" in invalid:
            invalid = invalid.replace("₫", " đồng ")
        if "%" in invalid:
            invalid = invalid.replace("%", " phần trăm ")
        if ":" in invalid:
            invalid = invalid.replace(":", " giờ ") + " phút"
        if "/" in invalid:
            if len(invalid.split("/")[1]) >2:
                invalid = " tháng " + invalid.replace("/", " năm ")
            else:
                invalid = " ngày " + invalid.replace("/", " tháng ")
        if "-" in invalid:
            invalid = invalid.replace("-", " ")
        if Counter(invalid)["-"] == 2:
            invalid = "ngày " + invalid.replace("-"," tháng ", 1)
            invalid = invalid.replace("-"," năm ", 1)
            # print(invalid)
        texts = invalid.split(" ")
        txt = ""
        for text in texts:
            if re.search("[^0-9]+", text):
                txt += text + " "
            else:
                txt += number_text(text) + " "
        rs.append([temp, txt])
        # if
        #     numbers = invalid.split(",").split("₫").split("%")
        #     text = text + number_text(numbers[0] + " phẩy " + numbers[1])
        #
        #
        #     text = text + " phần trăm"

        # if
    pd.DataFrame(rs, columns=["number", "text"]).to_csv("rs.csv")


def read_number_and_normalize_text(invalid):
    rs = []
    if invalid == "&":
        return "và"
    if invalid == "@":
        return "a còng"
    if invalid == "=":
        return "bằng"
    if len(invalid) == 1 and re.search(r"[\\'*+-./!\"[?]", invalid):
        return ""
    
    numbers = None
    text = ""
    temp = invalid
    if "-" in invalid[0]:
        invalid = invalid.replace("-", "âm ")
    if "," in invalid or "." in invalid:
        invalid = invalid.replace(",", " phẩy ").replace(".", " phẩy ")
    if "°" in invalid:
        invalid = invalid.replace("°", " độ")
    if "+" in invalid:
        invalid = invalid.replace("+", " cộng ")
    if "$" in invalid:
        invalid = invalid.replace("$", " đô")
    if "₫" in invalid:
        invalid = invalid.replace("₫", " đồng ")
    if "%" in invalid:
        invalid = invalid.replace("%", " phần trăm ")
    if ":" in invalid:
        invalid = invalid.replace(":", " giờ ") + " phút"
    if "/" in invalid:
        if len(invalid.split("/")[1]) >2:
            invalid = " tháng " + invalid.replace("/", " năm ")
        else:
            invalid = " ngày " + invalid.replace("/", " tháng ")
    if "-" in invalid:
        invalid = invalid.replace("-", " ")
    if Counter(invalid)["-"] == 2:
        invalid = "ngày " + invalid.replace("-"," tháng ", 1)
        invalid = invalid.replace("-"," năm ", 1)
        # print(invalid)
    texts = invalid.split(" ")
    txt = ""
    for text in texts:
        if re.search("[^0-9]+", text):
            txt += text + " "
        else:
            txt += number_text(text) + " "
    return txt

if __name__ == '__main__':
    get_unvalid_from_lst("../../out/origin_lst", "../../out/nor_number")
    # check("../../out/nor_number")