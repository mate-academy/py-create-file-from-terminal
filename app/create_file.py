import os
import sys
from datetime import datetime


def create_directory(path: str) -> None:
    try:
        os.makedirs(path)
        print(f"Directory {path} created successfully.")
    except FileExistsError:
        print(f"Directory {path} already exists.")


def create_file(file_path: str) -> None:
    try:
        with open(file_path, "a") as file:
            while True:
                line = input("Enter content line: ")
                if line.lower() == "stop":
                    break
                file.write(f"{line}\n")
    except Exception as e:
        print(f"Error: {e}")


def main() -> None:
    if len(sys.argv) < 3:
        print(
            "Usage: python create_file.py [-d directory_path] [-f file_name]"
        )
        sys.exit(1)
    if sys.argv[1] == "-d":
        directory_path = os.path.join(*sys.argv[2:])
        create_directory(directory_path)
    elif sys.argv[1] == "-f":
        file_name = sys.argv[2]
        file_path = os.path.join(os.getcwd(), file_name)

        if os.path.exists(file_path):
            print(f"File {file_path} already exists. Appending content.")
        else:
            with open(file_path, "w") as file:
                file.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")
        create_file(file_path)
    elif sys.argv[1] == "-d" and sys.argv[3] == "-f":
        directory_path = os.path.join(*sys.argv[2:-2])
        file_name = sys.argv[-1]
        file_path = os.path.join(directory_path, file_name)
        create_directory(directory_path)
        create_file(file_path)
    else:
        print("Invalid arguments. Use -d or -f flags.")
        sys.exit(1)


if __name__ == "__main__":
    main()
