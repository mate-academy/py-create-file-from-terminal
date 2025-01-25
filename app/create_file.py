import os
import sys
from datetime import datetime

now = datetime.now()

formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")

operand = sys.argv[1:]

directories = []

if operand[0] == "-f":
    with open(operand[1], "a", encoding="utf-8") as source_file:
        source_file.write(formatted_date + "\n")
        index = 1
        while True:
            message = input("Enter content line: ")

            if message.lower() == "stop":
                break

            source_file.write(f"{index} {message}\n")
            index += 1

        source_file.write("\n")

if operand[0] == "-d":
    for i in range(1, len(operand)):
        if operand[i] == "-f":
            break
        directories.append(operand[i])

    formatted_path = os.path.join(*directories)
    os.makedirs(formatted_path, exist_ok=True)

    if "-f" in operand:
        file_index = operand.index("-f") + 1

        if file_index < len(operand):
            file_name = operand[file_index]
            file_path = os.path.join(formatted_path, file_name)

            with open(file_path, "a", encoding="utf-8") as source_file:
                source_file.write(formatted_date + "\n")
                index = 1
                while True:
                    message = input("Enter content line: ")

                    if message.lower() == "stop":
                        break

                    source_file.write(f"{index} {message}\n")
                    index += 1

                source_file.write("\n")
