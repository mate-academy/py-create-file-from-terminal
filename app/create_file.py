import sys
import os
from datetime import datetime
from typing import Any


# Check for correct input
def check_input() -> Any:
    if len(sys.argv) < 3:
        print("Wrong usage! Usage is: create_file.py -d directory -f filename")
        sys.exit()
    if sys.argv.count("-d") > 1 or sys.argv.count("-f") > 1:
        print("Wrong usage! Usage is: create_file.py -d directory -f filename")
        sys.exit()

    allowed_flags = ["-d", "-f"]
    for arg in sys.argv[1:]:
        if arg.startswith("-") and arg not in allowed_flags:
            print(f"Unknown flag: {arg}")
            sys.exit()

    match sys.argv[1]:
        case "-d":
            filepath = []
            filename = None

            for i in range(2, len(sys.argv)):
                if sys.argv[i] == "-f":
                    try:
                        filename = sys.argv[i + 1]
                    except IndexError:
                        print("Missing filename")
                        sys.exit()
                    break
                else:
                    filepath.append(sys.argv[i])

            if not filepath:
                print("Incorrect filepath")
                sys.exit()

        case "-f":
            try:
                filename = sys.argv[2]
            except IndexError:
                print("Missing filename")
                sys.exit()

            filepath = None

            if "-d" in sys.argv:
                d_index = sys.argv.index("-d")
                filepath = sys.argv[d_index + 1:]
        case _:
            print("Wrong usage! Usage is: create_file.py"
                  " -d directory -f filename")
            sys.exit()

    return filepath, filename


# Creating file
def create_file(filepath: str | None, filename: str | None) -> None:
    if filepath:
        filepath = os.path.join(*filepath)
        os.makedirs(filepath, exist_ok=True)

    if filename:
        if filepath:
            filename = os.path.join(filepath, filename)

        with open(filename, "w") as input_file:
            now = datetime.now()
            input_file.write(now.strftime("%Y-%m-%d %H:%M:%S\n"))

            count = 1

            while True:
                line = input("Enter content line: ")
                if line != "stop":
                    line = f"{count} {line}\n"
                    input_file.write(line)
                    count += 1
                else:
                    break


if __name__ == "__main__":
    file_path, file_name = check_input()
    create_file(file_path, file_name)
