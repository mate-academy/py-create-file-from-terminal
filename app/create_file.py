import datetime
import os
import sys


def create_file(current_path: str) -> None:
    file_name = sys.argv[sys.argv.index("-f") + 1]
    with open(os.path.join(current_path, file_name), "a") as text_file:
        time = datetime.datetime.now()
        text_file.write(time.strftime("20%y-%m-%d %H:%m:%S\n"))
        line_number = 0
        while True:
            line = input("Enter content line: ")
            if line == "stop":
                break
            line_number += 1
            text_file.write(f"{line_number} {line}\n")
        text_file.write("\n")


def create_directory(current_path: str) -> str:
    new_dir1, new_dir2 = sys.argv[sys.argv.index("-d") + 1], \
        sys.argv[sys.argv.index("-d") + 2]
    new_path = os.path.join(current_path, new_dir1, new_dir2)
    os.makedirs(new_path)
    return new_path


if __name__ == "__main__":
    if "-f" in sys.argv and "-d" in sys.argv:
        new_directory_path = create_directory(os.getcwd())
        create_file(new_directory_path)

    elif "-f" in sys.argv:
        create_file(os.getcwd())

    elif "-d" in sys.argv:
        create_directory(os.getcwd())
