import sys
import os
import datetime

path = os.getcwd()
path_list = []
if "-d" in sys.argv and "-f" not in sys.argv:
    for arg in sys.argv[sys.argv.index("-d") + 1:len(sys.argv)]:
        path_list.append(arg)
elif "-d" in sys.argv and "-f" in sys.argv:
    for arg in sys.argv[sys.argv.index("-d") + 1:sys.argv.index("-f")]:
        path_list.append(arg)
makedir_path = os.path.join(path, path_list)
os.makedirs(makedir_path)

if "-f" in sys.argv:
    now = datetime.datetime.now()
    input_text = now.strftime("%Y-%m-%d %H:%M:%S\n")
    while True:
        line = input()
        if line == "stop":
            with open(f'{makedir_path}\\{sys.argv[sys.argv.index("-f") + 1]}', "a+") as target_file:
                target_file.write(f"{input_text}\n")
                break
        input_text += f"{line}\n"
