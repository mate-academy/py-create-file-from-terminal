import os
import sys
import datetime as d


def parser() -> None:
    if "-d" in sys.argv and "-f" in sys.argv:
        dir_path = create_directory_and_path()
        print(dir_path)
        create_file(dir_path)
        return
    if "-d" in sys.argv:
        create_directory_and_path()
        return
    create_file()


def create_directory_and_path() -> str | bytes:
    try:
        dir_list = sys.argv[sys.argv.index("-d") + 1:sys.argv.index("-f")]
    except ValueError:
        dir_list = sys.argv[sys.argv.index("-d") + 1:len(sys.argv)]
    dir_path = os.path.join(*dir_list)
    try:
        os.makedirs(dir_path)
    except FileExistsError:
        return dir_path
    return dir_path


def create_file(dir_path: str = os.getcwd()) -> None:
    file_name = sys.argv[sys.argv.index("-f") + 1]
    file_path = os.path.join(dir_path, file_name)
    print(file_path)
    page_number = 1
    with open(file_path, "a") as file:
        file.write(f"{d.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        text = input("Enter content line: ")
        while text != "stop":
            file.write(f"{page_number} {text}\n")
            text = input("Enter content line: ")
            page_number += 1
        file.write("\n")


parser()
