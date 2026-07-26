import datetime
import os
import sys


def create_file(file_name):
    file_path = []
    if "-d" in file_name:
        for el in range(file_name.index("-d"), len(file_name)):
            if file_name[el] == "-f":
                break
            file_path.append(file_name[el])
    os.makedirs(os.path.join(*file_path))

    if "-f" in file_name:
        file_path.append(file_name[file_name.index("-f") + 1])
        with open(os.path.join(*file_name), "a") as f:
            f.write(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            f.write("\n")
            number_line = 1
            while True:
                input_text = input("Enter content line: ")
                if input_text == "stop":
                    return
                f.write(f"{number_line} {input_text} \n")
                number_line += 1


create_file(sys.argv)
