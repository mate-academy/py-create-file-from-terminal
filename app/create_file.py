import os
import sys
import datetime


def enter_contend() -> str:
    file_contend = ""
    line_contend = ""
    count = 1
    while line_contend != "stop":
        line_contend = input("Enter content line:")
        if line_contend != "stop":
            file_contend += f"Line{count} {line_contend}\n"
            count += 1
    return file_contend


def create_directory(folders: list) -> str:
    path = "app/"
    for folder in folders[1:]:
        if folder == "-f":
            break
        path += folder + "/"
    os.makedirs(path, exist_ok=True)
    return path


def create_file(file_name: list) -> None:
    date_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if "-d" not in file_name:
        path = f"app/{file_name[-1]}"
    else:
        path = os.path.join(create_directory(file_name), file_name[-1])
    if not os.path.exists(path):
        with open(path, "w") as new_file:
            file_contend = f"{date_time}\n" + enter_contend()
            new_file.write(file_contend)
    else:
        with open(path, "a") as new_file:
            file_contend = f"\n{date_time}\n" + enter_contend()
            new_file.write(file_contend)


directory = sys.argv[1:]

if "-d" in directory and "-f" not in directory:
    create_directory(directory)
if "-d" not in directory and "-f" in directory:
    create_file(directory)
if "-d" in directory and "-f" in directory:
    create_file(directory)
