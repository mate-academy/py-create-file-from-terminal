import os
import sys
from datetime import datetime


def create_file() -> None:
    args = sys.argv

    d_index = args.index("-d") if "-d" in args else None
    f_index = args.index("-f") if "-f" in args else None

    directories = []
    if d_index is not None:
        if f_index is not None and f_index > d_index:
            end_d = f_index
        else:
            end_d = len(args)

        directories = args[d_index + 1 : end_d]

    file_name = None
    if f_index is not None:
        if f_index + 1 < len(args):
            file_name = args[f_index + 1]
        else:
            print("Erro: Falta o nome do ficheiro após a flag -f")
            return

    path = os.path.join(*directories) if directories else "."

    if directories:
        os.makedirs(path, exist_ok=True)

    if file_name:
        full_path = os.path.join(path, file_name)

        needs_newline = (
            os.path.exists(full_path) and os.path.getsize(full_path) > 0
        )

        with open(full_path, "a") as file:
            if needs_newline:
                file.write("\n")

            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            file.write(f"{timestamp}\n")

            line_count = 1
            while True:
                content = input("Enter content line: ")

                if content == "stop":
                    break

                file.write(f"{line_count} {content}\n")
                line_count += 1


if __name__ == "__main__":
    create_file()
