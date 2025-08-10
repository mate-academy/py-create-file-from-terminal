import os
import sys
from datetime import datetime

def create_directory(path_parts):
    directory_path = os.path.join(*path_parts)
    os.makedirs(directory_path, exist_ok=True)
    print(f"Created directory: {directory_path}")

def create_file(file_name):
    with open(file_name, 'a+') as file:
        if os.stat(file_name).st_size == 0:
            file.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")
        else:
            file.write("\n\n" + datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")

        line_number = 1
        while True:
            content = input("Enter content line: ")
            if content.lower() == "stop":
                break
            file.write(f"{line_number} {content}\n")
            line_number += 1
    print(f"File created: {file_name}")

def main():
    if "-d" in sys.argv and "-f" in sys.argv:
        dir_index = sys.argv.index("-d") + 1
        file_index = sys.argv.index("-f") + 1
        create_directory(sys.argv[dir_index:file_index - 1])
        create_file(sys.argv[file_index])
    elif "-d" in sys.argv:
        dir_index = sys.argv.index("-d") + 1
        create_directory(sys.argv[dir_index:])
    elif "-f" in sys.argv:
        file_index = sys.argv.index("-f") + 1
        create_file(sys.argv[file_index])
    else:
        print("Invalid arguments. Usage: create_file.py -d <directory_path> or create_file.py -f <file_name>")

if __name__ == "__main__":
    main()
