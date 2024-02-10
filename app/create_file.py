import os
import sys

from datetime import datetime


def file_create(path, file_name):
    with open(path + file_name, "a") as f:
        current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(current_date + "\n")
        count = 1

        while True:
            content_line = input("Enter content line: ")

            if content_line == "stop":
                f.write("\n")
                exit()

            else:
                f.write(f"{count} {content_line}\n")
                count += 1


def check_path(path):
    if not os.path.exists(path):
        os.makedirs(path)
    return path


def main():
    if "-d" in sys.argv and "-f" in sys.argv:
        path = check_path(os.sep.join(sys.argv[3:len(sys.argv) - 1]) + os.sep)
        file_name = sys.argv[-1]
        file_create(path, file_name)
    elif "-d" in sys.argv:
        path = check_path(os.sep.join(sys.argv[2:]))
        os.mkdir(path)
    elif "-f" in sys.argv:
        path = ""
        file_name = sys.argv[-1]
        file_create(path, file_name)


if __name__ == "__main__":
    main()
