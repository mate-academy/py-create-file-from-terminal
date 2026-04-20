from datetime import datetime
import os
import sys


def parse_args(args: list[str]) -> tuple[str, str]:
    directory_parts = []
    file_name = ""
    arg_index = 0

    while arg_index < len(args):
        if args[arg_index] == "-d":
            arg_index += 1
            while (
                arg_index < len(args)
                and not args[arg_index].startswith("-")
            ):
                directory_parts.append(args[arg_index])
                arg_index += 1

        elif args[arg_index] == "-f":
            arg_index += 1
            if (
                arg_index >= len(args)
                or args[arg_index].startswith("-")
            ):
                print("Error: Missing file name after '-f' flag.")
                sys.exit(1)
            file_name = args[arg_index]
            arg_index += 1

        else:
            print(
                f"Error: Unknown argument '{args[arg_index]}'. "
                "Use --help to see available options."
            )
            sys.exit(1)

    directory_path = ""
    if directory_parts:
        directory_path = os.path.join(os.getcwd(), *directory_parts)
        os.makedirs(directory_path, exist_ok=True)

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
    print("  python app/create_file.py -f file.txt -d dir1 dir2")


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
