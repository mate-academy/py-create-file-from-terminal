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


def get_file_name() -> str:
    if "-f" in sys.argv:
        file_index = sys.argv.index("-f") + 1
        if file_index < len(sys.argv):
            return sys.argv[file_index]
        else:
            print("Error: File name is missing after -f flag")
    else:
        print("Error: Use -f flag to specify the file name")


def create_file(directories: str, name: str) -> None:
    file_path = os.path.join(directories, name)
    key = "a" if os.path.exists(file_path) else "w"
    with open(file_path, key) as file:
        file.write(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S\n"))
        while True:
            text = input("Enter content line: ")
            if text == "stop":
                break
            file.write(f"{text}\n")


if __name__ == "__main__":
    directory = ""
    file_name = get_file_name()
    if "-d" in sys.argv:
        directory = create_directory()
    if "-f" in sys.argv:
        create_file(directory, file_name)
    else:
        print("Error: Use -b or -f flags")
