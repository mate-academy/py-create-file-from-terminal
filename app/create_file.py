import datetime
import sys
import os


def create_file() -> None:
    current_time = datetime.datetime.now()
    directory_path = None
    output_filename = None
    is_directory_flag = False
    i = 1
    while i < len(sys.argv):
        if sys.argv[i] == "-d":
            is_directory_flag = True
        elif sys.argv[i] == "-f":
            is_directory_flag = False
        else:
            if is_directory_flag:
                directory_path = os.path.join(
                    directory_path or "",
                    sys.argv[i]
                )
            else:
                output_filename = sys.argv[i]
        i += 1

    if directory_path:
        os.makedirs(directory_path, exist_ok=True)

    if output_filename:
        file_path = os.path.join(directory_path or ".", output_filename)
        with open(file_path, "a") as file:
            file.write(f"{current_time.strftime('%Y-%m-%d %H:%M:%S')}\n")
            count_lines = 1

            while True:
                user_input = input("Enter content line:")
                if user_input.lower() == "stop":
                    file.write("\n")
                    break
                file.write(f"{count_lines} {user_input}\n")
                count_lines += 1


create_file()
