import os
import sys
from datetime import datetime


def create_directory(path_parts: str | list[str]) -> None:
    directory_path = os.path.join(*path_parts)
    try:
        os.makedirs(directory_path)
        print(f"Directory created: {directory_path}")
    except FileExistsError:
        print(f"Directory already exists: {directory_path}")


def create_file(file_name: str) -> None:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    line_count = 1
    content = []

    if os.path.exists(file_name):
        with open(file_name, 'r') as f:
            content.extend(f.read().splitlines())

    while True:
        line = input("Enter content line: ")
        if line.lower() == 'stop':
            break
        content.append(f"{line_count} {line}")
        line_count += 1

    with open(file_name, 'w') as f:
        f.write(timestamp + '\n')
        f.write('\n'.join(content))


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python create_file.py -d <directory_path> -f <file_name>")
        sys.exit(1)
    dir_path = None
    for arg in sys.argv[1:]:
        if arg == "-d" or arg == "-f":
            flag = arg
            if flag == "-d":
                if "-f" in sys.argv:
                    dir_path = sys.argv[2:sys.argv.index("-f")]
                else:
                    dir_path = sys.argv[2:]
                create_directory(" ".join(dir_path).split("/"))
            elif flag == "-f":
                file = sys.argv[sys.argv.index("-f") + 1]
                os.chdir("/".join(dir_path))
                create_file(file)
        elif not sys.argv.__contains__("-d") and not sys.argv.__contains__("-f"):
            print("Invalid flag. Use -d or -f.")
            sys.exit(1)
