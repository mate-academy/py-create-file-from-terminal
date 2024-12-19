import sys
import os
from datetime import datetime


def create_file_with_content(file_path: str) -> None:
    timestomp = datetime.now()
    timestomp = timestomp.strftime("%Y-%m-%d %H:%M:%S")
    print("Enter content (typing 'stop' to finish)")
    while True:
        input_line = input("Input content: ")
        if input_line.lower() == "stop":
            break
        if os.path.exists(file_path):
            with open(file_path, "a") as file:
                file.write(input_line + "\n")
            print(f"File updated at: {file_path}")
        else:
            with open(file_path, "w") as file:
                file.write(f"{timestomp}\n{input_line}\n")
            print(f"File created at: {file_path}")


def main() -> None:
    args = sys.argv[1:]
    dir_path = os.getcwd()
    file_name = "NewTextFile.txt"
    if not args:
        print("No arguments. Use -d for show path or -f to show file ")
        return
    if "-d" in args:
        dir_index = args.index("-d")
        if "-f" in args:
            file_index = args.index("-f")
            dir_path = os.path.join(*args[dir_index + 1:file_index])
        else:
            dir_path = os.path.join(*args[dir_index + 1:])

        if dir_path:
            if os.path.exists(dir_path):
                print(f"{dir_path}, is already created")
            else:
                os.makedirs(dir_path, exist_ok=True)
                print(f"Directory created: {dir_path}")

    if "-f" in args:
        file_index = args.index("-f")
        if len(args) > file_index + 1:
            file_name = args[file_index + 1]

        if os.path.exists(dir_path):
            file_path = os.path.join(dir_path, file_name)
        else:
            file_path = file_name

        create_file_with_content(file_path)


if __name__ == "__main__":
    main()
