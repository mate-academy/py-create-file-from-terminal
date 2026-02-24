import os
import sys
import datetime


def create_file() -> None:
    if "-d" in sys.argv and "-f" in sys.argv:
        d_index = sys.argv.index("-d")
        f_index = sys.argv.index("-f")
        directory_path = sys.argv[d_index + 1:f_index]
        dir_path = os.path.join(*directory_path)
        os.makedirs(dir_path, exist_ok=True)
        file_path = sys.argv[f_index + 1]
        directory_path.append(file_path)
        full_file_path = os.path.join(*directory_path)
        with open(full_file_path, "a", encoding="utf-8") as f:
            f.write(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S\n"))
            while True:
                line = input("Enter content line: ")
                if line == "stop":
                    f.write("\n")
                    return
                f.write(line + "\n")
    elif "-d" in sys.argv and "-f" not in sys.argv:
        directory = sys.argv[2:]
        directory_path = os.path.join(*directory)
        os.makedirs(directory_path, exist_ok=True)
    elif "-f" in sys.argv and "-d" not in sys.argv:
        file_name = sys.argv[2]
        with open(file_name, "a", encoding="utf-8") as f:
            f.write(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S\n"))
            while True:
                line = input("Enter content line: ")
                if line == "stop":
                    f.write("\n")
                    return
                f.write(line + "\n")


if __name__ == "__main__":
    create_file()
