from datetime import datetime
import sys
import os


args = sys.argv
# print(args)
# print(args.index("-d") + 1)

if "-d" in args:

    for i in range(args.index("-d") + 1, len(args), 1):
        print(i)

        element = args[i]
        if element == "-f":
            break

        os.mkdir(f"{element}")
        os.chdir(f"{element}")

if "-f" in args:

    with open(f"{args[args.index("-f") + 1]}", "a") as file:
        formatted_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"{formatted_date}\n")
        num = 1
        while True:
            line = input("Enter content line:")
            if line == "stop":
                break

            file.write(f"{num} {line}\n")
            num += 1
