import os
import sys
from datetime import datetime


def create_file(directory: str, filename: str) -> None:
    filepath = os.path.join(directory, filename)
    if os.path.exists(filepath):
        mode = "a"
    else:
        mode = "w"

    with open(filepath, mode) as file:
        if mode == "a":
            file.write("\n\n")

        file.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")

        line_number = 1
        while True:
            content = input(f"Enter content line {line_number}: ")
            if content.lower() == "stop":
                break
            file.write(f"{line_number} {content}\n")
            line_number += 1


def create_directory(directory_path: str) -> None:
    try:
        os.makedirs(directory_path)
    except FileExistsError:
        print(f'Directory "{directory_path}" already exists.')
    except Exception as e:
        print(f"An error occurred: {e}")


def main() -> None:
    if len(sys.argv) < 3:
        print("Usage: python create_file.py -d <directory_path> -f <filename>")
        return

    flag = sys.argv[1]
    if flag == "-d":
        directory_path = os.path.join(*sys.argv[2:])
        create_directory(directory_path)
    elif flag == "-f":
        filename = sys.argv[2]
        create_file(".", filename)
    elif flag == "-h":
        print("Usage: python create_file.py -d <directory_path> -f <filename>")
        print("Flags:")
        print("-d: Create directory")
        print("-f: Create file")
    else:
        print("Invalid flag. Use -h for help.")


if __name__ == "__main__":
    main()
