import sys
import os
from datetime import datetime


def get_arguments() -> tuple[str, str]:
    directories = []
    filename = None

    args = sys.argv[1:]

    i = 0
    while i < len(args):
        if args[i] == "-d":
            i += 1
            while i < len(args) and args[i] != "-f":
                directories.append(args[i])
                i += 1

        elif args[i] == "-f":
            i += 1
            if i < len(args):
                filename = args[i]
                i += 1
            else:
                raise ValueError("Filename is missing after -f")

        else:
            raise ValueError(f"Unknown argument: {args[i]}")

    return directories, filename


def get_content() -> list[str]:
    lines = []

    while True:
        line = input("Enter content line: ")

        if line == "stop":
            break

        lines.append(line)

    return lines


def create_file(directories, filename) -> None:
    if not filename:
        if directories:
            os.makedirs(os.path.join(*directories), exist_ok=True)
            print("Directories created successfully.")
            return

        raise ValueError("You must provide -d or -f.")

    directory_path = os.path.join(*directories) if directories else "."

    os.makedirs(directory_path, exist_ok=True)

    file_path = os.path.join(directory_path, filename)

    lines = get_content()

    if not lines:
        print("No content provided.")
        return

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # with open(file_path, "a", encoding="utf-8") as file:
    #     file.write(timestamp + "\n")
    #
    #     for number, line in enumerate(lines, start=1):
    #         file.write(f"{number} {line}\n")

    with open(file_path, "a", encoding="utf-8") as file:
        if os.path.getsize(file_path) > 0:
            file.write("\n")

        file.write(timestamp + "\n")

        for number, line in enumerate(lines, start=1):
            file.write(f"{number} {line}\n")

    print(f"File created/updated successfully: {file_path}")


def main() -> None:
    try:
        directories, filename = get_arguments()
        create_file(directories, filename)

    except ValueError as error:
        print(f"Error: {error}")
        sys.exit(1)


if __name__ in ("__main__", "<run_path>"):
    main()
