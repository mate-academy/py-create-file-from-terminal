import os
import sys
from datetime import datetime


entered_data = sys.argv
print(entered_data)
directory_path = "."

if "-d" in entered_data:
    index_d = entered_data.index("-d")
    if "-f" in entered_data:
        index_f = entered_data.index("-f")
        path = entered_data[index_d + 1:index_f]
    else:
        path = entered_data[index_d + 1:]
    directory_path = os.path.join(*path)
    print(directory_path)
    os.makedirs(directory_path, exist_ok=True)

if "-f" in entered_data:
    index_f = entered_data.index("-f")
    file_name = entered_data[index_f + 1]
    file_path = os.path.join(directory_path, file_name)
    with open(file_path, "a") as file:
        text = ""
        current_date = datetime.now()
        timestamp = current_date.strftime("%Y-%m-%d %H:%M:%S")
        file.write("\n")
        file.write(str(timestamp) + "\n")
        counter = 1
        while text != "stop":
            text = input("Enter content line: ")
            if text != "stop":
                file.write(f"{counter} {text}" + "\n")
                counter += 1
