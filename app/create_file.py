from datetime import datetime
import os
import sys

input_data = sys.argv


def write_in_file(file_path: str) -> None:
    current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    line_number = 1

    file_exists = os.path.isfile(file_path)

    with open(file_path, "a") as work_file:
        if file_exists:
            work_file.write("\n")
        work_file.write(current_date + "\n")
        while True:

            input_text = input("Enter content line: ")
            if input_text == "stop":
                break

            work_file.write(f"{line_number} {input_text}\n")
            line_number += 1


if "-d" in input_data:
    d_index = input_data.index("-d")
    if "-f" not in input_data:
        os.makedirs(os.path.join(*input_data[d_index + 1:]), exist_ok=True)
    else:
        f_index = input_data.index("-f")
        if f_index > d_index:
            dir_path = os.path.join(*input_data[d_index + 1:f_index])
        else:
            dir_path = os.path.join(*input_data[d_index + 1:])

        os.makedirs(dir_path, exist_ok=True)

        file_path = os.path.join(dir_path, input_data[f_index + 1])

        write_in_file(file_path)
else:
    f_index = input_data.index("-f")
    file_path = input_data[f_index + 1]
    write_in_file(file_path)
