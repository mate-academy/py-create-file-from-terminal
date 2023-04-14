import argparse
from datetime import datetime
import os


def create_file() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-d", dest="dirs", nargs="*", help="create directories"
    )
    parser.add_argument("-f", dest="file", help="create file")
    args = parser.parse_args()

    path = ""

    if args.dirs:
        path = os.path.join(path, *args.dirs)
        os.makedirs(path, exist_ok=True)
        print(f"Directory created: {path}")

    if args.file:
        path = os.path.join(path, args.file)
        with open(path, "a") as file_out:
            lines = []
            line_number = 0
            while True:
                line = input("Enter content line: ")
                if not line or line == "stop":
                    break
                line_number += 1
                lines.append(f"\n{line_number} {line}")
            lines.append("\n" * 2)

            current_time = datetime.now()
            file_out.write(current_time.strftime("%Y-%m-%d %H:%M:%S"))
            file_out.writelines(lines)
            print(f"File created: {path}")


if __name__ == "__main__":
    create_file()
