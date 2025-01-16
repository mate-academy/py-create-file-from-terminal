import sys
import os
from datetime import datetime


def main() -> None:
    args = sys.argv[1:]
    directory = []
    file_name = None

    if "-d" in args:
        d_index = args.index("-d")
        directory = args[d_index + 1:args.index("-f")] if "-f" in args else args[d_index + 1:]
    if "-f" in args:
        f_index = args.index("-f")
        file_name = args[f_index + 1]

    if directory:
        os.makedirs(os.path.join(*directory), exist_ok=True)

    if not file_name:
        print("Error: File name not specified.")
        return

    lines = []
    while True:
        line = input("Enter content line: ")
        if line.lower() == "stop":
            break
        lines.append(line)

    file_path = os.path.join(*directory, file_name) if directory else file_name

    with open(file_path, "a") as file:
        file.write(f"\n{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        for index, line in enumerate(lines, start=1):
            file.write(f"{index} {line}\n")

    print(f"File '{file_path}' created/updated successfully!")


if __name__ == "__main__":
    main()
