import sys
from datetime import datetime
from pathlib import Path


def write_data(file_name: Path) -> None:
    current_time = datetime.now()
    formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")

    with open(file_name, "a", encoding="utf-8") as file:
        file.write(formatted_time + "\n")
        line_number = 1
        while True:
            line = input(f"Enter content line {line_number}: ")
            if line.lower() == "stop":
                file.write("\n")
                break
            file.write(f"{line_number} {line}\n")
            line_number += 1


def init_data(data: list) -> None:
    if not data:
        print("No arguments provided. Use -d for "
              "directory or -f for file creation.")
        return

    first_command = data.pop(0)
    second_command = None

    if "-f" in data:
        second_command = data.pop(data.index("-f"))

    dst_dir = Path(*data).parent
    dst_file = Path(*data)

    if first_command == "-d" and second_command is None:

        try:
            dst_dir.mkdir(parents=True, exist_ok=True)
            print(f"Directory '{dst_dir}' created successfully.")
        except Exception as e:
            print(f"Error creating directory: {e}")
    elif first_command == "-f" and second_command is None:
        try:
            write_data(dst_file)
            print(f"File '{dst_file}' created/modified successfully.")

        except Exception as e:
            print(f"Error creating/modifying file: {e}")
    elif first_command == "-d" and second_command == "-f":

        try:
            dst_dir.mkdir(parents=True, exist_ok=True)
            write_data(dst_file)
            print(f"Directory '{dst_dir}' and file '{dst_file}'"
                  f" created/modified successfully.")
        except Exception as e:
            print(f"Error: {e}")
    else:
        print("Invalid command. Use '-d' for directory or '-f' for file.")


if __name__ == "main":
    init_data(sys.argv[1:])
