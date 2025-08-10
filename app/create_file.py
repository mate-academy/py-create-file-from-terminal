import datetime
import os
import sys


def main() -> None:
    file_data = sys.argv[1:]

    if "-d" not in file_data and "-f" not in file_data:
        raise Exception("At least one of the -d or -f flags must be provided.")

    directories = []
    if "-d" in file_data:
        d_index = file_data.index("-d")

        for i in range(d_index + 1, len(file_data)):
            if file_data[i] == "-f":
                break
            directories.append(file_data[i])

        directory_path = os.path.join(*directories)
        os.makedirs(directory_path, exist_ok=True)

    if "-f" in file_data:
        f_index = file_data.index("-f")
        if f_index + 1 >= len(file_data):
            raise Exception("No file name provided.")

        content = datetime.datetime.now().strftime("%Y-%m-%d %H:%m:%S") + "\n"

        content_line = input("Enter content line: ")
        line_number = 1
        while content_line != "stop":
            content += f"{line_number} {content_line}\n"
            line_number += 1
            content_line = input("Enter content line: ")
        content += "\n"

        new_file_name = file_data[f_index + 1]
        with open(os.path.join(*directories, new_file_name), "a") as new_file:
            new_file.write(content)


if __name__ == "__main__":
    main()
