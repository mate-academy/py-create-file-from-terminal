import sys
import pathlib
from datetime import datetime


data_today = datetime.now()


def input_typing(file_inside: str) -> None:
    while True:
        text_input = input("Enter content line:")
        if text_input == "stop":
            file_inside.close()
            break
        file_inside.write(text_input + "\n")


if "-d" and "-f" in sys.argv:
    create_dir = "/".join(sys.argv[sys.argv.index("-d") + 1:
                                   sys.argv.index("-f")])
    pathlib.Path(create_dir).mkdir(parents=True, exist_ok=True)
    file_name = "/".join(sys.argv[sys.argv.index("-f") + 1:])
    file_patch = f"{create_dir}/{file_name}"
    file_create = open(file_patch, "w")
    file_create.write(data_today.strftime("%d-%m-%Y %H:%M:%S") + "\n")
    input_typing(file_create)

elif "-d" in sys.argv:
    create_dir = "/".join(sys.argv[sys.argv.index("-d") + 1:])
    pathlib.Path(create_dir).mkdir(parents=True, exist_ok=True)


elif "-f" in sys.argv:
    file_name = "/".join(sys.argv[sys.argv.index("-f") + 1:])
    path_file = pathlib.Path("file.txt")
    if path_file.exists() is None:
        file_create = open(file_name, "w")
    else:
        file_create = open(file_name, "a")
    file_create.write(data_today.strftime("%d-%m-%Y %H:%M:%S") + "\n")
    input_typing(file_create)
