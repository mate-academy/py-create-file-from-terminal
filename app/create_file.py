import os
from sys import argv
from datetime import datetime

def create_file() -> None:
    parts = argv[1:]
    dirs = []
    file_name = ""

    if "-d" in parts:
        for word in parts:
            if word.startswith("-"):
                break
            dirs.append(word)

    if "-f" in parts:
        file_name = parts[parts.index("-f") + 1]

    if dirs:
        path = os.path.join(*dirs)
        os.makedirs(path, exist_ok=True)
        if file_name:
            file_name = os.path.join(path, file_name)
        else:
            return

    inputed = []
    while True:
        line = input("Enter content line: ")
        if line.lower() == "stop":
            break
        inputed.append(line)

    with open(file_name, "a") as created:
        created.write(f"\n{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\n")
        for idx, text in enumerate(inputed, start=1):
            created.write(f"{idx} {text}\n")


if __name__ == "__main__":
    create_file()
