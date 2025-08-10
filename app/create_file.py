import sys
import os
import datetime


def content_writer(path: str) -> None:
    content_for_file = ""
    content_line = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    line_counter = 1
    while True:
        if "stop" in content_line:
            content_for_file += "\n"
            break
        content_for_file += content_line + "\n"
        content_line = (f"{str(line_counter)} "
                        f"{input('Enter content line: ')}")  # noqa
        line_counter += 1

    with open(path, "a") as new_file:
        new_file.write(content_for_file)


def create_app() -> None:
    command = sys.argv
    if "-d" in command and "-f" in command:
        file_name = None
        part_of_dir = []
        for part in sys.argv[2:]:
            if ("." not in part
                    and "-" not in part):
                part_of_dir.append(part)
            if "." in part:
                file_name = part

        joined_path = os.path.join(*part_of_dir)
        os.makedirs(joined_path, exist_ok=True)
        part_of_dir.append(file_name)
        path_with_file_name = os.path.join(*part_of_dir)

        content_writer(path_with_file_name)
        return

    flag = command[1]
    if flag == "-d":
        path = os.path.join(*command[2:])
        os.makedirs(path, exist_ok=True)
    if flag == "-f":
        content_writer(f"./{command[2]}")


if __name__ == "__main__":
    create_app()
