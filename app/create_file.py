import sys
import os
import datetime


def create_directory(directory: str) -> None:
    if not os.path.exists(directory):
        os.makedirs(directory)
        print(f"Directory '{directory}' created.")


def create_file(directory: str, filename: str) -> None:
    content = []
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    while True:
        line = input(f"{len(content) + 1} ")
        if line.lower() == "stop":
            break
        content.append(line)

    with open(os.path.join(directory, filename), "a") as file:
        file.write(current_time + "\n")
        for i, line in enumerate(content):
            file.write(f"{i + 1} {line}\n")


def main() -> None:
    if len(sys.argv) < 5:
        print("Incorrect format. Please use -d and -f "
              "flags to create a directory and a file with content.")
        return

    if "-d" not in sys.argv or "-f" not in sys.argv:
        print("Both -d and -f flags are "
              "required to create a directory and a file.")
        return

    dir_index = sys.argv.index("-d") + 1
    directory = sys.argv[dir_index]
    file_index = sys.argv.index("-f") + 1
    filename = sys.argv[file_index]

    create_directory(directory)
    create_file(directory, filename)


if __name__ == "__main__":
    main()
