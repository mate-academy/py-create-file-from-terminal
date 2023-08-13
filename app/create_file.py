import datetime
import os
import sys


def create_file() -> None:
    args = sys.argv[1:]
    if "-f" not in args and "-d" not in args:
        print("Please use either -d or -f flag.")
    else:
        directory_path = ""
        if "-d" in args:
            status = False
            for elem in args:
                if elem == "-d":
                    status = True
                    continue
                if elem == "-f":
                    status = False
                if status:
                    directory_path += elem + "/"
            print(directory_path)
            os.makedirs(directory_path, exist_ok=True)

        if "-f" in args:
            num_index = 0
            content = (
                datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n"
            )
            while True:
                num_index += 1
                answer = input("Enter content line: ")
                if answer == "stop":
                    break
                content += str(num_index) + " " + answer + "\n"
            content += "\n"

            if "-d" in args:
                file_path = directory_path + args[args.index("-f") + 1]
            else:
                file_path = args[args.index("-f") + 1]
            if os.path.exists(file_path):
                with open(file_path, "a") as file:
                    file.write(content)
            else:
                with open(file_path, "w") as file:
                    file.write(content)


if __name__ == "__main__":
    create_file()
