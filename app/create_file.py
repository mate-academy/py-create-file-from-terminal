import sys
import os
import datetime


def create_directory() -> str:
    start_index = sys.argv.index("-d") + 1
    try:
        end_index = sys.argv.index("-f")
    except ValueError:
        end_index = len(sys.argv)
    directories = os.path.join(*sys.argv[start_index: end_index])
    os.makedirs(directories, exist_ok=True)
    return f"{directories}\\"


def create_file(directories: str = "") -> None:
    if "-f" in sys.argv:
        file_index = sys.argv.index("-f") + 1
        if file_index < len(sys.argv):
            file_name = sys.argv[file_index]
        else:
            print("Error: File name is missing after -f flag")
            return
    else:
        print("Error: Use -f flag to specify the file name")
        return
    file_path = os.path.join(directories, file_name)
    key = "a" if os.path.exists(file_path) else "w"
    with open(file_path, key) as file:
        file.write(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S\n"))
        while True:
            test = input("Enter content line: ")
            if test == "stop":
                break
            file.write(f"{test}\n")


if __name__ == "__main__":
    directory = ""
    if "-d" in sys.argv:
        directory = create_directory()
    if "-f" in sys.argv:
        create_file(directory)
    else:
        print("Error: Use -b or -f flags")
