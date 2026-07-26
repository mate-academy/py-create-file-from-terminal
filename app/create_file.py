import os
import sys

from datetime import datetime


def create_directory(directory: list[str]) -> str:
    directory_path = os.path.join(*directory)
    os.makedirs(directory_path, exist_ok=True)
    return directory_path


def create_file(
        directory: list[str],
        file_name: str,
        file_content: str
) -> None:

    if directory:
        new_dir = create_directory(directory)
        path = os.path.join(new_dir, file_name)
    else:
        path = file_name

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(path, "a+") as file:
        if os.path.getsize(path) == 0:
            file.write(timestamp)
        else:
            file.write("\n\n" + timestamp)
        for num, line in enumerate(file_content.splitlines(), 1):
            file.write(f"\n{num} {line}")


def main() -> None:
    directory_path = None
    file_name = None

    if "-d" in sys.argv:
        dir_index = sys.argv.index("-d") + 1
        directory_path = sys.argv[dir_index:]
        if "-f" not in sys.argv:
            create_directory(directory_path)
            return

    if "-f" in sys.argv:
        file_index = sys.argv.index("-f") + 1
        file_name = sys.argv[file_index]

    if "-d" in sys.argv and "-f" in sys.argv:
        dir_index = sys.argv.index("-d") + 1
        file_index = sys.argv.index("-f") + 1

        if dir_index < file_index:
            directory_path = sys.argv[dir_index:file_index - 1]
        else:
            directory_path = sys.argv[dir_index:]

    file_content = ""

    while True:
        line = input("Enter content line: ")
        if line == "stop":
            break

        file_content += line + "\n"

    create_file(directory_path, file_name, file_content)


if __name__ == "__main__":
    main()
