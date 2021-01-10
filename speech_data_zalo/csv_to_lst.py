import sys
import os
from os import walk
import wave
import contextlib
import pandas as pd

def get_duration_of_audio_file(file_name):
    duration = 0
    with contextlib.closing(wave.open(file_name, 'r')) as f:
        frames = f.getnframes()
        rate = f.getframerate()
        duration = frames / float(rate)
    duration = round(duration, 2)
    return duration


prefix = "speech_zalo_"
index = 1
save_name = "../../out/" + prefix + "data.lst"
f_lst = open(save_name, "w+")
folder_path = sys.argv[1]
for (dirpath, dirnames, filenames) in walk(folder_path):
    for filename in filenames:
        if ".csv" in filename:
            trans_path = os.path.join(dirpath, filename)
            data = pd.read_csv(trans_path)
            audio_names = data["audio_name"]
            trans = data["trans"]
            for idx, audio_name in enumerate(audio_names):
                audio_path = os.path.join(dirpath, "audios/" + audio_name)
                if not os.path.exists(audio_path):
                    print(filename, "not exist")
                    continue
                f_lst.write(prefix + str(index) + "\t" + audio_path + "\t" +
                            str(get_duration_of_audio_file(audio_path)) + "\t" + str(trans[idx]) + "\n")
                index += 1

print("total", index)