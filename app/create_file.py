import os
import sys
import datetime


args = sys.argv
file_name = None
directory_path_parts = []

d_index = args.index("-d")
f_index = args.index("-f")
directory = args[d_index+1:f_index]
file_name = args[f_index+1]

directory_path = os.path.join(*directory)
os.makedirs(directory_path, exist_ok=True)
full_filename = os.path.join(directory_path, file_name)

user_text =[]
while True:
    text = input()
    if text == "stop":
        break
    user_text.append(text)

timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
lines_to_write = [timestamp]
for index, item in enumerate(user_text, start=1):
    formatted_line = f"{index} {item}"
    lines_to_write.append(formatted_line)
with open(full_filename, "a", encoding="utf-8") as f:
    f.write("\n".join(lines_to_write))
