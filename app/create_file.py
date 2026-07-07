import sys
import os
import datetime


def get_args(arg_start: str, arg_stop: str, args: list) -> list or str:
    res = []
    exact = False

    for command in args:
        if command == arg_start:
            exact = True
        elif command == arg_stop:
            exact = False
        elif exact:
            res.append(command)

    return res


def create_file_from_terminal() -> None:
    command_args = sys.argv

    dirs = get_args("-d", "-f", command_args)
    m_file = get_args("-f", "-d", command_args)

    if not m_file:
        return None

    if dirs:
        dirs_path = os.path.join(*dirs)

        if not os.path.exists(dirs_path):
            try:
                os.makedirs(dirs_path)
            except OSError as e:
                print(f"Error creating directory: {e}")
                return

        m_path = os.path.join(*[*dirs, *m_file])
    else:
        m_path = m_file

    with open(m_path, "a") as file:
        file.write(f"{str(datetime.datetime.now())}\n")
        line_counter = 0

        while True:
            line_counter += 1
            file_line = f"{input("Enter content line: ")}"

            if "stop" in file_line:
                return

            file.write(f"{line_counter} {file_line}\n")


create_file_from_terminal()
