from datetime import datetime
import os
import sys


def main() -> None:
    args = sys.argv[1:]

    if "-d" in args and "-f" in args:
        dir_index = args.index("-d")
        file_index = args.index("-f")
        directory = os.path.join(*args[dir_index + 1:file_index])
        filename = args[file_index + 1]
        filepath = os.path.join(directory, filename)

        if not os.path.exists(directory):
            os.makedirs(directory)

        create_file(filepath)

    elif "-d" in args:
        directory = os.path.join(*args[args.index("-d") + 1:])
        if not os.path.exists(directory):
            os.makedirs(directory)

    elif "-f" in args:
        filename = args[args.index("-f") + 1]
        create_file(filename)

    else:
        print("Invalid arguments provided. Please use -d for directory or -f for file.")


def create_file(filepath: str) -> None:
    file_exists = os.path.exists(filepath)
    with open(filepath, "a+") as file:
        file.seek(0)
        content = file.read()

        if content.strip():
            file.write("\n")

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"{timestamp}\n")

        line_number = 1
        while True:
            user_input = input("Enter content line (or type 'stop' to finish): ")
            if user_input.lower() == "stop":
                break
            file.write(f"{line_number} {user_input}\n")
            line_number += 1


if __name__ == "__main__":
    main()
