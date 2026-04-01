import os
import sys
from datetime import datetime


def main() -> None:
    args = sys.argv[1:]
    has_d = False
    has_f = False
    if "-d" in args:
        has_d = True
    if "-f" in args:
        has_f = True

    file_name = ""

    if has_f:
        f_index = args.index("-f")
        if f_index + 1 < len(args) and args[f_index + 1] not in ["-d", "-f"]:
            file_name = args[f_index + 1]

    dir_parts = []

    if has_d:
        d_index = args.index("-d")

        for arg in args[d_index + 1:]:
            if arg in ["-f", "-d"]:
                break
            dir_parts.append(arg)

    if dir_parts:
        path = os.path.join(*dir_parts)
        os.makedirs(path, exist_ok=True)

    if has_f and file_name:
        lines = []

        while True:
            line = input("Enter content line: ")

            if line == "stop":
                break

            lines.append(line)

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        numbered = []
        for i, line in enumerate(lines, start=1):
            numbered.append(f"{i} {line}")
        content = "\n".join(numbered)

        block = timestamp + "\n" + content

        if dir_parts:
            file_path = os.path.join(path, file_name)
        else:
            file_path = file_name
        with open(file_path, "a", encoding="utf-8") as f:
            if os.path.exists(file_path) and os.path.getsize(file_path) > 0:
                f.write("\n\n")

            f.write(block)


if __name__ == "__main__":
    main()
