import os
import sys
from datetime import datetime

for line in sys.stdin:
    if "python create_file.py" in line.rstrip():
        file_data: list[str] = line.rstrip().split()
        path = ""
        if "-d" in file_data:
            no_index: int = file_data.index("-d") + 1
            while file_data[no_index] != "-f":
                path = os.path.join(path, file_data[no_index])
                no_index += 1
            os.makedirs(path, exist_ok=True)
        if "-f" in file_data:
            try:
                no_index: int = file_data.index("-f") + 1
                path = os.path.join(path, file_data[no_index])
            except IndexError:
                print("You don't enter the file name!")
                break
        else:
            print("You don't enter the file name!")
            break
        with open(path, "a") as f:
            f.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            input_data = ""
            while True:
                input_data = input("Enter content line: ")
                if input_data == "stop":
                    f.write("\n")
                    break
                f.write(f"{input_data}\n")
            break
