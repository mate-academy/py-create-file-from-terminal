# write your code here
import os
import sys
import datetime


# handle -d fall
def scan_args() -> list:

    print(sys.argv)
    d_pos = 0
    f_pos = 0
    d_args = []
    f_args = []
    for index, item in enumerate(sys.argv):
        if item == "-d":
            d_pos = index
        if item == "-f":
            f_pos = index
    if d_pos != 0 and f_pos != 0:
        d_args = sys.argv[d_pos + 1 : f_pos]
        f_args = sys.argv[f_pos + 1 :]

    if d_pos != 0 and f_pos == 0:
        d_args = sys.argv[d_pos + 1 :]
        f_args = []

    if d_pos == 0 and f_pos != 0:
        d_args = []
        f_args = sys.argv[f_pos + 1 :]

    if d_pos == 0 and f_pos == 0:
        d_args = []
        f_args = []

    return d_args, f_args


def create_folder(args: list) -> str:
    if len(args) == 0:
        return os.getcwd()
    else:
        new_folder = os.path.join(os.getcwd(), *args)
        if not os.path.exists(new_folder):
            os.makedirs(new_folder)
            return new_folder
        else:
            print(f"Folder {new_folder} already exists.")
            return new_folder


def create_file(args: list, folder: str) -> None:

    if len(args) == 0:
        print("No file name provided.")
        return
    else:
        file_path = os.path.join(folder, args[0])
        with open(file_path, "a") as file:
            time = datetime.datetime.now()
            note_time = time.strftime("%Y-%m-%d %H:%M:%S")
            file.write(f"{note_time}\n")
            while True:
                input_text = input("Enter content line: ")
                if input_text == "stop":
                    break
                file.write(f"{input_text}\n")


def main() -> None:
    d_args, f_args = scan_args()
    folder = create_folder(d_args)
    create_file(f_args, folder)


if __name__ == "__main__":
    main()
