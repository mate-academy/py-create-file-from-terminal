from sys import argv
import os


def main() -> None:
    # work_string = argv

    work_string = ['./app/create_file.py', '-f', 'tets']

    print(f"Only test {work_string}")
    if "-d" not in work_string:
        if "-f" not in work_string:
            print("This not work string, print current string!")
            return
    print("This is a working version.")

    work_folder = []
    work_file = []

    flag_d = False
    flag_f = False

    for work_data in work_string:
        if not flag_d:
            if work_data == "-d":
                flag_d = True
        if flag_d:
            if work_data != "-f":
                work_folder.append(work_data)
            if work_data == "-f":
                flag_f = True
                flag_d = False
        if flag_f:
            work_file.append(work_data)
        if not flag_f:
            if work_data == "-f":
                flag_f = True

    path_folder = ""
    if len(work_folder) != 0:
        for index, new_folder in enumerate(work_folder):
            if index == 0:
                os.mkdir(new_folder)
                path_folder = f"./{new_folder}"
            path_folder = f"{path_folder}/{new_folder}"
            os.mkdir(path_folder)

    if len(work_file) != 0:
        if not path_folder:
            new_file = f"{work_file[0]}"
        else:
            new_file = f"{path_folder}/{work_file[0]}"
        print(f"NEW FILE: {new_file}")
        with open(new_file + ".txt", "w") as work_file_w:
            while True:
                work_line = input("Enter new line of content: ")
                if work_line == "stop":
                    break
                else:
                    work_file_w.write(work_line + "\n")


if __name__ == "__main__":
    main()
