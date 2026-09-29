import os
import sys
import datetime


def create_file() -> None:
    if "-d" in sys.argv and "-f" not in sys.argv:
        directories_index = sys.argv.index("-d")
        dirs = sys.argv[directories_index + 1:]
        if len(dirs) == 0:
            return
        os.makedirs(os.path.join(*dirs), exist_ok=True)
        return
    if "-f" in sys.argv and "-d" not in sys.argv:
        file_to_create_index = sys.argv.index("-f")
        file_to_create = sys.argv[file_to_create_index + 1]
        date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        if os.path.exists(file_to_create):
            date_with_new_line = f"\n{date}\n"
        else:
            date_with_new_line = f"{date}\n"
        with open(file_to_create, "a") as file:
            file.write(f"{date_with_new_line}")
            line = 1
            while True:
                input_text = input("Enter content line: ")
                if input_text == "stop":
                    break
                file.write(f"{line} {input_text}\n")
                line += 1
        return
    if "-f" in sys.argv and "-d" in sys.argv:
        directories_index = sys.argv.index("-d")
        filename_index = sys.argv.index("-f")
        file_to_create = sys.argv[filename_index + 1]
        if directories_index < filename_index:
            directories_to_create = sys.argv[directories_index
                                             + 1:filename_index]
        else:
            directories_to_create = sys.argv[directories_index + 1:]
        directories_path = os.path.join(*directories_to_create)
        os.makedirs(directories_path, exist_ok=True)
        final_path = os.path.join(directories_path, file_to_create)
        date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        if os.path.exists(final_path):
            date_with_new_line = f"\n{date}\n"
        else:
            date_with_new_line = f"{date}\n"
        with open(final_path, "a") as file:
            file.write(date_with_new_line)
            line = 1
            while True:
                input_text = input("Enter content line: ")
                if input_text == "stop":
                    break
                file.write(f"{line} {input_text}\n")
                line += 1
        return


create_file()
