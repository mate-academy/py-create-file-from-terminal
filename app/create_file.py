import sys
import os
from datetime import datetime


def create_directory(path_parts: list[str]) -> str:
    """Creates a directory from given path parts."""
    dir_path = os.path.join(*path_parts)
    os.makedirs(dir_path, exist_ok=True)
    print(f"Directory '{dir_path}' created or already exists.")
    return dir_path


def get_file_content() -> list[str]:
    """Gets content from user input until 'stop' is entered."""
    lines = []
    print("Enter content line (type 'stop' to finish):")
    while True:
        line = input("Enter content line: ")
        if line.strip().lower() == "stop":
            break
        lines.append(line)
    return lines


def write_to_file(file_path: str, content: list[str]) -> None:
    """Writes content to a file, adding a timestamp and numbering lines."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    numbered_content = "\n".join(f"{i + 1} {line}" for i, line
                                 in enumerate(content))

    with open(file_path, "a", encoding="utf-8") as file:
        if os.path.getsize(file_path) > 0:
            file.write("\n\n")
        file.write(f"{timestamp}\n{numbered_content}")
    print(f"Content written to '{file_path}'.")


def main() -> None:
    """Main function to parse arguments and execute corresponding actions."""
    args = sys.argv[1:]
    if not args:
        print("Usage: python create_file.py -d <directories> -f <filename>")
        return

    dir_path = ""
    file_name = ""

    if "-d" in args:
        d_index = args.index("-d")
        if "-f" in args:
            f_index = args.index("-f")
            dir_path = create_directory(args[d_index + 1:f_index])
            file_name = args[f_index + 1] if len(args) > f_index + 1 else ""
        else:
            create_directory(args[d_index + 1:])
            return
    elif "-f" in args:
        f_index = args.index("-f")
        file_name = args[f_index + 1] if len(args) > f_index + 1 else ""

    if file_name:
        full_path = os.path.join(dir_path, file_name)\
            if dir_path else file_name
        content = get_file_content()
        write_to_file(full_path, content)
    else:
        print("Error: No file name provided.")
        return


if __name__ == "__main__":
    main()
