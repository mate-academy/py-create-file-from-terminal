import sys
import os
import datetime

def parse_arguments(args):
    dir_parts = []
    file_name = None
    mode = None

    for arg in args:
        if arg == "-d":
            mode = "dir"
        elif arg == "-f":
            mode = "file"
        else:
            if mode == "dir":
                dir_parts.append(arg)
            elif mode == "file":
                file_name = arg

    return dir_parts, file_name

def get_file_content():
    lines = []
    while True:
        line = input("Enter content line: ")
        if line.lower() == "stop":
            break
        lines.append(line)

    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    content = [timestamp]
    content += [f"{i} {line}" for i, line in enumerate(lines, 1)]

    return "\n".join(content)


def main():
    args = sys.argv[1:]
    dir_parts, file_name = parse_arguments(args)

    if not file_name:
        sys.exit(1)

    if dir_parts:
        target_directory = os.path.join(os.getcwd(), *dir_parts)
        os.makedirs(target_directory, exist_ok=True)
    else:
        target_directory = os.getcwd()

    file_path = os.path.join(target_directory, file_name)

    content = get_file_content()

    mode = "a" if os.path.exists(file_path) else "w"

    with open(file_path, mode, encoding="utf-8") as f:
        if mode == "a":
            f.write("\n\n")
        f.write(content)

    print(f"Content written to {file_path}")


if __name__ == "__main__":
    main()
