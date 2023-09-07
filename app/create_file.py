import os
import sys
import datetime


def create_file(file_path: str) -> None:
    if os.path.exists(file_path):
        content = read_content(file_path)
    else:
        content = []
    while True:
        line = input("Enter content line: ")
        if line.lower() == "stop":
            break
        content.append(line)
    with open(file_path, "w") as file:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"{timestamp}\n")
        for i, line in enumerate(content, start=1):
            file.write(f"{i} {line}\n")


def read_content(file_path: str) -> list[str]:
    with open(file_path, "r") as file:
        return file.readlines()


def main() -> None:
    args = sys.argv[1:]

    if "-d" in args:
        dir_index = args.index("-d") + 1
        dir_path = os.path.join(*args[dir_index:])
        os.makedirs(dir_path, exist_ok=True)

    if "-f" in args:
        file_index = args.index("-f") + 1
        file_name = args[file_index]
        create_file(file_name)

    if "-d" not in args and "-f" not in args:
        print("Invalid arguments. Use either -d or -f flags.")


if __name__ == "__main__":
    main()
