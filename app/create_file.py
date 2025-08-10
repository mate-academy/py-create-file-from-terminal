import sys
import os
from datetime import datetime


def main() -> None:
    args = sys.argv[1:]
    if "-d" in args:
        # получение пути
        dir_index = args.index("d") + 1
        path_parts = []
        while dir_index < len(args) and args[dir_index] != "-f":
            path_parts.append(args[dir_index])
            dir_index += 1
        directory = os.path.join(*path_parts)
        os.makedirs(directory, exist_ok=True)

    if "-f" in args:
        # получение имени файла
        file_index = args.index("-f") + 1
        filename = args[file_index]
        if "-d" in args:
            file_path = os.path.join(directory, filename)
        else:
            file_path = filename

        print("Enter file content. Type 'stop' to finish.")
        lines = []
        while True:
            line = input("Enter content line: ")
            if line.lower() == "stop":
                break
            lines.append(line)

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(file_path, "a") as f:
            f.write(f"\n{timestamp}\n")
            for i, line in enumerate(lines, 1):
                f.write(f"{i} {line}\n")
        print(f"File {file_path} has been successfully created/updated!")

if __name__ == "__main__":
    main()
