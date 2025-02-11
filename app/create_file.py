import sys
import os
import datetime


current_data = datetime.datetime.now()

for item in sys.argv:
    current_dir = os.getcwd()
    if "-d" == item and "-d" != sys.argv[-1]:
        for elem in sys.argv[sys.argv.index("-d") + 1:]:
            if elem.startswith("-"):
                break
            current_dir = os.path.join(current_dir, elem)
            os.makedirs(current_dir, exist_ok=True)
            os.chdir(current_dir)

    if "-f" == item and "-f" != sys.argv[-1]:
        current_file = sys.argv[sys.argv.index("-f") + 1]
        if os.path.exists(current_file):
            with open(current_file, "a") as additional_text:
                additional_text.write(current_data.strftime(
                    "\n%Y-%m-%d %H:%M:%S\n"))
                count = 1
                while True:
                    user = input("Enter content line: ")
                    if user == "stop":
                        break
                    additional_text.write(f"{count} Another {user}\n")
                    count += 1
            break
        else:
            with open(current_file, "a") as f:
                f.write(current_data.strftime("%Y-%m-%d %H:%M:%S\n"))
                count = 1
                while True:
                    user = input("Enter content line: ")
                    if user == "stop":
                        break
                    f.write(f"{count} {user}\n")
                    count += 1
