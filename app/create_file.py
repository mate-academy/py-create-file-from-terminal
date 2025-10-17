import sys
import os

proba = sys.argv


if "-f" in proba:
    f_index = proba.index("-f")
    if "-d" in proba:
        d_index = proba.index("-d")
        path = os.path.join(*proba[d_index + 1: f_index])
        os.makedirs(path, exist_ok=True)
        path_to_file = path + "\\" + proba[f_index + 1]
        print(path_to_file)
        if os.path.exists(path_to_file):
            with open(path_to_file, "a") as file_append:
                while True:
                    message = input("Dopisz cos: ")
                    if message.lower() == "stop":
                        break
                    file_append.write(message + "\n")
        else:
            with open(path_to_file, "w") as file_write:
                while True:
                    message = input("wpisz cos")
                    if message.lower() == "stop":
                        break
                    file_write.write(message + "\n")
elif "-d" in proba:
    d_index = proba.index("-d")
    path = os.path.join(*proba[d_index + 1:])
    print(path)
    os.makedirs(path, exist_ok=True)
