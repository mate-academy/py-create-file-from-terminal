import os
import sys
import datetime


def create_folders(directions: list) -> str:
    directions_to_file = os.path.join(*directions)
    if not os.path.exists(directions_to_file):
        os.makedirs(directions_to_file)
    return directions_to_file


def open_file(file_name: str, path: str = "") -> None:
    with open(os.path.join(path, file_name), "a") as file:
        file.write(
            datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n"
        )
        line_num = 1
        while True:
            line_content = input("Enter content line: ")
            if line_content == "stop":
                break
            file.write(f"{line_num} {line_content}\n")
            line_num += 1


if "-d" in sys.argv and "-f" not in sys.argv:
    create_folders(sys.argv[sys.argv.index("-d") + 1:])

if "-f" in sys.argv and "-d" not in sys.argv:
    open_file(sys.argv[sys.argv.index("-f") + 1])

if "-f" in sys.argv and "-d" in sys.argv:
    index_d = sys.argv.index("-d")
    index_f = sys.argv.index("-f")
    folder_path = create_folders(sys.argv[index_d + 1:index_f])
    file_name = sys.argv[index_f + 1]
    open_file(
        file_name=file_name,
        path=folder_path
    )
