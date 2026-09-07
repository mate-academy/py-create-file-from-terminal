import os
import sys
import datetime


def create_file_in_directory() -> None:
    if "-d" in sys.argv and "-f" in sys.argv:
        if sys.argv.index("-d") < sys.argv.index("-f"):
            path = (sys.argv[sys.argv.index("-d") + 1:sys.argv.index("-f")])
            file_name = (sys.argv[sys.argv.index("-f") + 1:])
            create_directory(path)
            create_file(path, file_name)
        elif sys.argv.index("-f") < sys.argv.index("-d"):
            path = (sys.argv[sys.argv.index("-d") + 1:])
            file_name = (sys.argv[sys.argv.index("-f")
                                  + 1:sys.argv.index("-d")])
            create_directory(path)
            create_file(path, file_name)
    elif "-d" in sys.argv:
        path = sys.argv[sys.argv.index("-d") + 1:]
        create_directory(path)
    elif "-f" in sys.argv:
        file_name = (sys.argv[sys.argv.index("-f") + 1:])
        create_file([], file_name)


def create_directory(path: list) -> None:
    os.makedirs(os.path.join(*path), exist_ok=True)


def create_file(path: list, file_name: list) -> None:
    file_path = os.path.join(*path, *file_name)
    with open(file_path, "a") as f:
        if os.path.getsize(file_path) > 0:
            f.write("\n\n")
        f.write(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        line_num = 0
        while True:
            line = input("Enter content line: ")
            if line == "stop":
                break
            line_num += 1
            f.write(f"\n{str(line_num)} {line}")


create_file_in_directory()
