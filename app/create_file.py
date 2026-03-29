import os
import sys
from datetime import datetime

def create_directory(path):
    os.makedirs(path, exist_ok=True)
    print(f"Directory '{path}' created.")

def create_file(file_path):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    content = f"{timestamp}\n"

    print("Enter content (type 'stop' to finish):")
    line_number = 1

    while True:
        line = input("Enter content line: ")
        if line.lower() == "stop":
            break
        content += f"{line_number} {line}\n"
        line_number += 1

    with open(file_path, "a") as file:
        file.write(content)

    print(f"Content added to '{file_path}'.")

def main():
    args = sys.argv

    if "-d" in args and "-f" in args:
        dir_index = args.index("-d")
        file_index = args.index("-f")

        directory_parts = args[dir_index + 1:file_index]
        file_name = args[file_index + 1]

        if all(isinstance(part, str) for part in directory_parts):
            directory = os.path.join(*directory_parts)
            create_directory(directory)
            create_file(os.path.join(directory, file_name))
        else:
            print("Invalid directory components.")

    elif "-d" in args:
        dir_index = args.index("-d")
        directory_parts = args[dir_index + 1:]
        if all(isinstance(part, str) for part in directory_parts):
            directory = os.path.join(*directory_parts)
            create_directory(directory)
        else:
            print("Invalid directory components.")

    elif "-f" in args:
        file_index = args.index("-f")
        file_name = args[file_index + 1]
        if isinstance(file_name, str):
            create_file(file_name)
        else:
            print("Invalid file name.")

if __name__ == "__main__":
    main()
