from sys import argv
import os
from datetime import datetime


def main() -> None:
    work_string = argv

    # work_string = ['./app/create_file.py', '-d', 'test_dir', 'test_file']   # Для тестов

    if "-d" not in work_string:
        if "-f" not in work_string:
            print("This not work parameters string, "
                  "print current string:\n"
                  "' -d Name_New_Folder' add [new folder], "
                  "'-f Name_New_File' add new file")
            return
    if work_string.count('-d') > 1:
        print("This not work parameters string,\n"
              "you have multiple ""-d"" flags to create folders")
        return
    if work_string.count('-f') > 1:
        print("This not work parameters string,\n"
              "you have multiple ""-f"" flags to create files")
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
                print(f"This folder: '{path_folder}' already exists and will not be created")

    if len(work_file) != 0:
        if not path_folder:
            new_file = f"{work_file[0]}"
        else:
            new_file = f"{path_folder}/{work_file[0]}"
            with open(new_file + ".txt", "w") as work_file_w:
                now = datetime.now()
                date_time = now.strftime("%Y-%m-%d %H:%M:%S")
                work_file_w.write(date_time + "\n")
                while True:
                    work_line = input("Enter new line of content: ")
                    if work_line == "stop":
                        break
                    else:
                        work_file_w.write(work_line + "\n")


if __name__ == "__main__":
    main()
