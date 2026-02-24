from datetime import datetime
import os
import sys


def main() -> None:
    args = sys.argv[1:]

    directory = None
    filename = None

    if "-d" in args:
        dir_index = args.index("-d")
        directory = " ".join(args[dir_index + 1:])
        for flag in ["-f"]:
            if flag in directory:
                directory = directory.split(flag)[0].strip()
                break

    if "-f" in args:
        file_index = args.index("-f")
        filename = " ".join(args[file_index + 1:])

    if directory is None:
        print("Error: Directory (-d) is required.")
        return
    if filename is None:
        print("Error: Filename (-f) is required.")
        return

    filepath = os.path.join(directory, filename)

    if not os.path.exists(directory):
        os.makedirs(directory)
        print(f"Directory '{directory}' created.")

    create_file(filepath)


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
            user_input = input("Enter content line "
                               "(or type 'stop' to finish): ")
            if user_input.lower() == "stop":
                break
            file.write(f"{line_number} {user_input}\n")
            line_number += 1

    if file_exists:
        print(f"Appended to the existing file: {filepath}")
    else:
        print(f"Created new file: {filepath}")


if __name__ == "__main__":
    main()
