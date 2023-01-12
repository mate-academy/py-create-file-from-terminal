from datetime import datetime
from create_directory import create_directory


def create_file() -> None:
    with open(create_directory(), "a") as new_file:
        new_file.write(datetime.now().strftime("%Y-%d-%m %H:%M:%S%\n"))
        line_number = 1
        while True:
            line = input("Enter content line: ")
            if line.strip() == "stop":
                break
            new_file.write(f"{line_number} {line}\n")
            line_number += 1


if __name__ == "__main__":
    create_file()
