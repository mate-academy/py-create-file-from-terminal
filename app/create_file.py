import os
import sys
import datetime


def create_file_from_terminal() -> None:
    terminal_data = sys.argv
    d_index = terminal_data.index("-d") if "-d" in terminal_data else None
    f_index = terminal_data.index("-f") if "-f" in terminal_data else None

    dir_parts = []
    dir_path = ""

    if d_index is not None:
        dir_parts = terminal_data[d_index + 1:]
        if "-f" in dir_parts:
            dir_parts = dir_parts[:dir_parts.index("-f")]

        if dir_parts:
            dir_path = os.path.join(*dir_parts)
            os.makedirs(dir_path, exist_ok=True)

    if f_index is not None:
        file_name = terminal_data[f_index + 1]
        final_file_path = os.path.join(dir_path, file_name)

        is_file_exist = (os.path.exists(final_file_path)
                         and os.path.getsize(final_file_path) > 0)

        with open(final_file_path, "a") as f:
            if is_file_exist:
                f.write("\n")

            now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            f.write(f"{now}\n")
            number_of_line = 1
            while True:
                string_input = input("Enter content line: ")
                if string_input.lower() == "stop":
                    break
                else:
                    f.write(f"{number_of_line} {string_input}\n")
                    number_of_line += 1


if __name__ == "__main__":
    create_file_from_terminal()
