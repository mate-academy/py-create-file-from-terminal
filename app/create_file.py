import sys
import os
import datetime


file_name = None
args = sys.argv[1:]

if "-d" in args:
    d_index = args.index("-d")
    directory_parts = []
    for i in range(d_index + 1, len(args)):
        if args[i] == "-f":
            break
        directory_parts.append(args[i])

    if directory_parts:
        directory_path = os.path.join(os.getcwd(), *directory_parts)
        os.makedirs(directory_path, exist_ok=True)
else:
    print('ERROR: expected path. Use: -d \"path\"')
    sys.exit(1)

if "-f" in args:
    f_index = args.index("-f")
    file_name = args[f_index + 1]
else:
    print("ERROR: expected -f file_name.txt")
    sys.exit(1)

file_path = os.path.join(
    directory_path if directory_path else os.getcwd(), file_name
)

with open(file_path, "a") as new_file:
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    new_file.write(f"{current_time}\n")
    number_of_string = 0
    while True:
        user_input = input("Enter new line of content: ")
        if user_input.lower() == "stop":
            new_file.write("\n")
            break
        number_of_string += 1
        new_file.write(f"{number_of_string} {user_input}\n")
