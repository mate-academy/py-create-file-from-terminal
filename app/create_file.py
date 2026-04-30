import sys
import os
import datetime


data = sys.argv


def write_file(filepath: str) -> None:
    if os.path.exists(filepath):
        with open(filepath, "a") as file:
            file.write("\n")
            file.write(datetime.datetime.now().strftime("%Y-%m-%d "
                                                        "%H:%M:%S") + "\n")
            line_number = 1
            while True:
                text = input("Enter content line: ")
                if text == "stop":
                    break
                file.write(f"{line_number} {text}\n")
                line_number += 1
    else:
        with open(filepath, "w") as file:
            file.write(datetime.datetime.now().strftime("%Y-%m-%d "
                                                        "%H:%M:%S") + "\n")
            line_number = 1
            while True:
                text = input("Enter content line: ")
                if text == "stop":
                    break
                file.write(f"{line_number} {text}\n")
                line_number += 1


if "-d" in data:
    dirs = []
    for item in data[data.index("-d") + 1:]:
        if item in "-f":
            break
        dirs.append(item)

    path = os.path.join(*dirs) if dirs else "."
    os.makedirs(path, exist_ok=True)

    if "-f" in data:
        filename = str(data[data.index("-f") + 1])
        write_file(os.path.join(path, filename))

elif "-f" in data:
    write_file(str(data[data.index("-f") + 1]))
