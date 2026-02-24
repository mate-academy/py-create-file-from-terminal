import sys
import os
from datetime import datetime


def get_content() -> list[str]:
    lines = []
    counter = 1
    print("Enter content line (type 'stop' to finish):")
    while True:
        line = input("Enter content line: ")
        if line.strip().lower() == "stop":
            break
        lines.append(f"{counter} {line}")
        counter += 1
    return lines


def write_content(filepath: str, lines: list[str]) -> None:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    block = [timestamp] + lines + [""]

    try:
        with open(filepath, "a", encoding="utf-8") as f:
            f.write("\n".join(block))
            print(f'Content written to "{filepath}".')
    except Exception as e:
        print(f"Failed to write to file: {e}")


def main() -> None:
    args = sys.argv[1:]

    if not args:
        print("No arguments provided. Use -d for directory or -f for file.")
        return

    directory = ""
    filename = ""

    if "-d" in args:
        d_index = args.index("-d")
        if "-f" in args:
            f_index = args.index("-f")
            if d_index + 1 >= f_index:
                print("Error: No directory path specified between '-d' and '-f'.")
                return
            directory_parts = args[d_index + 1:f_index]
            directory = os.path.join(*directory_parts)
            if f_index + 1 >= len(args):
                print("Error: No filename specified after '-f'.")
                return
            filename = args[f_index + 1]
        else:
            if d_index + 1 >= len(args):
                print("Error: No directory path specified after '-d'.")
                return
            directory_parts = args[d_index + 1:]
            directory = os.path.join(*directory_parts)
    elif "-f" in args:
        f_index = args.index("-f")
        if f_index + 1 >= len(args):
            print("Error: No filename specified after '-f'.")
            return
        filename = args[f_index + 1]
    else:
        print("Error: You must provide at least -d or -f flag.")
        return

    if directory:
        try:
            os.makedirs(directory, exist_ok=True)
            print(f'Directory "{directory}" is ready.')
        except Exception as e:
            print(f"Failed to create directory: {e}")
            return

    if filename:
        filepath = os.path.join(directory, filename) if directory else filename
        lines = get_content()
        write_content(filepath, lines)
    else:
        print("Error: No file specified.")


if __name__ == "__main__":
    main()
