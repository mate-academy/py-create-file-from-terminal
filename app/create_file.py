import sys
import os
import datetime


def parse_args() -> tuple[list[str], str | None]:
    dirs = []
    file_name = None

    if "-d" in sys.argv:
        idx = sys.argv.index("-d")
        for arg in sys.argv[idx + 1:]:
            if arg.startswith("-"):
                break
            dirs.append(arg)

    if "-f" in sys.argv:
        idx = sys.argv.index("-f")
        if idx + 1 < len(sys.argv) and not sys.argv[idx + 1].startswith("-"):
            file_name = (sys.argv[idx + 1])

    return dirs, file_name


path = ""


def make_dir(dirs: list[str]) -> str:
    if dirs:
        path = os.path.join(*dirs)
        os.makedirs(path, exist_ok=True)
        return path
    return ""


def build_file_path(path: str, file_name: str | None) -> None:
    if file_name is None:
        return None
    if path:
        return os.path.join(path, file_name)
    return file_name


def write_file(file_path: str) -> None:
    lines = []
    while True:
        user = input("Enter content line: ")
        if user == "stop":
            break
        lines.append(user)

    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    new_line = []
    for index, line in enumerate(lines, start=1):
        new_line.append(f"{index} {line}")

    block = timestamp + "\n" + "\n".join(new_line) + "\n"

    with open(file_path, "a") as f:
        f.write(block)
        f.write("\n")


def main() -> None:
    dirs, file_name = parse_args()
    path = make_dir(dirs)
    file_path = build_file_path(path, file_name)

    if file_path:
        write_file(file_path)


if __name__ == "__main__":
    main()
