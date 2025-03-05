import sys
import datetime
import os


def create_file_function() -> None:
    terminal = sys.argv
    if "-d" in terminal:
        directory = []
        index_d = terminal.index("-d")
        for dirs in range(index_d + 1, len(terminal)):
            if dirs != "-f":
                directory.append(dirs)
            else:
                break
        directory_in_str = "/".join(directory)
        os.makedirs(directory_in_str, exist_ok=True)

    if "-f" in terminal:
        index_f = terminal.index("-f")
        my_file = terminal[index_f + 1]
        pyth_file = my_file if "-d" not in terminal \
            else os.path.join(directory_in_str, my_file)

        with open(pyth_file, "a") as filee:
            date = datetime.datetime.now()
            formated_date = date.strftime("%Y-%m-%d %H:%M:%S")
            filee.write(f"{formated_date}\n")
            while True:
                new_line = input("Enter content line: ")
                if "stop" != new_line.strip():
                    format_for_write = f"{new_line}\n"
                    filee.write(format_for_write)
                else:
                    break
