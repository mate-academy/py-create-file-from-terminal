import sys
import datetime
import os


def file_creation(file_name: str):
    path_to_file = []
    if "-d" in file_name:
        for i in range(file_name.index("-d"), len(file_name)):
            if file_name[i] == "-f":
                break
            path_to_file.append(file_name[i])
    os.makedirs(os.path.join(*path_to_file))

    if "-f" in file_name:
        path_to_file.append(file_name[file_name.index('-f') + 1])
        with open(os.path.join(*path_to_file), "a") as file_in:
            file_in.write(datetime.datetime.now().strftime("%Y-%m-%d "
                                                           "%H:%M:%S"))
            file_in.write("\n")
            line = 1
            while True:
                input_txt = input("Enter content line: ")
                if input_txt.lower() == "stop":
                    return
                file_in.write(f"{line} {input_txt} \n")
                line += 1


file_creation(sys.argv)
