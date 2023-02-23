import sys
import os
import datetime


def file_creating() -> None:
    path, first_flag, *content = sys.argv
    if "-f" in content:
        *content, _, file_name = content
        path = os.path.join(os.getcwd(), *content, file_name)

    if first_flag == "-d":
        path_directories = os.path.join(os.getcwd(), *content)
        if not os.path.exists(path_directories):
            os.makedirs(path_directories)
    elif first_flag == "-f":
        path = os.path.join(os.getcwd(), *content)

    with open(path, "a") as file_out:
        user_input = []
        while True:
            prompt_user_input = input("Enter content line: ")
            if prompt_user_input == "stop":
                if user_input:
                    user_input[-1] += "\n"
                break
            user_input.append(prompt_user_input)
        current_time = datetime.datetime.now()
        date_str = current_time.strftime("%Y-%m-%d %H:%M:%S\n")
        file_out.write(date_str)
        for index, element in enumerate(user_input):
            file_out.write(f"{index + 1} {element}\n")
