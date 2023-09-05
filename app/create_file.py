import os
import sys
import datetime


def create_file(file_path: (list[str], str)) -> None:
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


def read_content(file_path: str) -> str:
    with open(file_path, "r") as file:
        return file.readlines()


if __name__ == "__main__":
    args = sys.argv

    if "-d" in args and "-f" in args:
        start = args.index("-d") + 1
        end = args.index("-f")

        path_to_file = create_file(args[start:end])
        create_file(os.path.join(path_to_file, args[end + 1]))

    elif "-d" in args:
        start = args.index("-d") + 1
        end = len(args)
        create_file(args[start:end])

    elif "-f" in args:
        index = args.index("-f") + 1
        create_file(args[index])

    else:
        print("Invalid arguments. Use either -d or -f flags.")
