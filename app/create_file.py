import os
import sys
from datetime import datetime


def create_file(file_path: str) -> None:
    with open(file_path, "a") as file:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"\n{timestamp}\n")

        print("(to stop the program write 'stop')")
        line_counter = 1
        while True:
            line = input("Enter content line: ")
            if line.lower() == "stop":
                file.write("\n")
                break
            file.write(f"{line_counter} {line}\n")
            line_counter += 1

    print(f"File {file_path} created successfully.")


def main() -> None:
    directory_path = ""
    args = sys.argv[1:]
    if not args:
        raise ValueError("No arguments provided. Use '-d' to create "
                         "directories or '-f' to create a file.")

    if "-d" in args:
        dir_index = args.index("-d") + 1
        directory_parts = []
        while dir_index < len(args):
            directory_parts.append(args[dir_index])
            dir_index += 1
        os.makedirs(os.path.join(*directory_parts))
        print(f"{directory_path} directory created.")

    if "-f" in args:
        file_index = args.index("-f") + 1
        if file_index < len(args):
            file_name = args[file_index]
            file_path = os.path.join(directory_path, file_name)
            create_file(file_path)
        else:
            raise ValueError("Please write a file name after '-f'.")

    if not "-d" and "-f" not in args:
        raise ValueError("Neither '-d' nor '-f' flag provided.")


if __name__ == "__main__":
    try:
        main()
    except ValueError as e:
        print(f"Error: {e}")
