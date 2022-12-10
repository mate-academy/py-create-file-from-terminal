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
    # Create folder(s) and save folder(s) path into a variable:
    folder_path = create_folder(
        list_info[list_info.index("-d"):list_info.index("-f")]
    )
    # Create file and save file name into a variable:
    file_name = create_file(
        list_info[list_info.index("-f"):]
    )
    # Move file into created folder(s):
    os.replace(file_name, folder_path + file_name)


if "-f" not in sys.argv:
    create_folder(sys.argv)

if "-d" not in sys.argv:
    create_file(sys.argv)

if "-f" in sys.argv and "-d" in sys.argv:
    create_folder_and_create_file(sys.argv)
