import sys
import os
from datetime import datetime


def main() -> None:
    args = sys.argv[1:]
    dirs = []
    file_name = None
    if "-d" in args:
        d_index = args.index("-d") + 1
        while d_index < len(args) and args[d_index] != "-f":
            dirs.append(args[d_index])
            d_index += 1
    if "-f" in args:
        f_index = args.index("-f") + 1
        if f_index < len(args):
            file_name = args[f_index]
    if dirs:
        dir_path = os.path.join(*dirs)
        os.makedirs(dir_path, exist_ok=True)
    else:
        dir_path = "."
    if file_name:
        file_path = os.path.join(dir_path, file_name)
        print("Enter content line (type stop to finish):")
        lines = []
        while True:
            line = input("Enter content line: ")
            if line.lower() == "stop":
                break
            lines.append(line)
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        numbered_lines = [f"{i + 1} {text}" for i, text in enumerate(lines)]
        content = [timestamp] + numbered_lines
        with open(file_path, "a", encoding="utf-8") as f:
            f.write("\n".join(content) + "\n")
            print(f"File created or updated: {file_path}")
    else:
        print("No file name provided with -f flag.")


if __name__ == "__main__":
    main()
