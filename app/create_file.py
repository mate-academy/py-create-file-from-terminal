import os
import sys
import datetime


def name_and_path(args: list[str]) -> tuple[list[str], str | None]:
    file_name = None
    dir_parts =[]
    f_index = None
    d_index = None
    if "-f" in args:
        f_index = args.index("-f")
        if f_index + 1 < len(args):
            file_name = args[f_index + 1]
    if "-d" in args:
        d_index = args.index("-d")
        end_index = f_index if f_index is not None else len(args)
        dir_parts = args[d_index + 1 : end_index]
    return dir_parts, file_name


def user_input() -> list:
    user_text = []
    while True:
        text = input("Enter content line: ")
        if text == "stop":
            break
        user_text.append(text)
    return user_text


def write_to_file(full_filename : str, user_text : list[str]) -> None:
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    lines_to_write = [timestamp]
    for index, item in enumerate(user_text, start=1):
        formatted_line = f"{index} {item}"
        lines_to_write.append(formatted_line)
    file_exists_and_not_empty = (os.path.exists(full_filename)
                                 and os.path.getsize(full_filename) > 0)
    with open(full_filename, "a", encoding="utf-8") as output_file:
        if file_exists_and_not_empty:
            output_file.write("\n")
        output_file.write("\n".join(lines_to_write) + "\n")


def main() -> None:
    args = sys.argv[1:]
    dir_parts, file_name = name_and_path(args)
    dir_path = os.path.join(*dir_parts) if dir_parts else "."
    if dir_path != ".":
        os.makedirs(dir_path, exist_ok=True)
    if file_name:
        full_path = os.path.join(dir_path, file_name)
        content = user_input()
        if content:
            write_to_file(full_path, content)


if __name__ == "__main__":
    main()
