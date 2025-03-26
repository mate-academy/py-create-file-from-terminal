from datetime import datetime
import os
import sys


def parse_args(args: list[str]) -> tuple[str, str]:
    directory_path = ""
    file_name = ""

    has_f = "-f" in args
    has_d = "-d" in args
    file_flag_pos = args.index("-f") if has_f else -1
    dir_flag_pos = args.index("-d") if has_d else -1

    if has_f:
        if file_flag_pos + 1 >= len(args):
            print("Error: Missing file name after '-f' flag.")
            sys.exit(1)
        file_name = args[file_flag_pos + 1]

    if has_d:
        if has_f and file_flag_pos < dir_flag_pos:
            print("Error: '-d' flag must come before '-f' flag.")
            sys.exit(1)

        stop_pos = file_flag_pos if has_f else len(args)
        directory_parts = args[dir_flag_pos + 1:stop_pos]

        if not directory_parts:
            print("Error: Missing directory path after '-d' flag.")
            sys.exit(1)

        directory_path = os.path.join(os.getcwd(), *directory_parts)
        os.makedirs(directory_path, exist_ok=True)

        if not has_f:
            print(f"Directory created: {directory_path}")

    file_path = (
        os.path.join(directory_path, file_name)
        if directory_path else file_name
    )

    return file_path, file_name


def collect_input() -> list[str]:
    lines = []
    while True:
        line = input("Enter content line: ")
        if line.lower() == "stop":
            break
        lines.append(line)
    return lines


def write_to_file(file_path: str, lines: list[str]) -> None:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(file_path, "a", encoding="utf-8") as file:
        file.write(f"{timestamp}\n")
        for index, line in enumerate(lines, start=1):
            file.write(f"{index} {line}\n")


def show_help() -> None:
    print("Usage:")
    print("  python app/create_file.py [OPTIONS]")
    print()
    print("Options:")
    print("  -d [DIR ...]      Create directory path")
    print("  -f FILE           Create file and enter content until 'stop'")
    print("  --help            Show this help message and exit")
    print()
    print("Examples:")
    print("  python app/create_file.py --help")
    print("  python app/create_file.py -d dir1 dir2")
    print("  python app/create_file.py -f file.txt")
    print("  python app/create_file.py -d dir1 dir2 -f file.txt")


def main() -> None:
    args = sys.argv[1:]

    if not args or "--help" in args:
        show_help()
        return

    file_path, file_name = parse_args(args)

    if file_name:
        lines = collect_input()
        write_to_file(file_path, lines)


if __name__ == "__main__":
    main()
