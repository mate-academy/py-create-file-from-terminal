import sys
import os
from datetime import datetime
from typing import List


def get_timestamp() -> str:
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def collect_content() -> List[str]:
    lines: List[str] = []
    counter: int = 1
    while True:
        line: str = input("Enter content line: ")
        if line.strip().lower() == "stop":
            break
        lines.append(f"{counter} {line}")
        counter += 1
    return lines


def main() -> None:
    args: List[str] = sys.argv[1:]

    if "-d" in args:
        d_index: int = args.index("-d")
        dirs: List[str] = []
        for arg in args[d_index + 1:]:
            if arg.startswith("-"):
                break
            dirs.append(arg)
        if dirs:
            os.makedirs(os.path.join(*dirs), exist_ok=True)
            base_path: str = os.path.join(*dirs)
        else:
            base_path: str = "."
    else:
        base_path: str = "."

    if "-f" in args:
        f_index: int = args.index("-f")
        try:
            filename: str = args[f_index + 1]
        except IndexError:
            print("Error: Missing filename after -f")
            return

        file_path: str = os.path.join(base_path, filename)

        add_separator: bool = os.path.exists(file_path) and os.path.getsize(file_path) > 0

        with open(file_path, "a", encoding="utf-8") as file:
            if add_separator:
                file.write("\n")
            file.write(f"{get_timestamp()}\n")
            for line in collect_content():
                file.write(f"{line}\n")
    else:
        print(f"Directory created at: {base_path}")


if __name__ == "__main__":
    main()
