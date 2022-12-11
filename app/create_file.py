import sys
import datetime
import os


def create_folder(info_list: list) -> str:
    path_of_folder = ""
    folder_name_index = info_list.index("-d") + 1

    while folder_name_index < len(info_list):
        os.mkdir(path_of_folder + info_list[folder_name_index])
        path_of_folder += info_list[folder_name_index] + "/"
        folder_name_index += 1

    return path_of_folder


def create_file(info_list: list) -> str:
    content_line = 1
    file_name = info_list[info_list.index("-f") + 1]

    with open(file_name, "a") as file:
        write_date = datetime.datetime.now()
        file.write(write_date.strftime("%y-%m-%d %H:%M:%S\n"))

        while True:
            new_line = input("Enter content line: ")

            if new_line == "stop":
                file.write("\n")
                break

            file.write(f"{content_line} {new_line}\n")
            content_line += 1
    return file_name


def create_folder_and_create_file(list_info: list) -> None:
    saved_folder_path = create_folder(
        list_info[list_info.index("-d"):list_info.index("-f")]
    )

    saved_file_name = create_file(
        list_info[list_info.index("-f"):]
    )

    path_to_move_file = saved_folder_path \
        + saved_file_name

    os.replace(saved_file_name, path_to_move_file)


if "-f" not in sys.argv:
    create_folder(sys.argv)

if "-d" not in sys.argv:
    create_file(sys.argv)

if "-f" in sys.argv and "-d" in sys.argv:
    create_folder_and_create_file(sys.argv)
