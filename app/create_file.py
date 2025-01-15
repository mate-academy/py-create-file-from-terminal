import sys
import os
from datetime import datetime


def main() -> None:
    directories = []
    file_name = None

    if "-d" in sys.argv:
        index_d = sys.argv.index("-d") + 1
        for arg in sys.argv[index_d:]:
            if arg == "-f":
                break
            directories.append(arg)

    if "-f" in sys.argv:
        index_f = sys.argv.index("-f") + 1
        file_name = sys.argv[index_f]

    if directories:
        path = os.path.join(*directories)
        os.makedirs(path, exist_ok=True)

        if file_name:
            file_path = os.path.join(path, file_name)
        else:
            sys.exit("Error: File name missing.")
    else:
        file_path = file_name

    if file_path:
        line_count = 1
        if os.path.exists(file_path):
            with open(file_path, "r") as existing_file:
                lines = existing_file.readlines()
                if lines:
                    line_count = len(lines) + 1

        with open(file_path, "a") as new_file:
            if line_count > 1:
                new_file.write("\n")

            time = datetime.now()
            new_file.write(time.strftime("%Y-%m-%d %H:%M:%S") + "\n")

            while True:
                info = input("Enter content line or 'stop': ")
                if info.lower() == "stop":
                    break
                new_file.write(f"{line_count} {info}\n")
                line_count += 1


if __name__ == "__main__":
    main()
