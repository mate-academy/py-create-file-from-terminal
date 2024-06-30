import sys
from datetime import datetime
from pathlib import Path


def create_directory(path_parts: list[str]) -> Path:
    path = Path(*path_parts)
    path.mkdir(parents=True, exist_ok=True)
    return path


def create_file(file_path: Path) -> None:
    with open(file_path, "a") as f:
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"{current_time}\n")
        line_number = 1
        while True:
            content = input("Enter content line: ")
            if content.lower() == "stop":
                break
            f.write(f"{line_number} {content}\n")
            line_number += 1
        f.write("\n")


def main() -> None:
    args = sys.argv[1:]
    if "-d" in args:
        d_index = args.index("-d")
        if "-f" in args:
            f_index = args.index("-f")
            directory_path = create_directory(args[d_index + 1:f_index])
            file_path = directory_path / args[f_index + 1]
            create_file(file_path)
        else:
            create_directory(args[d_index + 1:])
    elif "-f" in args:
        f_index = args.index("-f")
        file_path = Path(args[f_index + 1])
        create_file(file_path)
    else:
        print("Invalid arguments. Use -d for directory and -f for file.")


if __name__ == "__main__":
    main()
