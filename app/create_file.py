from datetime import datetime
import os
import sys


def parse_command() -> None:
    dir_names = []
    file_name = ""
    arguments = sys.argv
    if "-d" not in arguments and "-f" not in arguments:
        print("Invalid command: You should add -f or/and -d flags to create "
              "new file or/and directories")
        return
    if "-d" in arguments:
        start_index = arguments.index("-d") + 1
        for directory in arguments[start_index:]:
            if directory == "-f":
                break
            dir_names.append(directory)
        if not dir_names:
            print("Invalid command: Nothing to create! Type new directories "
                  "names separated by whitespace after flag -d")
            return
    if "-f" in arguments:
        try:
            file_name = arguments[arguments.index("-f") + 1]
        except IndexError:
            print("Invalid command: After -f flag you should type new "
                  "filename")
            return
        if file_name == "-d":
            print("Invalid command: After -f flag you should type new "
                  "filename, not another flag")
            return
    new_path = os.path.join(os.getcwd(), *dir_names)
    os.makedirs(new_path, exist_ok=True)
    if file_name:
        if not os.path.isfile(os.path.join(new_path, file_name)):
            file_handing(new_path, file_name, "w")
            return
        file_handing(new_path, file_name, "a")


def file_handing(file_path: str, filename: str, mode: str) -> None:
    with open(os.path.join(file_path, filename), mode) as file:
        file_content = []
        if file.mode == "a":
            file.write("\n")
        while True:
            new_line = input("Enter content line:")
            if new_line.lower() == "stop":
                break
            file_content.append(new_line)
        file.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")
        for line_number, line_text in enumerate(file_content):
            file.write(str(line_number + 1) + " " + line_text + "\n")


if __name__ == "__main__":
    parse_command()
