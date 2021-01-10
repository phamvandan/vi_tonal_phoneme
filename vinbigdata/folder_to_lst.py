import sys
import os
from os import walk
import wave
import contextlib


def get_duration_of_audio_file(file_name):
    duration = 0
    with contextlib.closing(wave.open(file_name, 'r')) as f:
        frames = f.getnframes()
        rate = f.getframerate()
        duration = frames / float(rate)
    duration = round(duration, 2)
    return duration


prefix = "vlsp_2020_"
index = 1
save_name = "../../out/vin_big_data.lst"
f_lst = open(save_name, "w+")
folder_path = sys.argv[1]
for (dirpath, dirnames, filenames) in walk(folder_path):
    for filename in filenames:
        if ".txt" in filename:
            audio_path = os.path.join(dirpath, filename.split(".")[0] + ".wav")
            if not os.path.exists(audio_path):
                print(filename, "not exist")
                continue
            trans_path = os.path.join(dirpath, filename)
            f_trans = open(trans_path)
            trans = f_trans.readline().replace("\n", "")
            f_lst.write(prefix + str(index) + "\t" + audio_path + "\t" +
                        str(get_duration_of_audio_file(audio_path)) + "\t" + trans + "\n")
            index += 1

print("total", index)