import datetime
import os


def write_new_file_with_input(file_path: list):
    path = "".join(file_path)
    if "-d" in path and "-f" in path:
        create_path(path[path.index('-d') + 3:path.index(" -f")])
        create_file(path[path.index("-f") + 3:])
    elif "-d" in path:
        create_path(path[path.index('-d') + 3:])
    else:
        create_file(path[path.index("-f") + 3:])


def create_path(check_flag_d: str):
    new_dir = check_flag_d.replace(" ", "/")
    os.makedirs(new_dir)
    os.chdir(os.path.join(os.getcwd(), new_dir))


def create_file(file_name: str):
    time_today = datetime.datetime.now()
    daytime_strf = time_today.strftime("%Y-%m-%d %H:%M:%S" + "\n")
    if os.path.exists("file.txt"):
        add_input = "Another"
    else:
        add_input = ""
    with open(file_name, "a") as add_newline:
        add_newline.write(f"{daytime_strf}\n")
        lines_num = 1
        while True:
            line = input("Enter content line: ")
            if line.lower() == "stop":
                break
            add_newline.write(f"{lines_num} {add_input} {line} content \n")
            lines_num += 1
