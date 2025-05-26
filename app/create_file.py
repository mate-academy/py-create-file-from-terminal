import sys
import os
from datetime import datetime

def create_directory(path_parts: list[str]) -> None:
    directory = os.path.join(*path_parts)
    os.makedirs(directory, exist_ok=True)
    print(f"✅ Directory '{directory}' created!")

def create_file(file_path: str) -> None:
    mode = "a" if os.path.exists(file_path) else "w"

    with open(file_path, mode) as file:
        print("✅ File opened:", file_path)
        file.write(f"\n{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")

        line_number = 1
        while True:
            line = input(f"Enter content line {line_number}: ")
            if line.lower() == "stop":
                break
            file.write(f"{line_number} {line}\n")
            line_number += 1

    print(f"✅ File '{file_path}' created successfully!")

def main() -> None:
    if "-d" in sys.argv:
        d_index = sys.argv.index("-d")
        path_parts = []
        for i in range(d_index + 1, len(sys.argv)):
            if sys.argv[i] == "-f":
                break
            path_parts.append(sys.argv[i])
        create_directory(path_parts)

    if "-f" in sys.argv:
        f_index = sys.argv.index("-f")
        file_name = sys.argv[f_index + 1]
        directory = os.path.join(*sys.argv[1:f_index]) if "-d" in sys.argv else ""
        file_path = os.path.join(directory, file_name) if directory else file_name
        create_file(file_path)

if __name__ == "__main__":
    main()
