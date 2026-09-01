import os
import sys
import datetime


console_text = sys.argv
d_index = None
f_index = None
inner_text = None

if "-f" in console_text:
    f_index = console_text.index("-f")
if "-d" in console_text:
    d_index = console_text.index("-d")

if d_index is not None and d_index + 1 <= len(console_text):
    if f_index is None:
        path = os.path.join(os.getcwd(), *console_text[d_index + 1:])
    if f_index is not None and f_index > d_index:
        path = os.path.join(os.getcwd(), *console_text[d_index + 1:f_index])
    if f_index is not None and f_index < d_index:
        path = os.path.join(os.getcwd(), *console_text[d_index + 1:])
    os.makedirs(path, exist_ok=True)
if f_index is not None and f_index + 1 <= len(console_text):
    if d_index is None:
        file_path = console_text[f_index + 1]
    if d_index is not None:
        file_path = os.path.join(path, console_text[f_index + 1])

    with open(file_path, "a") as f:
        if os.path.exists(file_path) and os.path.getsize(file_path) > 0:
            f.write("\n")
        date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S\n")
        f.write(date)
        counter = 0
        while inner_text != "stop":
            counter += 1
            inner_text = input("Enter content line: ")
            if inner_text != "stop":
                f.write(f"{counter} {inner_text}\n")
