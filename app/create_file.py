import os
import sys
from datetime import datetime


def create_directory(path_parts: list[str]) -> None:
    directory_path = os.path.join(*path_parts)
    os.makedirs(directory_path, exist_ok=True)
    print(f"Created directory: {directory_path}")


def create_file(file_name: str) -> None:
    try:
        with open(file_name, "a") as file:
            print(f"Created file: {file_name}")
            print("Enter content lines (type 'stop' to finish):")
            while True:
                line = input("Enter content line: ")
                if line.lower() == "stop":
                    break
                file.write(line + "\n")
    except Exception as e:
        print(f"Error creating file: {e}")


def main() -> None:
    if len(sys.argv) < 3:
        print("Usage: python create_file.py [-d path_parts] [-f file_name]")
        sys.exit(1)

    flag = sys.argv[1]
    if flag == "-d":
        path_parts = sys.argv[2:]
        create_directory(path_parts)
    elif flag == "-f":
        file_name = sys.argv[2]
        if os.path.exists(file_name):
            print(
                f"File '{file_name}' already exists. Appending content below:"
            )
        else:
            print(f"Creating new file: {file_name}")
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(file_name, "a") as file:
            file.write(f"\n\n{timestamp}\n")
            create_file(file_name)
    else:
        print("Invalid flag. Use either -d or -f.")
        sys.exit(1)


if __name__ == "__main__":
    main()
