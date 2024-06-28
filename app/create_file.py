import sys
import os
import datetime


def create_file() -> None:
    all_argv = sys.argv[1:]
    dirs_path = ""

    if "-d" in all_argv:
        if "-f" in all_argv:
            dirs_path = all_argv[1:all_argv.index("-f")]
        else:
            dirs_path = all_argv[1:]

        dirs_path = os.path.join(*dirs_path)
        os.makedirs(dirs_path, exist_ok=True)

    if "-f" in all_argv:
        file_name = all_argv[all_argv.index("-f") + 1]
        exists = False
        if os.path.exists(os.path.join(dirs_path, file_name)):
            exists = True
        with open(os.path.join(dirs_path, file_name), "a") as file:
            if exists:
                file.write("\n\n")
            file.write(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            line_counter = 1
            while True:
                entered_data = input("Enter content line: ")
                if entered_data == "stop":
                    break
                file.write(f"\n{line_counter} {entered_data}")
                line_counter += 1


if __name__ == "__main__":
    create_file()