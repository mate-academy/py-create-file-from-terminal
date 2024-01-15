import os
from sys import argv
from datetime import datetime


def create_directory(destination: str) -> None:
    try:
        os.makedirs(destination, exist_ok=True)
        print(f"Directory '{destination}' created successfully.")
    except FileExistsError:
        print(f"Directory {destination} already exists.")


def create_file(filename: str) -> None:
    try:
        with open(filename, "a") as file:
            print(f"File '{filename}' created successfully.")
            print("Input content (type 'stop' to finish):")
            current_date = datetime.now().strftime("%Y/%B/%d %I:%M:%S")
            content = f"{current_date}\n"
            while True:
                line = input()
                if line.lower() == "stop":
                    break
                content += line + "\n"
            file.write(content)
            print(f"Content written to '{filename}'.")
    except Exception as e:
        print(f"An error occurred: {e}")


def creator() -> None:
    if "-d" in argv and "-f" in argv:
        dir_index = argv.index("-d")
        file_index = argv.index("-f")
        dir_path = os.path.join(*argv[dir_index + 1:])
        file_path = os.path.join(*argv[file_index + 1:])
        if dir_index < file_index:
            directory_path = os.path.join(*argv[dir_index + 1:file_index])
            create_directory(directory_path)
            create_file(os.path.join(directory_path, file_path))
        else:
            f_path = os.path.join(*argv[file_index + 1:dir_index])
            create_directory(dir_path)
            create_file(os.path.join(dir_path, f_path))
    elif "-d" in argv:
        create_directory(os.path.join(*argv[2:]))
    elif "-f" in argv:
        create_file(os.path.join(*argv[2:]))


if __name__ == "__main__":
    creator()
