import sys
import os
import datetime


current_data = datetime.datetime.now()

for item in sys.argv:
    if "-d" == item:
        for elem in sys.argv[sys.argv.index("-d") + 1:]:
            if elem == "-f":
                break
            current_dir = os.getcwd()
            os.mkdir(elem)
            current_dir = os.path.join(current_dir, elem)
            os.chdir(current_dir)


    if "-f" == item:
        current_file = sys.argv[sys.argv.index("-f") + 1]
        if os.path.exists(current_file):
            with open(current_file, "a") as additional_text:
                additional_text.write(current_data.strftime("\n%I:%M%p %d/%B/%Y\n"))
                count = 1
                while True:
                    user = input("Enter content line: ")
                    if user == "stop":
                        break
                    additional_text.write(f"{count} Another {user}\n")
                    count += 1
            break

        with open(current_file, "a") as f:
            f.write(current_data.strftime("%I:%M%p %d/%B/%Y\n"))
            count = 1
            while True:
                user = input("Enter content line: ")
                if user == "stop":
                    break
                f.write(f"{count} {user}\n")
                count += 1
