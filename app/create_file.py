import sys
import os
from datetime import datetime


def get_timestamp() -> str:
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def read_content() -> list:
    lines = []
    counter = 1
    while True:
        line = input("Enter content line: ")
        if line.strip().lower() == "stop":
            break
        lines.append(f"{counter} {line}")
        counter += 1
    return lines


def main() -> None:
    args = sys.argv[1:]
    if not args:
        print("❌ No arguments provided.")
        return

    path = os.getcwd()
    filename = None
    i = 0

    while i < len(args):
        if args[i] == "-d":
            i += 1
            dirs = []
            while i < len(args) and not args[i].startswith("-"):
                dirs.append(args[i])
                i += 1
            if dirs:
                path = os.path.join(path, *dirs)
                os.makedirs(path, exist_ok=True)
        elif args[i] == "-f":
            i += 1
            if i < len(args):
                filename = args[i]
                i += 1
            else:
                print("❌ File name is missing after -f flag.")
                return
        else:
            print(f"❌ Unknown argument: {args[i]}")
            return

    if filename:
        filepath = os.path.join(path, filename)
        content = read_content()
        with open(filepath, "a", encoding="utf-8") as file:
            file.write(get_timestamp() + "\n")
            for line in content:
                file.write(line + "\n")
            file.write("\n")
        print(f"✅ File written to: {filepath}")
    elif path != os.getcwd():
        print(f"✅ Directory created: {path}")
    else:
        print("❌ No operation performed.")
