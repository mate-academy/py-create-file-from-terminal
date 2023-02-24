import sys
import os
import datetime


def file_creating(path: str) -> None:
    with open(path, "a") as file_out:
        if file_out.tell() != 0:
            file_out.write("\n")
        user_input = []
        while True:
            prompt_user_input = input("Enter content line: ")
            if prompt_user_input == "stop":
                break
            user_input.append(prompt_user_input)
        current_time = datetime.datetime.now()
        date_str = current_time.strftime("%Y-%m-%d %H:%M:%S\n")
        file_out.write(date_str)
        for index, element in enumerate(user_input):
            file_out.write(f"{index + 1} {element}\n")


def path_creating(first_flag: str, *path_details) -> str:
    if "-f" in path_details:
        *path_details, _, file_name = path_details
        path = os.path.join(os.getcwd(), *path_details, file_name)
    if first_flag == "-d":
        path_directories = os.path.join(os.getcwd(), *path_details)
        if not os.path.exists(path_directories):
            os.makedirs(path_directories)
    elif first_flag == "-f":
        path = os.path.join(os.getcwd(), *path_details)
    return path


if __name__ == "__main__":
    _, first_flag, *path_details = sys.argv
    path = path_creating(first_flag, *path_details)
    file_creating(path)
