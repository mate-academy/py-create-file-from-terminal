import sys
import os
from datetime import datetime


def create_file() -> None:
    arguments = sys.argv[1:]
    file_name = "file.txt"
    directories = []
    if "-f" in arguments:
        if "-d" in arguments and "-f" in arguments:
            index_d = arguments.index("-d")
            index_f = arguments.index("-f")
            directories = arguments[(index_d + 1) : index_f]
            file_name = arguments[-1]
        if "-f" in arguments and "-d" not in arguments:
            file_name = arguments[-1]

        directories_path = os.path.join(*directories) if directories else ""
        file_name = str(file_name)
        destination = os.path.join(directories_path, file_name)
        if directories_path != "":
            if not os.path.exists(directories_path):
                os.makedirs(directories_path)

        with open(destination, "a+") as destination_file:
            content = []
            line = ""
            counter = 1
            while line != "stop":
                line = input("Enter content line: ")
                if line != "stop":
                    if destination_file.tell() == 0:
                        content.append(f"{counter} Line{counter} " + line)
                    else:
                        content.append(
                            f"{counter} Another line{counter} " + line
                        )
                counter += 1

            now = datetime.now()
            date_time = now.strftime("%Y-%m-%d %H:%M:%S")
            content.insert(0, date_time)
            content.append("")
            destination_file.write("\n".join(content))
    else:
        directories = arguments[(arguments.index("-d") + 1) :]
        directories_path = os.path.join(*directories)
        if not os.path.exists(directories_path):
            os.makedirs(directories_path)


if __name__ == "__main__":
    create_file()
