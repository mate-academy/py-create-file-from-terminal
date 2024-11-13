import sys
from datetime import datetime
from pathlib import Path


def get_content():
    content_lines = []
    line_number = 1
    while True:
        line = input("Enter content line: ")
        if line.lower() == "stop":
            break
        content_lines.append(f"{line_number} {line}")
        line_number += 1
    return content_lines


def create_directories(directories):
    path = Path(*directories)
    path.mkdir(parents=True, exist_ok=True)  # Створює каталоги, якщо їх ще не існує
    print(f"Directory created: {path}")
    return path


def create_file(file_path, content_lines):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(file_path, 'a') as f:
        f.write(f"\n{timestamp}\n")
        for line in content_lines:
            f.write(f"{line}\n")
    print(f"File created/updated: {file_path}")


def main():
    if "-d" not in sys.argv and "-f" not in sys.argv:
        print("Usage:\n  python create_file.py -d <directory> ... -f <filename>")
        return

    directories = None
    filename = None

    if "-d" in sys.argv:
        d_index = sys.argv.index("-d")
        directories = []
        for i in range(d_index + 1, len(sys.argv)):
            if sys.argv[i].startswith("-"):
                break
            directories.append(sys.argv[i])

    if "-f" in sys.argv:
        f_index = sys.argv.index("-f")
        filename = sys.argv[f_index + 1]

    if directories:
        directories = [str(d) for d in directories]

        directory_path = create_directories(directories)

        if filename:
            file_path = directory_path / filename
            content_lines = get_content()
            create_file(file_path, content_lines)

    elif filename:
        content_lines = get_content()
        create_file(filename, content_lines)


if __name__ == "__main__":
    main()
