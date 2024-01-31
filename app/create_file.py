import os
import sys
from datetime import datetime


def get_file_content() -> list:
    content = []
    while True:
        print("Enter 'stop' if you want to quite")
        message = input("Enter content line: ")
        if message == "stop":
            break
        content.append(message)

    return content


def create_file(file_name: str, content: list) -> None:
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(file_name, "a") as file:
        file.write(f"{current_time}\n")
        for line_number, line in enumerate(content, start=1):
            file.write(f"{line_number} {line}\n")
        file.write("\n")

    print("File was successfully created or appended")


def create_directory(path: str) -> None:
    os.makedirs(path)
    print("Directory was successfully created")


def main():
    if "-d" in sys.argv and "-f" in sys.argv:
        path = os.path.join(*sys.argv[2:sys.argv.index("-f")])
        create_directory(path)
        os.chdir(path)
        create_file(sys.argv[-1], get_file_content())
    elif "-f" in sys.argv:
        create_file(sys.argv[-1], get_file_content())
    elif "-d" in sys.argv:
        create_directory(os.path.join(*sys.argv[2:]))


if __name__ == "__main__":
    main()
