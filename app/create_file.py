import os
import sys
import datetime


def create_file() -> None:
    with open(sys.argv[-1], "a") as f:
        f.write(str(datetime.datetime.now()
                    .strftime("%Y-%m-%d %H:%M:%S")) + "\n")
        file_contents = input("Enter content line: ")
        number_of_lines = 1

        while file_contents != "stop":
            f.write(f"{number_of_lines} {file_contents}\n")
            file_contents = input("Enter content line: ")
            number_of_lines += 1
        f.write("\n")


def create_directories(directory_list):
    directory_path = "/".join(directory_list)
    os.makedirs(directory_path)
    os.chdir(directory_path)


def make_dirs_and_create_file() -> None:
    if "-d" in sys.argv and "-f" in sys.argv:
        create_directories(sys.argv[2:-2])
        create_file()
    elif "-d" in sys.argv:
        create_directories(sys.argv[2:])
    elif "-f" in sys.argv:
        create_file()


if __name__ == "__main__":
    make_dirs_and_create_file()
