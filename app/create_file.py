import sys
import os
import datetime


data = sys.argv


def write_file(filepath: str) -> None:
    with open(filepath, "w") as file:
        file.write(str(datetime.datetime.now().replace(microsecond=0)) + "\n")
        while True:
            text = input("Enter content line:")
            if text == "stop":
                break
            file.write(text + "\n")


analyzed_data = []
if "-d" in data:
    for i in range(len(data)):
        if data[i] != "-f":
            analyzed_data.append(data[i])
        else:
            path = "/".join(analyzed_data[2:])
            os.makedirs(path)
            current_filepath = os.path.join(path, data[i + 1] + ".txt")
            write_file(current_filepath)
            break
    os.makedirs("/".join(analyzed_data[2:]), exist_ok=True)

if "-f" in data and "-d" not in data:
    write_file(data[-1] + ".txt")
