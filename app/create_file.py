import os
import sys
import datetime


# os.makedirs(os.path.join("dir1/dir2/"))

def create_directory(dir_path: str, filename: str = None) -> None:
    print(filename)
    dir_path = dir_path.split(" ")
    directory = ""
    flag = False
    for word in dir_path:
        if word == "-f":
            create_file(directory + filename)
            break
        if flag:
            directory += f"{word}/"
            os.mkdir(os.path.join(directory))
        if word == "-d":
            flag = True


def create_file(file_name: str) -> None:
    with open(os.path.join(file_name), "a") as file:
        command = str(datetime.datetime.today())[:-7]
        file.write(command + "\n")
        while True:
            command = input("Enter content line: ")
            if command == "stop":
                break
            file.write(command + "\n")
        file.write("\n")


if len(sys.argv) > 1 and "-d" in sys.argv and "-f" in sys.argv:
    create_directory(" ".join(sys.argv), sys.argv[-1])

elif len(sys.argv) > 1 and "-d" in sys.argv:
    create_directory(" ".join(sys.argv))

elif len(sys.argv) > 1 and "-f" in sys.argv:
    create_file(sys.argv[-1])
