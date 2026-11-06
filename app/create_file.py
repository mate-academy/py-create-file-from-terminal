import sys
from datetime import datetime
from os import makedirs, path


def main() -> None:
    dirs, filename = parse_arguments()

    if "-d" in sys.argv:
        if len(dirs) == 0:
            raise ValueError("Missing dirname/s after -d")
        create_directories(dirs)

    if "-f" in sys.argv:
        if filename is None:
            raise ValueError("Missing filename after -f")
        file_path = path.join(*dirs, filename) if dirs else filename
        create_file_and_content(file_path)


def parse_arguments() -> tuple[list[str], str | None]:
    dirs: list[str] = []
    filename: str | None = None
    current_flag: str | None = None

    for arg in sys.argv[1:]:
        if arg in ("-d", "-f"):
            current_flag = arg
            continue

        if current_flag == "-d":
            dirs.append(arg)
        elif current_flag == "-f":
            filename = arg
            current_flag = None

    return dirs, filename


def create_directories(dirs: list[str]) -> None:
    if not dirs:
        return
    dirs_path = path.join(*dirs)
    makedirs(dirs_path, exist_ok=True)


def create_file_and_content(filename: str) -> None:
    file_exists: bool = path.exists(filename)
    is_empty: bool = not file_exists or path.getsize(filename) == 0

    with open(filename, "a") as file_out:
        if not is_empty:
            file_out.write("\n")

        current_date: datetime = datetime.now()
        file_out.write(current_date.strftime("%Y-%m-%d %H:%M:%S\n"))

        line_number: int = 1

        while True:
            content: str = input("Enter content line: ")
            if content == "stop":
                break
            file_out.write(f"{line_number} {content}\n")
            line_number += 1


main()
