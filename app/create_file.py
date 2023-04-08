from datetime import datetime
import os
import sys


def write_on_file(path: str) -> None:
    with open(path, "a") as file:
        line_count = 1
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"\n{timestamp}\n")
        while True:
            line = input("Enter content line: ")
            if line == "stop":
                break
            file.write(f"{line_count} {line}\n")
            line_count += 1


def create_dir(path: str) -> None:
    os.makedirs(path, exist_ok=True)


def main() -> None:
    args = sys.argv[1:]
    file_path = []
    if "-d" in args and "-f" in args:

        if args[0] == "-d":
            file_path = [arg for arg in args[1:-2]]
            file_path.append(args[-1])

        elif args[0] == "-f":
            file_path = [arg for arg in args[3:]]
            file_path.append(args[1])

        create_dir(os.path.join(*file_path[:-1]))
        write_on_file(os.path.join(*file_path))

    elif "-d" in args:
        file_path = [arg for arg in args[1:]]
        create_dir(os.path.join(*file_path))

    elif "-f" in args:
        write_on_file(args[-1])


if __name__ == "__main__":
    main()
