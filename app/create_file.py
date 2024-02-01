import os
import sys
import datetime


def create_directory(directory_name: str) -> None:
    os.makedirs(directory_name, exist_ok=True)


def create_file(file_name: str) -> None:
    mode = "a" if os.path.exists(file_name) else "w"

    with open(file_name, mode) as file:
        create_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"{create_time}\n")

        lines = 1
        while True:
            new_line = input("Enter content line: ")
            if new_line == "stop":
                break
            file.write(f"Line{lines}: {new_line}\n")
            lines += 1


def main() -> None:
    if "-d" in sys.argv:
        base_directory = sys.argv[sys.argv.index("-d") + 1]
        dir2_path = os.path.join(base_directory, "dir2")
        create_directory(dir2_path)

        if "-f" in sys.argv:
            file_name = os.path.join(dir2_path, sys.argv[-1])
            create_file(file_name)


if __name__ == "__main__":
    main()
