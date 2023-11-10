from sys import argv
import datetime
import os


def find_path_and_file_name() -> tuple:
    path = []
    file_name = ""
    if "-d" in argv and "-f" not in argv:
        path = argv[argv.index("-d") + 1:]
    if "-d" in argv and "-f" in argv:
        path = argv[argv.index("-d") + 1: argv.index("-f")]
        file_name += argv[-1]
    elif "-f" in argv:
        file_name += argv[-1]
    path = "/".join(path)
    return path, file_name


def make_file() -> None:
    directory, file_name = find_path_and_file_name()
    date = datetime.datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    )
    if directory:
        path = os.getcwd() + "\\" + directory + "/"
        if not os.path.exists(path):
            os.makedirs(path)
            os.chdir(path)
        else:
            print("This directory already exists")

    try:
        with open(file_name, "a") as text:
            text.write(date + "\n")
            count_lines = 0
            while True:
                user_input = input("Enter content line: ")
                count_lines += 1
                if user_input == "stop":
                    text.write("\n")
                    break
                text.write(str(count_lines) + " " + user_input + "\n")
    except FileNotFoundError:
        print("file does not exist")


if __name__ == "__main__":
    make_file()
