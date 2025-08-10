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

    if first_command == "-d" and second_command is None:
        dst_dir = Path(*data)
        dst_file = dst_dir / "new_file.txt"

    elif first_command == "-f" and second_command is None:
        dst_file = Path(*data)
        dst_dir = dst_file.parent

    elif first_command == "-d" and second_command == "-f":
        dst_dir = Path(*data)
        dst_file = dst_dir / "new_file.txt"

    else:
        print("Invalid command. Use '-d' for directory or '-f' for file.")
        return

    try:
        dst_dir.mkdir(parents=True, exist_ok=True)
        print(f"Directory '{dst_dir}' created successfully.")
    except Exception as e:
        print(f"Error creating directory: {e}")

    try:
        write_data(dst_file)
        print(f"File '{dst_file}' created/modified successfully.")
    except Exception as e:
        print(f"Error creating/modifying file: {e}")


if __name__ == "__main__":
    init_data(sys.argv[1:])
