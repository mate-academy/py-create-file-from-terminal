import datetime
import sys
import os


def create_directory() -> str:
    start_path = sys.argv.index("-d") + 1
    try:
        end_path = sys.argv.index("-f")
    except ValueError:
        end_path = len(sys.argv)
    directory = os.path.join(*sys.argv[start_path: end_path])
    os.makedirs(directory, exist_ok=True)
    return f"{directory}\\"


def create_file(path_to_file: str) -> None:
    file_name = sys.argv[-1]
    key = "a" if os.path.exists(path_to_file + file_name) else "w"
    with open(path_to_file + file_name, key) as file:
        file.write(
            f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
        )
        while True:
            text = input("Enter content line: ")
            if text == "stop":
                break
            file.write(f"{text}\n")


path = ""
if "-d" in sys.argv:
    path = create_directory()
if "-f" in sys.argv:
    create_file(path)
