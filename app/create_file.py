import os
import sys
import datetime


def create_folders(directions: list) -> str:
    directions_to_file = os.path.join(*directions)

    if not os.path.exists(directions_to_file):
        os.makedirs(directions_to_file)
    return directions_to_file


def write_to_file(file_name: str, path: str = "") -> None:
    full_path = os.path.join(path, file_name)

    with open(full_path, "a") as file:
        now = datetime.datetime.now()
        formatted_time = now.strftime("%Y-%m-%d %H:%M:%S")

        file.write(str(formatted_time) + "\n")
        counter_lines = 1

        while True:
            content = input("Enter content line: ")

            if content == "stop":
                file.write(f"\n")
                break

            file.write(f"{counter_lines} {content}\n")
            counter_lines += 1


if "-d" in sys.argv and "-f" not in sys.argv:
    folder_path = create_folders(sys.argv[sys.argv.index("-d") + 1:])
elif "-f" in sys.argv and "-d" not in sys.argv:
    file_name = sys.argv[sys.argv.index("-f") + 1]
    write_to_file(file_name)
elif "-f" in sys.argv and "-d" in sys.argv:
    index_d = sys.argv.index("-d")
    index_f = sys.argv.index("-f")
    folder_path = create_folders(sys.argv[index_d + 1:index_f])
    file_name = sys.argv[index_f + 1]
    write_to_file(file_name=file_name, path=folder_path)
