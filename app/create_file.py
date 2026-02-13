import os
import sys
from datetime import datetime


def create_file() -> None:
    args = sys.argv

    d_index = args.index("-d") if "-d" in args else None
    f_index = args.index("-f") if "-f" in args else None

    directories = []
    if d_index is not None:
        end_d = f_index if (f_index and f_index > d_index) else len(args)
        directories = args[d_index + 1 : end_d]

    file_name = None
    if f_index is not None:
        file_name = args[f_index + 1]

    path = os.path.join(*directories)
    if directories:
        os.makedirs(path, exist_ok=True)

    if file_name:
        full_path = os.path.join(path, file_name)

        with open(full_path, "a") as file:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            file.write(f"{timestamp}\n")

            line_count = 1
            while True:
                content = input("Enter content line: ")
                if content.lower() == "stop":
                    file.write("\n")
                    break

                file.write(f"{line_count} {content}\n")
                line_count += 1


if __name__ == "__main__":
    create_file()
