import glob
import os

lst_dir = "./data"
save_dir = "./saved_dir"
filepaths = glob.glob(os.path.join(lst_dir, "/*.lst"))

for filepath in filepaths:
    f = open(filepath)
    filename = filepath.split("/")[-1]
    f_save = open(os.path.join(save_dir, filename), "w+")
    while True:
        text_line = f.readline().replace("\n", "")
        if text_line == "":
            break
        fields = text_line.split("\t")
        for word in fields[3]:
