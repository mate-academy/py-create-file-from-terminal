import os
import sys
import datetime

path = sys.argv
current_dir = os.getcwd()


def making_file():
    file_name = path[-1]
    new_line_content = ""

    with open(file_name, "a") as file:
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"{current_time}\n")
        while new_line_content != "stop":
            new_line_content = input("Enter content line: ")
            file.write(f"{new_line_content}\n")

    with open(file_name, "r") as file:
        total_content = file.readlines()
        total_content.remove("stop\n")
        total_content_without_stop = "".join(total_content)

    with open(file_name, "w") as file:
        file.write(f"{total_content_without_stop}")


def making_dirs():
    try:
        dirs = path[path.index("-d") + 1:path.index("-f")]
    except ValueError:
        dirs = path[path.index("-d") + 1:]
    count = 0
    while count < len(dirs):
        os.mkdir(f"{current_dir}/" + "/".join(dirs[:count + 1]))
        os.chdir(f"{current_dir}/" + "/".join(dirs[:count + 1]))
        count += 1


if "-f" in path and "-d" in path:
    making_dirs()
    making_file()
else:
    if "-f" in path:
        if os.path.exists(os.path.join(current_dir, path[-1])):
            with open(os.path.join(current_dir, path[-1]), "a") as f:
                f.write("\n")
        making_file()

    if "-d" in path:
        making_dirs()
