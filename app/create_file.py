import os
import sys
from datetime import datetime

def get_timestamp() -> str:
    return datetime.now().strftime('%Y-%m-%d %H:%M:%S')

def get_user_input() -> list:
    lines = []
    while True:
        line = input("Enter content line: ")
        if line.strip().lower() == "stop":
            break
        lines.append(line)
    return lines

def write_content_to_file(file_path: str, lines: list) -> None:
    with open(file_path, "a", encoding="utf-8") as f:
        f.write(f"{get_timestamp()}\n")
        for idx, line in enumerate(lines, 1):
            f.write(f"{idx} {line}\n")
        f.write("\n")  # Add an empty line after each session

def main():
    args = sys.argv[1:]

    if not args:
        print("No arguments provided. Use -d for directory or -f for file.")
        return

    dir_path = ""
    file_name = ""

    if "-d" in args:
        d_index = args.index("-d")
        # Check if there's -f as well
        if "-f" in args:
            f_index = args.index("-f")
            dir_parts = args[d_index + 1:f_index]
        else:
            dir_parts = args[d_index + 1:]
        dir_path = os.path.join(*dir_parts)
        os.makedirs(dir_path, exist_ok=True)

    if "-f" in args:
        f_index = args.index("-f")
        try:
            file_name = args[f_index + 1]
        except IndexError:
            print("File name not provided after -f.")
            return
        file_path = os.path.join(dir_path, file_name) if dir_path else file_name
        user_lines = get_user_input()
        write_content_to_file(file_path, user_lines)
        print(f"\nFile saved to: {file_path}")

    elif not "-f" in args:
        print("Directory created.")
        return

if __name__ == "__main__":
    main()
