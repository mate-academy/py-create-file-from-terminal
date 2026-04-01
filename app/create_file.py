import os
import sys
from datetime import datetime


def create_file() -> None:
    data = sys.argv[1:]

    def spliting_args(command: list[str]) -> list[str]:
        args = {"-d": [], "-f": []}
        current = None
        for arg in command:
            if arg in args:
                current = arg
            else:
                args[current].append(arg)
        dirs_data = args["-d"]
        file_name = args["-f"]
        return dirs_data, file_name

    def making_paths(directory: list[str]) -> str:
        base_path = os.getcwd()
        if directory:
            dir_paths = os.path.join(base_path, *directory)
            os.makedirs(dir_paths, exist_ok=True)
        else:
            dir_paths = base_path
        return dir_paths

    def making_file(filename: list[str], path: str) -> None:
        if filename:
            file_path = os.path.join(path, filename[0])
            lines = []
            counter = 1
            while True:
                line = input("Enter content line: ")
                if line.lower() == "stop":
                    break
                lines.append(f"{counter} {line}")
                counter += 1
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            content = timestamp + "\n" + "\n".join(lines) + "\n"
            if os.path.exists(file_path):
                with open(file_path, "a") as f:
                    f.write("\n" + content)
            else:
                with open(file_path, "w") as f:
                    f.write(content)
            print(f"File created/updated: {file_path}")

    dirs, files = spliting_args(data)
    paths = making_paths(dirs)
    making_file(files, paths)
