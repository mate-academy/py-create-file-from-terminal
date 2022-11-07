from sys import argv
from os import makedirs
import os.path
from datetime import datetime


def create_file():
    if '-d' in argv and '-f' not in argv:
        makedirs(f"{argv[3]}")
        makedirs(f"{argv[3]}/{argv[4]}")

    if '-f' in argv and '-d' not in argv:
        if os.path.exists(f"{argv[3]}"):
            f = open(f"{argv[3]}", "a")
            f.write(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

            n = 1
            content = f"Another line{n}{input('')}"
            string = f"{content}\n"
            while content != "stop":
                content = input("Enter content line:")
                string += f"Another line{n+1} {content}\n"
                n = n + 1
            f.write(string)

        if os.path.exists(f"{argv[3]}") is False:
            f = open(f"{argv[3]}", "a")
            f.write(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
            n = 1
            content = f"Line{n}{input('')}"
            string = f"{content}\n"
            while content != "stop":
                content = input("Enter content line:")
                string += f"Line{n + 1} {content}\n"
                n = n + 1
            f.write(string)

    if '-f' in argv and '-d' in argv:
        makedirs(f"{argv[3]}")
        makedirs(f"{argv[3]}/{argv[4]}")

        f = open(f"{argv[3]}/{argv[4]}/{argv[6]}", "a")
        f.write(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        n = 1
        content = f"Line{n}{input('')}"
        string = f"{content}\n"
        while content != "stop":
            content = input("Enter content line:")
            string += f"Line{n + 1} {content}\n"
            n = n + 1
        f.write(string)
