from datetime import datetime
import sys
import os


def create_directory(path: str) -> None:
    try:
        os.makedirs(path)
    except FileExistsError:
        print(f"Directory already exists: {path}")


def create_file(file_name: str) -> None:
    try:
        if os.path.exists(file_name):
            mode = "a"
        else:
            mode = "w"
        with open(file_name, mode) as file:
            if mode == "w":
                file.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S\n"))
        line_count = 1
        with open(file_name, mode) as file:
            file.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S\n"))
            while True:
                print("Enter content line: ")
                line = input()
                if line.strip().lower() == "stop":
                    break
                file.write(f"{line_count} {line}\n")
                line_count += 1
    except Exception as e:
        print(f"Error creating file: {e}")


def main() -> None:
    if len(sys.argv) < 2:
        return
    if "-d" in sys.argv and "-f" not in sys.argv:
        directory_path = str(os.path.join(*sys.argv[2:]))
        create_directory(directory_path)
    elif "-d" not in sys.argv and "-f" in sys.argv:
        create_file(sys.argv[-1])
    elif "-d" in sys.argv and "-f" in sys.argv:
        directory_path = str(os.path.join(*sys.argv[2:-2]))
        create_directory(directory_path)
        create_file(f"{directory_path}\\{sys.argv[-1]}")


if __name__ == "__main__":
    main()
