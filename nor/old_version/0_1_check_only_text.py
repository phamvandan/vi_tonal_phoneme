import re
import sys
import argparse

UNI_CHARS = "àáảãạâầấẩẫậăằắẳẵặèéẻẽẹêềếểễệđìíỉĩịòóỏõọôồốổỗộơờớởỡợùúủũụưừứửữựỳýỷỹỵÀÁẢÃẠÂẦẤẨẪẬĂẰẮẲẴẶÈÉẺẼẸÊỀẾỂỄỆĐÌÍỈĨỊÒÓỎÕỌÔỒỐỔỖỘƠỜỚỞỠỢÙÚỦŨỤƯỪỨỬỮỰỲÝỶỸỴÂĂĐÔƠƯ"

def check_file(file_path):
    print("PROCESS", file_path)
    f = open(file_path)
    rg = r"[^a-zA-Z " + UNI_CHARS + "]+"
    while True:
        sentence = f.readline().replace("\n", "")
        if sentence == "":
            break
        sentence = sentence.split("\t")[3]
        if re.search(rg, sentence):
            print(sentence)

def check_dir(lst_dir):
    filenames = os.listdir(lst_dir)
    for filename in filenames:
        file_path = os.path.join(lst_dir, filename)
        check_file(file_path)

if __name__ == '__main__':
    args = argparse.ArgumentParser()
    args.add_argument("--dir", default=None)
    args.add_argument('--file', default=None)
    parse = args.parse_args()
    if parse.dir is not None:
        check_dir(parse.dir)
    if parse.file is not None:
        check_file(parse.file)
