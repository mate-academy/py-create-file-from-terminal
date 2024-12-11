from datetime import datetime
from sys import argv
from os import makedirs, path


def create_file_with_content(file_path: str) -> None:
    """Creates a file and appends content from user input."""
    now = datetime.now()
    timestamp = now.strftime("%Y-%m-%d %H:%M:%S")

    content_lines = []
    print("Enter content line (type 'stop' to finish):")
    while True:
        line = input("Enter content line: ")
        if line.lower() == "stop":
            break
        content_lines.append(line)

    new_content = f"\n{timestamp}\n"
    for i, line in enumerate(content_lines, start=1):
        new_content += f"{i} {line}\n"

    if path.exists(file_path):
        with open(file_path, "a") as file:
            file.write(new_content)
    else:
        with open(file_path, "w") as file:
            file.write(new_content)

    print(f"File created/updated at: {file_path}")


def main() -> None:
    args = argv[1:]

    if not args:
        print("No arguments provided. Use -d for directory or -f for file.")
        return

    dir_path = ""
    file_name = ""

    if "-d" in args:
        dir_index = args.index("-d")
        if "-f" in args:
            file_index = args.index("-f")
            dir_path = path.join(*args[dir_index + 1:file_index])
        else:
            dir_path = path.join(*args[dir_index + 1:])

        if dir_path:
            makedirs(dir_path, exist_ok=True)
            print(f"Directory created: {dir_path}")

    if "-f" in args:
        file_index = args.index("-f")
        if len(args) > file_index + 1:
            file_name = args[file_index + 1]

        if dir_path:
            file_path = path.join(dir_path, file_name)
        else:
            file_path = file_name

        create_file_with_content(file_path)


if __name__ == "__main__":
    main()
