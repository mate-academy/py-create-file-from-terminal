import os
import sys
import datetime


def make_dirs(path_file: str, input_list: list) -> str:
    if input_list is None:
        raise TypeError("input_list cannot be None")
    try:
        d_index = input_list.index("-d") + 1
    except ValueError:
        return str(path_file)
    dirs = []
    for element in input_list[d_index:]:
        if element == "-f":
            break
        dirs.append(element)
    full_path = os.path.join(path_file, *dirs)
    os.makedirs(full_path, exist_ok=True)
    return str(full_path)


def create_file(input_list: list, dir_path: str = "") -> None:
    if input_list is None:
        raise TypeError("input_list cannot be None")

    dt = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    txt_file_name = "".join([element
                             for element in input_list
                             if ".txt" in element])
    full_path = os.path.join(dir_path, txt_file_name)

    with open(full_path, "a") as f:
        if os.path.getsize(full_path) != 0:
            f.write("\n\n")
        f.write(f"{dt}\n")
        counter = 1
        while True:
            str_line = input("Enter content line: ")
            if str_line.lower() == "stop":
                break
            f.write(f"{counter} {str_line}\n")
            counter += 1


def main() -> None:
    current_path_file = os.path.dirname(os.path.abspath(__file__))
    terminal_input = sys.argv

    if "-d" in terminal_input and "-f" in terminal_input:
        result_dir = make_dirs(current_path_file, terminal_input)
        create_file(terminal_input, result_dir)
    elif "-d" in terminal_input:
        make_dirs(current_path_file, terminal_input)
    elif "-f" in terminal_input:
        create_file(terminal_input, current_path_file)


if __name__ == "__main__":
    main()
