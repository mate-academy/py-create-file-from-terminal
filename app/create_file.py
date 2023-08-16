import os
import sys
import datetime


def file_content() -> str:
    print(sys.argv)
    datetime_now = datetime.datetime.now()
    return datetime_now.strftime("%Y-%m-%d %X\n")


def create_file(file_name: str) -> None:
    with open(file_name, "a") as file:
        file.write(file_content())


def make_file(file_path: str) -> None:
    file_name = os.path.basename(file_path)
    create_file(file_name)
    line = "  "
    content = ""
    number_line = 0
    while line != "stop":
        number_line += 1
        line = input(f"Enter content line: {line}")
        if line != "stop":
            line = (f"{number_line} Line{number_line} content\n")
            content += line
            print(content)

    with open(file_name, "a") as f:
        f.write(content)


if "-f" in sys.argv and "-d" in sys.argv:
    if sys.argv[1] == "-d":
        directory_path = os.path.join(*sys.argv[2:-2])
        os.makedirs(directory_path, exist_ok=True)
        os.chdir(directory_path)
        file_path = sys.argv[-1]
    else:
        directory_path = os.path.join(*sys.argv[4:])
        os.makedirs(directory_path, exist_ok=True)
        os.chdir(directory_path)
        file_path = sys.argv[2]
    make_file(file_path)


elif "-d" in sys.argv:
    directory_path = os.path.join(*sys.argv[2:])
    os.makedirs(directory_path, exist_ok=True)


elif "-f" in sys.argv:
    file_path = sys.argv[2]
    make_file(file_path)


if __name__ == "__main__":
    file_content()
