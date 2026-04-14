import sys
import os
from datetime import datetime


def main() -> None:

    args = sys.argv[1:]

    dir_parts = []
    file_name = None

    current_flag = None
    for arg in args:
        if arg == "-d":
            current_flag = "-d"
        elif arg == "-f":
            current_flag = "-f"
        else:
            if current_flag == "-d":
                dir_parts.append(arg)
            elif current_flag == "-f":
                file_name = arg
                current_flag = None

    dir_path = ""
    if dir_parts:

        dir_path = os.path.join(*dir_parts)
        os.makedirs(dir_path, exist_ok=True)

    if file_name:

        if dir_path:
            file_path = os.path.join(dir_path, file_name)
        else:
            file_path = file_name

        lines = []
        while True:
            line = input("Enter content line: ")
            if line.strip() == "stop":
                break
            lines.append(line)

        prefix = ""
        if os.path.exists(file_path) and os.path.getsize(file_path) > 0:

            with open(file_path, "rb") as f:

                f.seek(-1, os.SEEK_END)
                last_char = f.read(1)

                if last_char == b"\n":
                    prefix = "\n"
                else:
                    prefix = "\n\n"

        with open(file_path, "a") as target_file:

            if prefix:
                target_file.write(prefix)

            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            target_file.write(f"{timestamp}\n")

            for index, text in enumerate(lines, 1):
                target_file.write(f"{index} {text}\n")


if __name__ == "__main__":
    main()
