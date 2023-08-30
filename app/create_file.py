import os
import sys
import datetime


def create_file(file_name: str) -> None:
    with open(file_name, "a") as source_file:
        source_file.write(
            f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
        )
        line_number = 1
        while (content := input("Enter content line: ")) != "stop":
            source_file.write(f"{line_number} {content}\n")
            line_number += 1
        source_file.write("\n")


def create_dir(path: list) -> None:
    path = os.path.join(os.getcwd(), *path)

    if not os.path.exists(path):
        os.makedirs(path)
        os.chdir(path)


def main() -> None:
    terminal_input = sys.argv

    if "-d" in terminal_input and "-f" in terminal_input:
        d_index = terminal_input.index("-d")
        f_index = terminal_input.index("-f")
        create_dir(terminal_input[d_index + 1:f_index])
        create_file(terminal_input[-1])

    elif "-d" in terminal_input:
        path_ls = terminal_input[terminal_input.index("-d") + 1:]
        create_dir(path_ls)

    elif "-f" in terminal_input:
        create_file(terminal_input[-1])


if __name__ == "__main__":
    main()
