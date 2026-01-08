import sys
import os
from datetime import datetime


def main() -> None:
    args = sys.argv[1:]

    dir_parts: list[str] = []
    file_name: str | None = None

    if "-d" in args:
        index_d = args.index("-d")
        for arg in args[index_d + 1:]:
            if arg == "-f":
                break
            dir_parts.append(arg)

    if "-f" in args:
        index_f = args.index("-f")
        if index_f + 1 < len(args):
            file_name = args[index_f + 1]

    path = ""
    if dir_parts:
        path = os.path.join(*dir_parts)
        os.makedirs(path, exist_ok=True)

    if file_name:
        file_path = os.path.join(path, file_name) if path else file_name
        with open(file_path, "a", encoding="utf-8") as f:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            f.write(f"{timestamp}\n")
            line_number = 1
            while True:
                line = input("Enter content line: ")
                if line.strip().lower() == "stop":
                    break
                f.write(f"{line_number} {line}\n")
                line_number += 1


if __name__ == "__main__":
    main()
