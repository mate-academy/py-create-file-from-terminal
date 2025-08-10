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
        line_number = 1
        for line in content:
            f.write("\n")
            f.write(str(line_number) + " " + line)
            line_number += 1

        f.write("\n")
        f.write("\n")
    print(f"File {file_name} has been created")


def make_dir(*path_way: str) -> None:
    path = os.path.join(*path_way)
    os.makedirs(path, exist_ok=True)
    print(f"A folder has been created by the path: {path}")


def obtaining_file_name() -> str:
    if "-f" in sys.argv:
        return "".join(sys.argv[sys.argv.index("-f") + 1])


def obtaining_path_way() -> list:
    if "-d" in sys.argv:
        pathway = []
        for element in sys.argv[sys.argv.index("-d") + 1:]:
            if element == "-f":
                break
            pathway.append(element)
        return pathway


file_name = obtaining_file_name()
path_way = obtaining_path_way()


if path_way:
    make_dir(*path_way)
    if file_name:
        file_name = os.path.join(*path_way, file_name)

if file_name:
    make_file(file_name)
