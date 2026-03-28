import sys
import os
from datetime import datetime


def create_directories(path_parts: list[str]) -> str:
    """Create nested directories and return their path."""
    path = os.path.join(*path_parts)
    os.makedirs(path, exist_ok=True)
    return path


def write_to_file(file_path: str) -> None:
    """Ask user for content and write it with timestamp and line numbers."""
    lines = []
    while True:
        line = input("Enter content line: ")
        if line.strip().lower() == "stop":
            break
        lines.append(line)

    if not lines:
        return

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    file_exists = os.path.exists(file_path)
    has_content = file_exists and os.path.getsize(file_path) > 0

    with open(file_path, "a", encoding="utf-8") as output_file:
        if has_content:
            output_file.write("\n")  # порожній рядок перед новим блоком
        output_file.write(f"{timestamp}\n")
        for line_number, line in enumerate(lines, start=1):
            output_file.write(f"{line_number} {line}\n")

    print(f"\n✅ File '{file_path}' updated successfully.")


def main() -> None:
    """Parse terminal arguments and create directories or files."""
    args = sys.argv[1:]

    if not args:
        print("Usage examples:")
        print("  python create_file.py -d dir1 dir2")
        print("  python create_file.py -f file.txt")
        print(
            "  python create_file.py -d dir1 dir2 -f file.txt"
        )
        sys.exit(1)

    dir_parts: list[str] = []
    file_name: str | None = None

    if "-d" in args:
        d_index = args.index("-d") + 1
        for i in range(d_index, len(args)):
            if args[i] == "-f":
                break
            dir_parts.append(args[i])

    if "-f" in args:
        f_index = args.index("-f") + 1
        if f_index < len(args):
            file_name = args[f_index]

    # Handle directory creation
    if dir_parts:
        dir_path = create_directories(dir_parts)
    else:
        dir_path = os.getcwd()

    # Handle file creation
    if file_name:
        file_path = os.path.join(dir_path, file_name)
        write_to_file(file_path)
    else:
        print(
            f"✅ Directory '{dir_path}' created successfully "
            "(no file specified)."
        )


if __name__ == "__main__":
    main()
