import os
from datetime import datetime
import sys


def create_new_directory_cli(path_of_directories: list) -> str:
    path = os.path.join(*path_of_directories)
    try:
        os.makedirs(path, exist_ok=True)
        print(f"Directory '{path}' created or already exists.")
        return path
    except Exception as e:
        print(f"Error creating directory: {e}")
        return ""


def create_file_cli(file_name: str, directory: str) -> None:
    try:
        if directory:
            file_name = os.path.join(directory, file_name)

        with open(file_name, "a") as file:
            if os.path.getsize(file_name) > 0:
                file.write("\n")
            file.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            counter = 1
            while True:
                new_line = input("Enter content line: ")
                if new_line.lower() == "stop":
                    break
                file.write(f"{counter} {new_line}\n")
                counter += 1
        print(f"Content added to file '{file_name}'.")
    except Exception as e:
        print(f"Error writing to file: {e}")


def main() -> None:
    print("Starting...")
    directory = ""

    if "-d" in sys.argv:
        d_index = sys.argv.index("-d") + 1
        directories = []
        while d_index < len(sys.argv) and not sys.argv[d_index].startswith("-"):
            directories.append(sys.argv[d_index])
            d_index += 1
        if directories:
            directory = create_new_directory_cli(directories)

    if "-f" in sys.argv:
        f_index = sys.argv.index("-f") + 1
        if f_index < len(sys.argv):
            create_file_cli(sys.argv[f_index], directory)

    print("Finished.")


if __name__ == "__main__":
    main()
