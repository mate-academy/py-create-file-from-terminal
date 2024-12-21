import datetime
import os
import sys

command = sys.argv[1]
file_name = sys.argv[2]
directory_name = f"{sys.argv[2]}/{sys.argv[3]}"

if command == "-f":
    with open(file_name, "w") as file:
        file.write(datetime.datetime.now()
                   .strftime("%Y-%m-%d %H:%M:%S") + "\n")
        for line in sys.stdin:
            if "stop" == line.rstrip():
                break
            file.write(line)
            print(f"Enter content line: {line}")

        print("Enter content line: stop")

if command == "-d":
    os.makedirs(directory_name, exist_ok=True)
