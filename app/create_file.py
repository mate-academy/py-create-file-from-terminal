import argparse
from datetime import datetime
import os
#directory_path: str, file_name: str, file_content: str

def create_file() -> None:
    # why did i spell it create_life at first
    # parser / flag setup
    parser = argparse.ArgumentParser(description=\
        "Create a file with inputted name and content.")

    #flags setup
    parser.add_argument('-d', metavar="directory-name",\
        type=str, help="Enter a directory for new file.")

    parser.add_argument('-f', metavar="file-name",\
        type=str, help="Enter a name for new file.")

    args = parser.parse_args()

    if args.d:
        os.makedirs(args.d, exist_ok=True)
        directory_path = args.d
    else:
        directory_path = input("Enter directory path: ")
    os.makedirs(directory_path, exist_ok=True)

    if args.f:
        file_name = args.f
    else:
        file_name = input("Enter file_name: ")

    file_path = os.path.join(directory_path, file_name)

    # file content detup
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(file_path, "a") as file:
        if os.path.getsize(file_path) > 0:
            file.write("\n" + current_time + "\n")
        else:
            file.write(current_time + "\n")

        while True:
            file_content = input("Enter file_content: ")
            if file_content.lower() == "stop":
                break
            else:
                file.write(file_content + "\n")


create_file()
