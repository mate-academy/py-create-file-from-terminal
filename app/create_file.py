import datetime
import sys
import os


def file_handling(path: str) -> None:
    """
    This function at first creates line with date and time of addition text,
    then added line by line all users inputs with numbers
    """
    with open(path, "a") as text_file:
        text_file.write(f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        line_number = 1
        while True:
            content = input("Enter content line: ")
            if content == "stop":
                text_file.write("\n")
                break
            text_file.write(f"{line_number} {content}\n")
            line_number += 1


def create_file_func() -> None:
    """
    This function take arguments from terminal command,
    check, if there is "-d" or "-f" flags and creates path to file
    has to be created, then calls file_handling() function.
    """
    arg_list = sys.argv
    file_name = arg_list[-1]
    if "-d" in arg_list:
        new_list = arg_list[arg_list.index("-d") + 1:]
        if "-f" in new_list:
            new_list = new_list[0:new_list.index("-f")]
            file_path = "/".join(new_list) + "/" + file_name
            os.makedirs("/".join(new_list), exist_ok=True)
            file_handling(path=file_path)
        else:
            os.makedirs("/".join(new_list))
    elif "-f" in arg_list:
        file_handling(path=file_name)


if __name__ == '__main__':
    create_file_func()
