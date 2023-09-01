import argparse
from datetime import datetime
import os


def create_file() -> None:
    parser = argparse.ArgumentParser()

    parser.add_argument("-d", type=str, nargs="*", help="create directory")
    parser.add_argument("-f", type=str, help="create file")

    args = parser.parse_args()

    directory_path = os.path.join(*args.d) if args.d else ""
    file_name_with_path = os.path.join(
        directory_path, args.f
    ) if args.f else ""

    os.makedirs(directory_path, exist_ok=True)

    file_mode = "a" if os.path.exists(file_name_with_path) else "w"

    with open(file_name_with_path, file_mode) as output_file:
        line_count = 1
        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        output_file.write(f"{date}\n")

        while True:
            another_message = "Another " if file_mode == "a" else ""
            input_message = (f"Enter content line: "
                             f"{another_message}Line{line_count} ")
            output_message = f"{line_count} {another_message}Line{line_count} "

            input_text = input(input_message)

            if input_text == "stop":
                output_file.write("\n")
                break

            output_file.write(f"{output_message} {input_text} \n")
            line_count += 1


create_file()
