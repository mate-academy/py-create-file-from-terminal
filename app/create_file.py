import sys
import os
from datetime import datetime


def main() -> None:
    args = sys.argv[1:]

    dir_parts = []
    file_name = None

    if not args:
        print(
            "Please provide flags and arguments. "
            "Use -d for directory, -f for file."
        )
        return

    if "-d" in args:
        d_index = args.index("-d")
        dir_parts = []
        for i in range(d_index + 1, len(args)):
            if args[i] == "-f":
                break
            dir_parts.append(args[i])

    if "-f" in args:
        f_index = args.index("-f")
        if f_index + 1 < len(args):
            file_name = args[f_index + 1]

    if dir_parts:
        dir_path = os.path.join(*dir_parts)
        os.makedirs(dir_path, exist_ok=True)
    else:
        dir_path = ""

    if file_name:
        file_path = os.path.join(
            dir_path, file_name
        ) if dir_path else file_name

        lines = []
        count = 1
        while True:
            content = input("Enter content line: ")
            if content.strip().lower() == "stop":
                break
            lines.append(f"{count} {content}")
            count += 1

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        mode = "a" if os.path.exists(file_path) else "w"
        with open(file_path, mode, encoding="utf-8") as f:
            if mode == "a":
                f.write("\n")
            f.write(f"{timestamp}\n")
            for line in lines:
                f.write(f"{line}\n")

        print(f"File created/updated at: {file_path}")
    elif dir_parts:
        print(f"Directory created at: {dir_path}")
    else:
        print("No file or directory specified.")


if __name__ == "__main__":
    main()
