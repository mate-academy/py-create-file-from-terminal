import os
import sys
import datetime


def create_directory(directories: list[str]) -> str:
    paths = os.path.join(*directories)

    os.makedirs(paths, exist_ok=True)
    return paths


def create_file(filename: str, path: str = "") -> str:
    full_path = os.path.join(path, filename)

    with open(full_path, "a") as file:
        time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        file.write(str(time) + "\n")
        lines = 1
        while True:
            content = input("Enter content line: ")
            if content == "stop":
                break
            file.write(f"{lines} {content}\n")
            lines += 1
        file.write("\n")


def main(args: list[str]) -> None:
    if "-d" in args and "-f" not in args:
        create_directory(args[args.index("-d") + 1:])
    elif "-f" in args and "-d" not in args:
        create_file(args[args.index("-f") + 1])
    elif "-f" in args and "-d" in args:
        index_d = args.index("-d")
        index_f = args.index("-f")
        folder_path = create_directory(args[index_d + 1:index_f])
        create_file(args[index_f + 1], folder_path)


main(sys.argv)
