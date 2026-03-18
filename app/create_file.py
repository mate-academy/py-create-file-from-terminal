import sys
import os
import datetime


directory_list = []
file_str = ""
i = 1
while i < len(sys.argv):
    if sys.argv[i] == "-d":
        while i < (len(sys.argv) - 1) and sys.argv[i + 1] != "-f":
            directory_list.append(sys.argv[i + 1])
            i += 1
    if sys.argv[i] == "-f":
        if i < (len(sys.argv) - 1):
            file_str = sys.argv[i + 1]
    i += 1
if directory_list:
    path = os.path.join(*directory_list)
    os.makedirs(path, exist_ok=True)
    if file_str:
        path_file = os.path.join(path, file_str)
else:
    path_file = file_str

if path_file:
    with open(path_file, "a") as file:
        file.write(
            datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n"
        )
        while True:
            content = input("Enter content line: ")
            if content == "stop":
                file.write("\n")
                break
            i = 1
            file.write(f"{i} content\n")
            i += 1
