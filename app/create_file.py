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
    try:
        flag_d = sys.argv.index("-d")
        flag_f = sys.argv.index("-f")
    except ValueError:
        try:
            flag_d = sys.argv.index("-d")
        except ValueError:
            try:
                flag_f = sys.argv.index("-f")
            except ValueError:
                print("Invalid flag. Use either -d or -f.")
                sys.exit(1)
            else:
                file_name = sys.argv[flag_f + 1]
                if os.path.exists(file_name):
                    print(
                        f"File '{file_name}' already exists."
                        f"Appending content below:"
                    )
                else:
                    print(f"Creating new file: {file_name}")
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                with open(file_name, "a") as file:
                    file.write(f"\n\n{timestamp}\n")
                    create_file(file_name)
        else:
            path_parts = sys.argv[flag_d + 1:]
            create_directory(path_parts)
    else:
        path_parts = sys.argv[flag_d + 1: flag_f]
        create_directory(path_parts)
        file_name = sys.argv[flag_f + 1]
        if os.path.exists(file_name):
            print(
                f"File '{file_name}' already exists."
                f"Appending content below:"
            )
        else:
            print(f"Creating new file: {file_name}")
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(file_name, "a") as file:
            file.write(f"\n\n{timestamp}\n")
            create_file(file_name)


if __name__ == "__main__":
    main()
