import sys
from datetime import datetime
from os import makedirs

print(sys.argv)


def run(data):
    path = None
    if "-d" in data:
        index_d_flag = data.index("-d")
        try:
            index_f_flag = data.index("-f")
        except ValueError:
            index_f_flag = None

        path = '/'.join(data[index_d_flag + 1:index_f_flag])
        makedirs(path)

    if "-f" in data:
        index_f_flag = data.index("-f")

        if path is None:
            file_name = data[index_f_flag + 1]
        else:
            file_name = path + "/" + data[index_f_flag + 1]

        with open(f"{file_name}", "a") as file:
            file.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S\n"))
            line = 1

            while True:
                inp = input("Enter content line: ")
                file.write(f"{line} {inp} \n")
                line += 1

                if inp == "stop":
                    file.write("\n")
                    break


if __name__ == '__main__':
    run(sys.argv)
