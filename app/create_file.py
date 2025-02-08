import sys
import os
import datetime


def main() -> None:
    args = sys.argv[1:]

    dir_index = args.index("-d") if "-d" in args else None
    file_index = args.index("-f") if "-f" in args else None

    if dir_index is not None:
        dir_path = os.path.join(*args[dir_index+1:file_index if file_index else None])
        os.makedirs(dir_path, exist_ok=True)
        print(f"Directory '{dir_path}' created")
    else:
        dir_path = os.getcwd()

    if file_index is not None:
        file_name = args[file_index + 1]
        file_path = os.path.join(dir_path, file_name)
        with open(file_path, 'a') as file:
            print(f"File '{file_path}' opened for writing")
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            file.write(f"\n{timestamp}")
            line_number = 1
            while True:
                content = input(f"Print string {line_number} (or stop): ")
                if content.lower() == "stop":
                    break
                file.write(f"{line_number} {content}\n")
                line_number += 1
        print(f"File {file_path} written")

