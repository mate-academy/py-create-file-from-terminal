import sys
import os
import datetime


def create_file() -> None:
    if "-d" in sys.argv:
        d_index = sys.argv.index("-d")
        dir_path = os.path.join(*sys.argv[d_index + 1:])
        os.makedirs(dir_path, exist_ok=True)
    elif "-f" in sys.argv:
        f_index = sys.argv.index("-f")
        file_name = sys.argv[f_index + 1]
        if os.path.isfile(file_name):
            with open(file_name, "a") as f:
                timestamp = (datetime.datetime.now()
                             .strftime("%Y-%m-%d %H:%M:%S"))
                f.write("\n")
                while True:
                    content_line = input("Enter content line: ")
                    if content_line == "stop":
                        break
                    f.write(f"{timestamp}\n{content_line}\n")
        else:
            with open(file_name, "w") as f:
                timestamp = (datetime.datetime.now()
                             .strftime("%Y-%m-%d %H:%M:%S"))
                f.write(f"{timestamp}\n")
                while True:
                    content_line = input("Enter content line: ")
                    if content_line == "stop":
                        break
                    f.write(f"{content_line}\n")
            print(f"File {file_name} created")
    elif "-h" in sys.argv or "--help" in sys.argv:
        print("Usage: python create_file.py [-d dir_path] [-f file_name]")
    else:
        print("Invalid arguments. Use -h or --help for help.")


if __name__ == "__main__":
    create_file()
