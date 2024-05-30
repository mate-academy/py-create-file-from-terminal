import datetime
import sys
import os


def create_file(is_path: bool, is_file: bool) -> None:
    path_to_file = ""

    if is_path:
        start_path = sys.argv.index("-d") + 1
        try:
            end_path = sys.argv.index("-f")
        except ValueError:
            end_path = len(sys.argv)
        directory = os.path.join(*sys.argv[start_path: end_path])
        os.makedirs(directory, exist_ok=True)
        path_to_file = f"{directory}\\"

    if is_file:
        file_name = sys.argv[-1]
        key = "a" if os.path.exists(path_to_file + file_name) else "w"
        with open(path_to_file + file_name, key) as file:
            file.write(
                f"{datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\n"
            )
            while True:
                text = input("Enter content line: ")
                if text == "stop":
                    break
                file.write(f"{text}\n")


create_file("-d" in sys.argv, "-f" in sys.argv)
