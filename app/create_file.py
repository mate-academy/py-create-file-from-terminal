import sys
import os

from datetime import datetime


def create_directory(path_parts: list[str]) -> str | None:
    if path_parts:
        dir_path = os.path.join(*path_parts)
        os.makedirs(dir_path, exist_ok=True)
        return dir_path
    return None


def create_file(file_name: str, dir_path: str | None) -> str | None:
    if file_name:
        if dir_path is not None:
            file_path = os.path.join(dir_path, file_name)
        else:
            file_path = file_name

        file_exists = os.path.exists(file_path)

        with open(file_path, "a") as file:
            if file_exists:
                file.write("\n\n")
            file.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")
            lines = get_content()
            file.write(
                "\n".join(f"{i + 1} {line}" for i, line in enumerate(lines))
            )

        return file_path

    return None


def get_content() -> list:
    lines = []
    while True:
        line = input("Enter content line: ")
        if line.lower() == "stop":
            break
        lines.append(line)
    return lines


def main() -> None:
    args = sys.argv[1:]
    path_parts = []
    file_name = None

    if "-d" in args and "-f" in args:
        dir_index = args.index("-d")
        file_index = args.index("-f")
        file_name = args[file_index + 1]
        if dir_index < file_index:
            path_parts = args[dir_index + 1:file_index]
        else:
            path_parts = args[dir_index + 1:]
    elif "-d" in args:
        dir_index = args.index("-d")
        path_parts = args[dir_index + 1:]
    elif "-f" in args:
        file_index = args.index("-f")
        file_name = args[file_index + 1]

    dir_path = create_directory(path_parts)
    create_file(file_name, dir_path)


if __name__ == "__main__":
    main()
