import os
import sys



def create_file() -> None:
    print(sys.argv)

    full_path = ""
    file_name = ""

    is_dir = False
    is_file = False

    for item in sys.argv:
        if item == "-d":
            is_dir = True
            is_file = False
            continue

        if item == "-f":
            is_dir = False
            is_file = True
            continue

        if is_dir:
            full_path = os.path.join(full_path, item)

        if is_file:
            file_name = item

    input_str = ""
    while input_str != "stop":
        input_str = input("Enter content line: ")
        if input_str == "stop":
            break



create_file()
