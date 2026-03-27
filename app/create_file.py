import os
import sys
from datetime import datetime


def create_directory(directory_path: str) -> None:
    os.makedirs(directory_path, exist_ok=True)
    print(f"Directory '{directory_path}' created.")


def write_content_to_file(file_path: str, content_lines: list[str]) -> None:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    content = [f"{timestamp}"] + [
        f"{i} {line}" for i, line in enumerate(content_lines, 1)
    ]

    file_exists_and_not_empty = (os.path.exists(file_path)
                                 and os.path.getsize(file_path) > 0)

    with open(file_path, "a") as file:
        if file_exists_and_not_empty:
            file.write("\n")
        file.write("\n".join(content) + "\n")


# noinspection PyTypeChecker
def main() -> None:
    args = sys.argv[1:]
    if not args:
        print(
            "Usage: python create_file.py [-d directory_path] [-f file_name]"
        )
        return

    if "-f" in args and "-d" in args:
        f_index = args.index("-f")
        d_index = args.index("-d")
        if f_index < d_index:
            directory_path = os.path.join(*args[d_index + 1:])
            file_name = args[f_index + 1]
        else:
            directory_path = os.path.join(*args[d_index + 1:f_index])
            file_name = args[f_index + 1]

        # noinspection PyTypeChecker
        create_directory(directory_path)

        content_lines = []
        print("Enter content line (input 'stop' to finish):")
        while True:
            line = input()
            if line.strip() == "stop":
                break
            content_lines.append(line)

        file_path = os.path.join(directory_path, file_name)
        write_content_to_file(file_path, content_lines)
        print(f"File '{file_name}' created in directory '{directory_path}'.")

    elif "-d" in args:
        dir_index = args.index("-d") + 1
        directory_path = os.path.join(*args[dir_index:])
        create_directory(directory_path)

    elif "-f" in args:
        file_index = args.index("-f") + 1
        file_name = args[file_index]
        file_path = os.path.join(os.getcwd(), file_name)

        content_lines = []
        print("Enter content line (input 'stop' to finish):")
        while True:
            line = input()
            if line.strip() == "stop":
                break
            content_lines.append(line)

        write_content_to_file(file_path, content_lines)
        print(f"File '{file_name}' created in current directory.")


if __name__ == "__main__":
    main()
