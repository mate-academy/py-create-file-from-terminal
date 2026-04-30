import sys
import os
import datetime


data = sys.argv


def write_file(filepath: str) -> None:
    with open(filepath, "w") as file:
        file.write(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")
        while True:
            text = input("Enter content line:")
            if text == "stop":
                break
            file.write(text + "\n")


if "-d" in data:
    analyzed_data = []
    for item in data:
        if item == "-f":
            break
        analyzed_data.append(item)
    if "-f" in data:
        path = os.path.join(*analyzed_data[2:])
        os.makedirs(path)
        current_filepath = os.path.join(path, data[-1] + ".txt")
        write_file(str(current_filepath))
    else:
        os.makedirs(os.path.join(*analyzed_data[2:]), exist_ok=True)

if "-f" in data and "-d" not in data:
    write_file(data[-1] + ".txt")
