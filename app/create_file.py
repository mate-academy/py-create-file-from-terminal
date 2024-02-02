import os
import sys
import datetime


def create_directory(directory_name: str) -> None:
    os.makedirs(directory_name, exist_ok=True)


def create_file(file_name: str) -> None:

    with open(file_name, "a") as file:
        if os.stat(file_name).st_size > 0:
            file.write("\n")
        create_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"{create_time}\n")

        lines = 1
        while True:
            new_line = input("Enter content line: ")
            if new_line == "stop":
                break
            file.write(f"Line{lines}: {new_line}\n")
            lines += 1


def main() -> None:
    if "-d" in sys.argv and "-f" in sys.argv:
        d_index = sys.argv.index("-d")
        f_index = sys.argv.index("-f")

        if f_index < d_index:
            raise Exception("Error: Please use -d before -f.")

    if "-d" in sys.argv:
        base_directory = (
            sys.argv[sys.argv.index("-d") + 1:sys.argv.index("-f")]
            if "-f" in sys.argv
            else sys.argv[sys.argv.index("-d"):])
        path = os.path.join(*base_directory)
        create_directory(path)

    if "-f" in sys.argv:
        file_name = sys.argv[-1]
        os.chdir(path)
        create_file(file_name)

if __name__ == "__main__":
    main()
