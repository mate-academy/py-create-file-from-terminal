import datetime
import os
import sys


def find_path_and_filename() -> str | None:
    args = sys.argv[1:]

    idx_d = args.index("-d") if "-d" in args else None
    idx_f = args.index("-f") if "-f" in args else None

    filename = None
    if idx_f is not None and idx_f + 1 < len(args):
        filename = args[idx_f + 1]

    if idx_d is None:
        dir_path = []
    elif idx_f is None or idx_d > idx_f:
        dir_path = args[idx_d + 1:]
    else:
        dir_path = args[idx_d + 1: idx_f]

    if dir_path:
        os.makedirs(os.path.join(*dir_path), exist_ok=True)

    if filename:
        return os.path.join(*dir_path, filename) if dir_path else filename
    return None


def write_file(file_path: str) -> None:
    with open(file_path, "a") as file:
        file.write(
            datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n"
        )
        lines = []
        while True:
            line = input("Enter content line: ")
            if line.strip() == "stop":
                break
            lines.append(line.rstrip())
        for i, line in enumerate(lines, 1):
            file.write(f"{i} {line}\n")
        file.write("\n")


def main() -> None:
    file_path = find_path_and_filename()
    if file_path:
        write_file(file_path)


if __name__ == "__main__":
    main()
