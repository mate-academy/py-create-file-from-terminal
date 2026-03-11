import sys
import os
import datetime


def create_file() -> None:
    now = datetime.datetime.now()
    date = now.strftime("%Y-%m-%d %H:%M:%S")
    list_dirs = []
    filename = None
    current_flag = None

    for arg in sys.argv:
        if arg == "-d":
            current_flag = "-d"
        elif arg == "-f":
            current_flag = "-f"
        else:
            if current_flag == "-d":
                list_dirs.append(arg)
            if current_flag == "-f":
                filename = arg
    if list_dirs:
        os.makedirs(os.path.join(*list_dirs), exist_ok=True)

    if filename:
        full_path = os.path.join(*list_dirs, filename)
        file_exists = os.path.exists(full_path)

        with open(os.path.join(*list_dirs, filename), "a") as file:
            if file_exists:
                file.write("\n")

            file.write(f"{date}\n")
            count = 0

            while True:
                line = input("Enter content line:")

                if line == "stop":
                    break
                else:
                    count += 1
                    file.write(f"{count} {line}\n")
