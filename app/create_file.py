import sys
from datetime import datetime
from pathlib import Path


def parse_arguments(arguments: list[str]) -> tuple[list[str], str | None]:
    """Split terminal arguments into directories and file name."""
    directories: list[str] = []
    file_name: str | None = None
    current_flag: str | None = None

    for argument in arguments:
        if argument in ("-d", "-f"):
            current_flag = argument
        elif current_flag == "-d":
            directories.append(argument)
        elif current_flag == "-f":
            file_name = argument

    return directories, file_name


def read_content() -> list[str]:
    """Read lines from the terminal until 'stop' is entered."""
    content: list[str] = []

    while True:
        line = input("Enter content line: ")

        if line == "stop":
            break

        content.append(line)

    return content


def write_to_file(file_path: Path, content: list[str]) -> None:
    """Append timestamp and numbered lines to the file."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(file_path, "a") as file:
        file.write(f"{timestamp}\n")

        for number, line in enumerate(content, start=1):
            file.write(f"{number} {line}\n")


def main() -> None:
    directories, file_name = parse_arguments(sys.argv[1:])
    directory_path = Path(*directories)

    if directories:
        directory_path.mkdir(parents=True, exist_ok=True)

    if file_name is None:
        return

    write_to_file(directory_path / file_name, read_content())


if __name__ == "__main__":
    main()
