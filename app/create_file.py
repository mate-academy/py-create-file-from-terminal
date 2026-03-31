import sys
import os
import datetime


def get_args():
    args = sys.argv[1:]

    dirs = []
    file_name = None

    i = 0
    while i < len(args):
        if args[i] == "-d":
            i += 1
            while i < len(args) and args[i] not in ["-d", "-f"]:
                dirs.append(args[i])
                i += 1
        elif args[i] == "-f":
            i +=1
            if i < len(args):
                file_name = args[i]
                i += 1
        else:
            i += 1

    return dirs, file_name


def create_dirs(dirs):
    if dirs:
        path = os.path.join(*dirs)
        os.makedirs(path, exist_ok=True)
        return path
    return ""


def get_content():
    lines = []
    while True:
        line = input("Enter content line: ")
        if line == "stop":
            break
        lines.append(line)
    return lines


def format_content(lines):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    result = [timestamp]
    for i, line in enumerate(lines, start=1):
        result.append(f"{i} {line}")

    return "\n".join(result) + "\n"


def write_file(path, file_name, content):
    full_path = os.path.join(path, file_name) if path else file_name

    file_exists = os.path.exists(full_path)

    with open(full_path, "a", encoding="utf-8") as f:
        if file_exists:
            f.write("\n")  # відступ між блоками
        f.write(content)


def main():
    dirs, file_name = get_args()

    path = create_dirs(dirs)

    if file_name:
        lines = get_content()
        content = format_content(lines)
        write_file(path, file_name, content)
    else:
        print("No file specified (-f)")

if __name__ == "__main__":
    main()
