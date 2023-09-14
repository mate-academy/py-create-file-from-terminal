from datetime import datetime
import os
import sys


def main() -> None:
    if "-d" in sys.argv and "-f" in sys.argv:
        path = os.path.join(
            *sys.argv[sys.argv.index("-d") + 1:sys.argv.index("-f")]
        )
        create_folder(path)
        create_file(path)
        return
    if "-d" in sys.argv:
        path = os.path.join(*sys.argv[sys.argv.index("-d") + 1:])
        create_folder(path)
    if "-f" in sys.argv:
        create_file()


def create_folder(path: str) -> None:
    os.makedirs(path, exist_ok=True)


def create_file(path: str = os.getcwd()) -> None:
    content = [datetime.now().strftime("%Y-%m-%d %H:%M:%S")]
    counter = 0
    while True:
        message = input("Enter content line: ")
        if message.lower() == "stop":
            content.append("\n")
            break
        counter += 1
        content.append(f"{counter} {message}")
    file_name = sys.argv[sys.argv.index("-f") + 1]
    with open(os.path.join(path, file_name), "a") as new_file:
        new_file.write("\n".join(content))


if __name__ == "__main__":
    main()
