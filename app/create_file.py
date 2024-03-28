import os
import sys
from datetime import datetime


def collect_content():
    content_lines = []
    line_number = 1
    while True:
        content = input(f"Enter content line {line_number} (type 'stop' to finish): ")
        if content.lower() == "stop":
            break
        content_lines.append((line_number, content))
        line_number += 1
    return content_lines


def create_file(directory: str, filename: str) -> None:
    filepath = os.path.join(directory, filename)

    content_lines = collect_content()

    with open(filepath, "a") as file:
        file.write("\n\n")
        file.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")
        for line_number, content in content_lines:
            file.write(f"{line_number} {content}\n")


def create_directory(directory_path: str) -> None:
    try:
        os.makedirs(directory_path, exist_ok=True)
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
    else:
        print("Invalid flag. Use -h for help.")


if __name__ == "__main__":
    main()
