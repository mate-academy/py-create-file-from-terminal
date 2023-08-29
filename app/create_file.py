"""Simple folders and file creator.

This script create folders and file,
that takes directory path, file name,
file content from the terminal and creates file

 - If only -d
 flag passed, means all items after this flag are parts of the path
 - If only -f
 flag passed, means first item is the file name
"""

from sys import argv
import os
from datetime import datetime


def parameter_check(work_string: list) -> bool:
    if "-d" not in work_string:
        if "-f" not in work_string:
            print("This not work parameters string, "
                  "print current string:\n"
                  "' -d Name_New_Folder' add [new folder], "
                  "'-f Name_New_File' add new file")
            return False
    if work_string.count("-d") > 1:
        print("This not work parameters string,\n"
              "you have multiple ""-d"" flags to create folders")
        return False
    if work_string.count("-f") > 1:
        print("This not work parameters string,\n"
              "you have multiple ""-f"" flags to create files")
        return False
    return True


def create_file(work_file: list, path_folder: str) -> None:
    if len(work_file) != 0:
        new_file = f"{path_folder}/{work_file[0]}"
        if os.path.isfile(new_file + ".txt"):
            with open(new_file + ".txt", "a") as work_file_w:
                now = datetime.now()
                work_file_w.write("\n")
                date_time = now.strftime("%Y-%m-%d %H:%M:%S")
                work_file_w.write(date_time + "\n")
                number_string = 1
                while True:
                    work_line = input("Enter new line of content: ")
                    if work_line == "stop":
                        break
                    else:
                        work_file_w.write(f"{number_string} {work_line} \n")
                        number_string += 1
        else:
            with open(new_file + ".txt", "w") as work_file_w:
                now = datetime.now()
                date_time = now.strftime("%Y-%m-%d %H:%M:%S")
                work_file_w.write(date_time + "\n")
                number_string = 1
                while True:
                    work_line = input("Enter new line of content: ")
                    if work_line == "stop":
                        break
                    else:
                        work_file_w.write(f"{number_string} {work_line} \n")
                        number_string += 1


def main() -> None:
    if "-h" in argv[1:] or "--help" in argv[1:]:
        print(
            """Usage: python create_file.py [OPTION] ...\n
            -h, --help  display this help and exit\n
            -d [name_folders] create folders with attachments\n
            -f name_file create file """
        )
        exit()

    work_string = argv

    if not parameter_check(work_string):
        return

    work_folder = []
    work_file = []

    flag_d = False
    flag_f = False
    work_path = ""

    for index, work_data in enumerate(work_string):
        if index == 0:
            work_path = work_data
        else:
            if not flag_d:
                if work_data == "-d":
                    flag_d = True
            else:
                if work_data != "-f":
                    work_folder.append(work_data)

            if not flag_f:
                if work_data == "-f":
                    flag_f = True
                    flag_d = False
            else:
                work_file.append(work_data)

    dirpath, filename = os.path.split(work_path)

    path_folder = dirpath
    if len(work_folder) != 0:
        for new_folder in work_folder:
            try:
                path_folder = f"{path_folder}/{new_folder}"
                os.mkdir(path_folder)
            except FileExistsError:
                print(
                    f"This folder: '{path_folder}' "
                    f"already exists and will not be created"
                )

    create_file(work_file, path_folder)


if __name__ == "__main__":
    main()
