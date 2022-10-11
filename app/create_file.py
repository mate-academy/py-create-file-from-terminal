import os
import sys
import datetime


def file_content() -> str:
    print(sys.argv)
    xx = datetime.datetime.now()
    time_print = xx.strftime("%Y-%m-%d %X\n")
    return time_print


def create_file(file_name: str) -> None:
    with open(file_name, "a") as file:
        file.write(file_content())


def make_file(file_path: str) -> None:
    create_file(file_name)
    line = "  "
    content = ""
    nn = 0
    while line != "stop":
        nn += 1
        line = input("Enter content line: ")
        if line != "stop":
            with open("file.txt", "r") as f:
                contente = f.read()
            if contente:
                line = f"{nn} Another line{nn} content \n"
                print(f"Line{nn} content")
                content += line
            else:
                line = f"{nn} Line{nn} content \n"
                print(f"Line{nn} content")
                content += line

    with open("file.txt", "a") as f:
        f.write("".join(content))


if len(sys.argv) >= 4 and sys.argv[1] == "-d":
    directory_path = os.path.join(*sys.argv[2:4])
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)

    if len(sys.argv) >= 6 and sys.argv[4] == "-f":
        file_name = sys.argv[5]
        file_path = os.path.join(directory_path, file_name)
        target_directory = "dir1\\dir2"
        os.chdir(target_directory)
        make_file(file_path)


elif len(sys.argv) == 3 and sys.argv[1] == "-f":
    file_path = sys.argv[2]
    file_name = "file.txt"
    make_file(file_path)


def ttt() -> str:
    print(sys.argv)
    xx = datetime.datetime.now()
    print(xx.strftime("%Y-%m-%d %X"))


if __name__ == "__main__":
    ttt()
