import os
import sys
from datetime import datetime


def create_file(filename: str, content_lines: list) -> None:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    content = [f"{timestamp}"]
    content.extend(f"{i + 1} {line}" for i, line in enumerate(content_lines))
    content = "\n".join(content)

    if os.path.exists(filename):
        with open(filename, "a") as f:
            f.write("\n\n" + content)
    else:
        with open(filename, "w") as f:
            f.write(content)


def main() -> None:
    args = sys.argv[1:]
    dir_path = ""

    if "-d" in args:
        dir_index = args.index("-d")
        if "-f" in args:
            f_flag = args.index("-f")
            dir_names = args[dir_index + 1:f_flag]
        else:
            dir_names = args[dir_index + 1:]
        dir_path = os.path.join(*dir_names)
        os.makedirs(dir_path, exist_ok=True)

    if "-f" in args:
        file_index = args.index("-f")
        file_name = args[file_index + 1]
        content_lines = []
        while True:
            line = input("Enter content line: ")
            if line == "stop":
                break
            content_lines.append(line)

        create_file(os.path.join(dir_path, file_name), content_lines)


if __name__ == "__main__":
    main()
