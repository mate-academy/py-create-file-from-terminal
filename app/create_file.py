import sys
import os
import datetime


def app() -> None:
    term = sys.argv
    if term[1] == "-f" and len(term) < 5:
        if os.path.exists(term[2]) is False:
            with open(term[2], "w") as file:
                current_date = datetime.datetime.now()
                in_put = input("Enter content line: ")
                file.write(current_date.strftime("%d/%m/%Y %H:%M:%S") + "\n")
                while in_put != "stop":
                    file.write(in_put + "\n")
                    in_put = input("Enter content line: ")
        elif os.path.exists(term[2]) is True and len(term) < 5:
            with open(term[2], "a") as file:
                current_date = datetime.datetime.now()
                in_put = input("Enter content line: ")
                file.write("\n" + current_date.strftime(
                    "%d/%m/%Y %H:%M:%S"
                ) + "\n")
                while in_put != "stop":
                    file.write(in_put + "\n")
                    in_put = input("Enter content line: ")

    if term[1] == "-d" and term[4] != "-f":
        subdirectory_path = os.path.join(term[2], term[3])
        os.makedirs(subdirectory_path)

    if term[1] == "-d" and term[4] == "-f":
        subdirectory_path = os.path.join(term[2], term[3])
        os.makedirs(subdirectory_path)
        file_path = os.path.join(subdirectory_path, term[0])
        with open(file_path, "w") as file:
            current_date = datetime.datetime.now()
            in_put = input("Enter content line: ")
            file.write(current_date.strftime("%d/%m/%Y %H:%M:%S") + "\n")
            while in_put != "stop":
                file.write(in_put + "\n")
                in_put = input("Enter content line: ")


app()
