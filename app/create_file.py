import sys
import datetime
import os


def create_file(path_to_file: str) -> None:
    blank_line = ""
    if os.path.exists(
            os.path.join(
                path_to_file,
                sys.argv[sys.argv.index("-f") + 1]
            )
    ):
        blank_line += "\n"
    with open(
            os.path.join(
                path_to_file,
                sys.argv[sys.argv.index("-f") + 1]
            ), "a"
    ) as f:
        f.write(blank_line)
        f.write(f"{str(datetime.datetime.now()).split('.')[0]}\n")
        number_line = 1
        while True:
            file_content = input("Enter content line: ")
            if file_content == "stop":
                break
            f.write(f"{number_line} {file_content}\n")
            number_line += 1


directory_path = "."

if "-d" in sys.argv:
    directory_path = os.path.join(
        *[directory for directory in sys.argv[sys.argv.index("-d") + 1:]
          if directory != "-f" and not directory.endswith(".txt")]
    )
    os.makedirs(directory_path, exist_ok=True)

if "-f" in sys.argv:
    create_file(directory_path)
