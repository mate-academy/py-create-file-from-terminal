import os
import sys
from datetime import datetime as dt

if __name__ == '__main__':
    parse_dir = False
    parse_filename = False
    dirs_parts = []
    filename = ''
    for arg in sys.argv:
        if arg == "-d":
            parse_dir = True
            parse_filename = False
            continue
        elif arg == "-f":
            parse_dir = False
            parse_filename = True
            continue

        if parse_dir:
            dirs_parts.append(arg)
        elif parse_filename:
            filename = arg

    dir_path = ''
    if dirs_parts:
        dir_path = os.path.join(*dirs_parts)
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)

    if filename:
        file_content = str(dt.now().strftime("%Y-%m-%d, %H:%M:%S")) + "\n"
        while (line := input("Enter content line: ")) != "s":
            file_content += line + "\n"
        file_content = file_content.rstrip()
        with open(os.path.join(dir_path, filename), 'a') as users_file:
            users_file.seek(0, os.SEEK_END)
            file_is_empty = not bool(users_file.tell())
            users_file.seek(0)
            if not file_is_empty:
                users_file.write("\n")
            users_file.write(file_content)
