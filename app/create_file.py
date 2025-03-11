import sys
from pathlib import Path
from datetime import datetime


def create_directory(path_parts: list[str]) -> None:
    path = Path(*map(str, path_parts))
    path.mkdir(parents=True, exist_ok=True)
    print(f"Directory '{path}' created successfully.")


def create_file(file_path: str) -> None:
    file_obj = Path(file_path)
    mode = "a" if file_obj.exists() else "w"
    with file_obj.open(mode) as f:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"\n{timestamp}\n")
        line_number = 1
        while True:
            content = input(f"Enter content line {line_number}: ")
            if content.lower() == "stop":
                break
            f.write(f"{line_number} {content}\n")
            line_number += 1
    print(f"File '{file_obj}' created/updated successfully.")


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print(
            "Usage: python create_file.py -d dir1 dir2 "
            "OR python create_file.py -f file_name"
        )
        sys.exit(1)
    flag = sys.argv[1]
    if flag == "-d":
        create_directory(sys.argv[2:])
    elif flag == "-f":
        if len(sys.argv) < 3:
            print("Error: No file name provided after '-f' flag.")
            sys.exit(1)
        create_file(sys.argv[2])
    elif "-d" in sys.argv and "-f" in sys.argv:
        path_parts = sys.argv[2:sys.argv.index("-f")]
        create_directory(path_parts)

        file_index = sys.argv.index("-f") + 1
        if file_index >= len(sys.argv):
            print("Error: No file name provided after '-f' flag.")
            sys.exit(1)
        file_name = sys.argv[file_index]
        create_file(str(Path(*path_parts) / file_name))
    else:
        print("Invalid flag. Use -d to create directory or -f to create file.")
