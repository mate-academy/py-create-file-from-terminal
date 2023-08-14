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
    file_name = sys.argv[2]
    create_file(file_name)
    line = "  "
    content = ""
    number_line = 0
    while line != "stop":
        number_line += 1
        line = input("Enter content line: ")
        if line != "stop":
            with open(file_name, "r") as f:
                lines = len(f.readlines())
            if lines > 1:
                lines = "Another line"
            else:
                lines = "Line"
            line = f"{number_line} {lines} {number_line} content \n"
            print(f"{lines} {number_line} content")
            content += line
    with open(file_name, "a") as f:
        f.write("".join(content))


if len(sys.argv) >= 4 and sys.argv[1] == "-d":
    if os.path.join(sys.argv[-2]) != "-f":
        directory_path = os.path.join(*sys.argv[2:])
        if not os.path.exists(directory_path):
            os.makedirs(directory_path)

    else:
        file_name = sys.argv[-1]
        directory_path = os.path.join(*sys.argv[2:-2])
        file_path = os.path.join(directory_path, file_name)
        target_directory = os.path.join(*sys.argv[2:-2])
        if not os.path.exists(directory_path):
            os.makedirs(directory_path)
        os.chdir(target_directory)
        make_file(file_path)


elif len(sys.argv) == 3 and sys.argv[1] == "-f":
    file_path = sys.argv[2]
    file_name = sys.argv[2]
    make_file(file_path)


if __name__ == "__main__":
    file_content()
