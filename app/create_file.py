import os
import sys
from datetime import datetime


def create_file(directory: str, filename: str, content: list) -> None:
    if directory:
        os.makedirs(directory, exist_ok=True)
    filepath = os.path.join(directory, filename)

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(filepath, "a") as file:
        file.write(timestamp + "\n")
        for i, line in enumerate(content, start=1):
            file.write(f"{i} {line}\n")


def main() -> None:
    args = sys.argv[1:]
    if not args:
        print("Usage: python create_file.py -d [directory_path] -f [filename]")
        return

    directory = ""
    filename = ""
    content = []
    while args:
        flag = args.pop(0)
        if flag == "-d":
            directory = os.path.join(directory, args.pop(0))
        elif flag == "-f":
            filename = args.pop(0)
        else:
            print(f"Invalid flag: {flag}")
            return

    if filename:
        print("Enter content line:")
        while True:
            line = input()
            if line.lower() == "stop":
                break
            content.append(line)

    create_file(directory, filename, content)
    print(f"File '{filename}' created successfully.")


if __name__ == "__main__":
    main()
