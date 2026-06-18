import argparse
import datetime
import os


def parse_arguments() -> tuple[list[str], str | None]:
    parser = argparse.ArgumentParser()

    parser.add_argument("-d", nargs="*", default=[])
    parser.add_argument("-f")

    args = parser.parse_args()

    return args.d, args.f


def read_lines_from_input() -> list[str]:
    lines: list[str] = []
    index = 1

    while True:
        line = input("Enter content line: ").strip()

        if line == "stop":
            break

        lines.append(f"{index} {line}")
        index += 1

    return lines


def create_file_and_content(file_path: str) -> None:
    dir_path = os.path.dirname(file_path)

    if dir_path:
        os.makedirs(dir_path, exist_ok=True)

    file_exists = os.path.exists(file_path)
    lines = read_lines_from_input()

    with open(file_path, "a") as file:
        if file_exists and os.path.getsize(file_path) > 0:
            file.write("\n")

        date_now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(
            f"{date_now}\n"
        )

        if lines:
            file.write("\n".join(lines))
            file.write("\n")


def main() -> None:
    directories, filename = parse_arguments()

    if filename:
        path = (
            os.path.join(*directories, filename)
            if directories
            else filename
        )

        create_file_and_content(path)

    elif directories:
        os.makedirs(os.path.join(*directories), exist_ok=True)


main()
