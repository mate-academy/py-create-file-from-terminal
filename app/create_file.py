import os
import datetime

from sys import argv


def create_file(file_name: str) -> None:
    chek_file = False

    if os.path.exists(file_name):
        chek_file = True

    page_number = 1
    file_content = ""

    while True:
        line_content = input("Enter content line: ")

        if line_content.lower() == "stop":
            break

        file_content += f"{page_number} {line_content}\n"
        page_number += 1

    with open(file_name, "a") as source_file:
        if chek_file:
            source_file.write("\n")

        time_output = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        source_file.write(f"{time_output}\n{file_content}")


def main() -> None:
    char_f = "-f"
    char_d = "-d"

    if char_f in argv and char_d in argv:
        index_f = argv.index("-f")
        index_d = argv.index("-d")

    if (char_f in argv and char_d in argv
            and index_f > index_d):
        directory_names = os.path.join(*argv[2:index_f:])
        file_name = os.path.join(*argv[index_f + 1::])
        os.makedirs(directory_names, exist_ok=True)
        os.chdir(directory_names)
        create_file(file_name)

    elif (char_f in argv and char_d in argv
          and index_f < argv.index(char_d)):
        directory_names = os.path.join(*argv[index_d + 1::])
        file_name = os.path.join(*argv[2:index_d:])
        os.makedirs(directory_names, exist_ok=True)
        os.chdir(directory_names)
        create_file(file_name)

    elif char_f in argv:
        file_name = argv[-1]
        create_file(file_name)

    elif char_d in argv:
        directory_names = os.path.join(*argv[2::])
        os.makedirs(directory_names, exist_ok=True)


if __name__ == "__main__":
    main()
