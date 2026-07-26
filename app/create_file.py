from datetime import datetime
import os
import sys


directory_or_with_file = sys.argv
directory_name = ""
file_name = ""
file_mod = "a"
for word in directory_or_with_file:
    if (
        not word.count("create_file.py")
        and word != "-d"
        and word != "-f"
        and not word.count(".")
    ):
        directory_name = os.path.join(
            directory_name,
            word
        )

    if (
        directory_or_with_file.count("-f")
        and word.count(".")
        and not word.count("create_file.py")
    ):
        file_name = word
        file_mod = "w"

if directory_or_with_file.count("-d"):
    os.makedirs(
        directory_name,
        exist_ok=True
    )

with open(
    os.path.join(directory_name, file_name),
    file_mod
) as file:
    num = 1
    file.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S\n"))
    while True:
        line_text = input(
            "Enter content line: "
        )
        if line_text == "stop":
            break
        file.write(str(num) + " " + line_text + "\n")
        num += 1
