import os
import sys
import datetime


def create_file(directory: list[str], filename: str) -> None:
    if directory:
        dir_path = os.path.join(*directory)
        os.makedirs(dir_path, exist_ok=True)
        file_path = os.path.join(dir_path, filename)
    else:
        file_path = filename

    content = []
    while True:
        line = input("Enter content line: ")
        if line.lower() == "stop":
            break
        content.append(line)

    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    numbered_content = [f"{i + 1} {line}" for i, line in enumerate(content)]

    if os.path.exists(file_path):
        with open(file_path, "a") as f:
            f.write(f"\n{timestamp}\n")
            f.write("\n".join(numbered_content) + "\n")
    else:
        with open(file_path, "w") as f:
            f.write(f"{timestamp}\n")
            f.write("\n".join(numbered_content) + "\n")


if __name__ == "__main__":
    directory = []
    filename = None

    if "-d" in sys.argv:
        dir_index = sys.argv.index("-d") + 1
        if "-f" in sys.argv:
            file_index = sys.argv.index("-f")
            directory = sys.argv[dir_index:file_index]
            filename = sys.argv[file_index + 1]
        else:
            print("Error: No filename provided.")
            sys.exit(1)
    elif "-f" in sys.argv:
        file_index = sys.argv.index("-f") + 1
        filename = sys.argv[file_index]

    if directory and filename:
        create_file(directory, filename)
    elif filename:
        create_file([], filename)
    else:
        print("Invalid arguments. Please use -d or -f flags.")
