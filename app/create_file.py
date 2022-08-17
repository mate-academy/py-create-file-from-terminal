import os
import argparse
import datetime


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", dest="dir_name", nargs="+")
    parser.add_argument("-f", dest="file_name", nargs=1)
    args = parser.parse_args()

    file_path = os.path.curdir

    if args.dir_name:
        file_path = f"{os.sep}".join(args.dir_name)
        os.makedirs(name=file_path, mode=0o777, exist_ok=True)

    if args.file_name:
        file_name = os.path.join(file_path, args.file_name[0])
        line_number = 1

        with open(file=file_name, mode="a") as f:
            line_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            f.write(f"{line_date}\n")

            while True:
                line_content = input("Enter content line: ")

                if line_content == "stop":
                    f.write("\n")
                    break

                f.write(f"{line_number} {line_content}\n")
                line_number += 1
