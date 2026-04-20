import sys
import os
import datetime


def create_file(file_name: str) -> None:
    with open(file_name, "a") as file:
        if os.path.getsize(file_name) > 0:
            file.write("\n")
        file.write(str(
            datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S\n")))
        line_number = 1
        while True:
            input_content = input("Enter content line: ")
            if input_content == "stop":
                break

            if line_number > 1:
                file.write("\n")
            file.write(f"{line_number} {input_content}")
            line_number += 1

        file.write("\n")


def main() -> None:
    cmd_text = sys.argv

    correct_path = None

    if "-d" in cmd_text:
        index_d = cmd_text.index("-d")
        if "-f" in cmd_text:
            index_f = cmd_text.index("-f")
            correct_path = os.path.join(*cmd_text[index_d + 1: index_f])
        else:
            correct_path = os.path.join(*cmd_text[index_d + 1:])
        os.makedirs(correct_path, exist_ok=True)

    if "-f" in cmd_text:
        index_f = cmd_text.index("-f")
        file_name = cmd_text[index_f + 1]
        if correct_path is None:
            create_file(file_name)
        else:
            create_file(os.path.join(correct_path, file_name))


if __name__ == "__main__":
    main()
