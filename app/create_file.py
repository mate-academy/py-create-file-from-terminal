import sys
import os
from datetime import datetime
# імпорт бібліотек


def create_file() -> None:
    args = sys.argv[1:]   # зріз з командної строки
    if "-d" in args:
        dir_index = args.index("-d") + 1
        directories = args[dir_index:]
        if "-f" in directories:
            directories = directories[:directories.index("-f")]
        dir_path = os.path.join(*directories)
        os.makedirs(dir_path, exist_ok=True)
    else:
        dir_path = ""

    if "-f" in args:
        file_index = args.index("-f") + 1
        if file_index >= len(args):
            print("Error: No file name provided after '-f'.")
            return
        file_name = args[file_index]
        file_path = os.path.join(dir_path, file_name)
    else:
        print("Error: Missing '-f' flag for file creation.")
        return

    content_line = []
    print("Enter content line (type 'stop' to finish):")
    while True:
        line = input("Enter content line")
        if line == "stop":
            break
        content_line.append(line)

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    formatted_ts = f"\n{timestamp}\n"
    formatted_ts += "\n".join(f"{i + 1} {line}"
                              for i, line in enumerate(content_line))

    if os.path.exists(file_path):
        with open(file_path, "a") as f:
            f.write(formatted_ts)
    else:
        with open(file_path, "w") as f:
            f.write(formatted_ts)

    print(f"File created/updated at: {file_path}")
