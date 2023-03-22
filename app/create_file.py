from datetime import datetime
import os
import sys


def get_flag_index(command: list[str], flag: str) -> int:
    return command.index(flag)


def create_dirs(paths: list[str]) -> str:
    path = os.path.join(*paths)
    os.makedirs(path, exist_ok=True)
    return path


def write_to_file(*args) -> None:
    line_count = 0

    with open(os.path.join(*args), "a+") as output_file:
        output_file.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")
        while True:
            user_input = input("Enter content line: ")

            if user_input == "stop":
                output_file.write("\n")
                break

            line_count += 1
            output_file.write(f"{line_count} {user_input}\n")


def main() -> None:
    command = sys.argv

    if "-f" in command and "-d" not in command:
        filename = command[get_flag_index(command, "-f") + 1]
        write_to_file(filename)

    if "-d" in command and "-f" not in command:
        paths = command[get_flag_index(command, "-d") + 1:]
        create_dirs(paths)

    if "-f" in command and "-d" in command:
        filename = command[get_flag_index(command, "-f") + 1]
        paths = command[get_flag_index(command, "-d") + 1
                        :get_flag_index(command, "-f")]
        write_to_file(create_dirs(paths), filename)


main()
