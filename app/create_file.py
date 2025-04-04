from sys import argv
from os import makedirs, path
from datetime import datetime

terminal = argv[1:]

def write_into_file(our_path: str) -> None:
    filename_index = terminal.index("-f") + 1 if "-f" in terminal else -1
    our_path = path.join(our_path, terminal[filename_index])
    line_number = 1  # Initialize line counter
    with open(our_path, "a") as file:
        file.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")
        while True:
            file_text = input("Enter content line: ")
            if file_text == "stop":
                break
            file.write(f"{line_number} {file_text}\n")
            line_number += 1

def d_and_f_flags() -> None:
    our_path = path.join(*terminal[1:terminal.index("-f")])
    makedirs(our_path, exist_ok=True)  # Ensure directory is created if not exists
    write_into_file(our_path)

def d_flag() -> None:
    our_path = path.join(*terminal[1:])
    makedirs(our_path, exist_ok=True)

def f_flag() -> None:
    filename = terminal[1] if len(terminal) > 1 else "default.txt"
    our_path = path.join(".", filename)  # Assume current directory if no path provided
    write_into_file(our_path)

if "-f" in terminal and "-d" in terminal:
    d_and_f_flags()
elif "-d" in terminal:
    d_flag()
else:
    f_flag()
