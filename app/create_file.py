import sys
import os
from datetime import datetime

print(sys.argv)


def make_file(file_name: str) -> None:
    content = []
    while True:
        content_line = input("Enter content line or enter stop to complete:")
        if content_line == "stop":
            break
        content.append(content_line)
    with open(file_name, "a") as f:
        f.write(datetime.now().strftime("%Y-%m-%d %H-%M-%S"))
        for line in content:
            f.write("\n" + line)
        f.write("\n")
        f.write("\n")
    print(f"File {file_name} has been created")


def make_dir(*path_way: str) -> None:
    path = os.path.join(*path_way)
    if not os.path.exists(path):
        os.makedirs(path)
        print(f"A folder has been created by the path: {path}")
    else:
        print(f"The folder at path {path} already exists")


path_way = None
file_name = None

if "-d" in sys.argv and "-f" in sys.argv:  # якщо два ключі
    f_index = sys.argv.index("-f")
    d_index = sys.argv.index("-d")
    if f_index > d_index:
        file_name = sys.argv[f_index + 1]
        path_way = sys.argv[d_index + 1: f_index]
    else:
        path_way = sys.argv[d_index + 1:]
        file_name = sys.argv[f_index + 1]

elif "-d" in sys.argv:
    d_index = sys.argv.index("-d")
    path_way = sys.argv[d_index + 1:]

elif "-f" in sys.argv:
    f_index = sys.argv.index("-f")
    file_name = "".join(sys.argv[-1:])
    print(f"file_name {file_name}")

else:
    print("No command line arguments are specified.")
    sys.exit()


if path_way:
    make_dir(*path_way)
    if file_name:
        file_name = os.path.join(*path_way, file_name)

if file_name:
    make_file(file_name)
