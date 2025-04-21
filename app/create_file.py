import sys
import os
from datetime import datetime


def create_file(name_file: str) -> None:
    with open(name_file, "a") as file:
        file.write(datetime.now().strftime("%Y-%d-%m %H:%M:%S") + "\n")
        count = 1
        while True:
            text = input("Enter content line:")
            if text.lower() == "stop":
                file.write("\n")
                break
            file.writelines(f"{count} {text}\n")
            count += 1


if __name__ == "__main__":
    create_new_info = sys.argv

    if "-d" in create_new_info and "-f" in create_new_info:
        new_dir = "\\".join(create_new_info[
                            create_new_info.index("-d") + 1:
                            create_new_info.index("-f")])

        if not os.path.exists(f"{os.getcwd()}\\{new_dir}"):
            os.makedirs(new_dir)

        os.chdir(new_dir)
        create_file(create_new_info[-1])

    elif "-d" in create_new_info:
        new_dir = "\\".join(create_new_info[create_new_info.index("-d") + 1:])
        if not os.path.exists(f"{os.getcwd()}\\{new_dir}"):
            os.makedirs(new_dir)
    elif "-f" in create_new_info:
        create_file(create_new_info[-1])
