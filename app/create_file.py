import sys
import os
import datetime


arguments_list = sys.argv


def create_directories(arguments_list: list) -> None:
    if "-f" in arguments_list:
        new_dir = "/".join(arguments_list[2:-2])
    else:
        new_dir = "/".join(arguments_list[2:])
    os.makedirs(new_dir)
    return new_dir


def write_in_file(arguments_list: list) -> None:
    file_name = arguments_list[-1]
    if "-d" in arguments_list:
        new_dir = create_directories(arguments_list)
        path_to_file = f"{new_dir}/{file_name}"
    else:
        path_to_file = file_name
    with open(path_to_file, "a") as new_file:
        now = datetime.datetime.now()
        time_to_append = now.strftime("%Y-%d-%m %H:%M:%S")
        new_file.write(time_to_append + "\n")
        input_line = "start"
        count = 1
        while input_line != "stop":
            input_line = input("Enter content line: ")
            if input_line != "stop":
                new_file.write(str(count) + " " + input_line + "\n")
                count += 1
                continue
            new_file.write("\n")


if __name__ == "__main__":
    write_in_file(arguments_list)
