import os
from sys import argv
from datetime import datetime


def find_flags(parts: list[str]) -> None | str:
    file_name = None
    dirs = []
    if "-d" in parts:
        for word in parts[parts.index("-d") + 1:]:
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

    return file_name


def create_file() -> None:
    file_name = find_flags(argv[1:])
    if not file_name:
        return

    received = []
    while True:
        line = input("Enter content line: ")
        if line.lower() == "stop":
            break
        received.append(line)

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if os.path.exists(file_name):
        timestamp = "\n" + timestamp

    with open(file_name, "a") as created:
        created.write(f"{timestamp}\n")

        for idx, text in enumerate(received, start=1):
            created.write(f"{idx} {text}\n")


if __name__ == "__main__":
    create_file()
