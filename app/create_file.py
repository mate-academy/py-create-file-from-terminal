import sys
import os
import datetime


def check_for_directories():
    directory = ""
    if "-d" in sys.argv:
        directory = sys.argv[sys.argv.index("-d") + 1:]
        if "-f" in directory:
            directory = directory[:directory.index("-f")]
        directory = os.path.join(*directory) + "\\"

        if os.path.dirname(directory) != "":
            os.makedirs(os.path.dirname(directory), exist_ok=True)
    return directory


def check_files(directory):
    if "-f" in sys.argv:
        file_name = sys.argv[sys.argv.index("-f") + 1:]
        if "-d" in directory:
            file_name = file_name[:directory.index("-f")]
        file_name = f"{directory}" + "".join(file_name)

        with open(file_name, "a") as file:
            file.write(str(datetime.datetime.now().replace(microsecond=0)) + "\n")
            line_index = 1
            while True:
                content = input("Enter content line: ")
                if content == "stop":
                    file.write("\n")
                    break
                file.writelines(f"{line_index} {content}\n")
                line_index += 1


def main():
    directory = check_for_directories()
    check_files(directory)


if __name__ == "__main__":
    main()
