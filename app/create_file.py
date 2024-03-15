import sys
import os
from datetime import datetime


def create_file_from_terminal() -> None:
    command_line = sys.argv

    if "-d" in command_line:
        index_d = command_line.index("-d")
        if "-f" in command_line:
            index_f = command_line.index("-f")
            dir_path = command_line[index_d + 1:index_f]
        else:
            dir_path = command_line[index_d + 1:]

        dir_path = os.path.join(*dir_path)

        os.makedirs(dir_path, exist_ok=True)

    if "-f" in command_line:
        file_name = command_line[command_line.index("-f") + 1]
        if "-d" in command_line:
            file_name = os.path.join(dir_path, file_name)
        with open(file_name, "a") as file:
            file.write(str(datetime.now().strftime("%Y-%m-%d %H:%M:%S\n")))
            number_of_line = 1
            while True:
                input_line = input("Enter content line:")
                if input_line == "stop":
                    file.write("\n")
                    break

                file.write(f"{number_of_line} {input_line}\n")
                number_of_line += 1


if __name__ == "__main__":
    create_file_from_terminal()
