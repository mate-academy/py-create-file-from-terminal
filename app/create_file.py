import os
import sys
import datetime


def create_file(lines: str) -> None:
    user_text = input(f"Enter content line: {lines}")

    direct_index = sys.argv.index("-d")
    file_index = sys.argv.index("-f")

    if "-d" in sys.argv :
        list_dir = []
        for i in range(direct_index, file_index):
            if sys.argv[i] == "stop":
                break
            else:
                if sys.argv[i] != "-f":
                    list_dir.append(sys.argv[i])
                full_path = os.path.join(*list_dir)
                os.makedirs(full_path, exist_ok=True)

    if "-f" in sys.argv:
        for i in sys.argv:
            if i == "-f":
                name_of_file = sys.argv[sys.argv.index(i) + 1]
                if user_text == "stop":
                    break
                else:
                    count = 1
                    with open(name_of_file, "a") as name_file:
                        for text in user_text:
                            name_file.write(
                                datetime.datetime.now().strftime
                                ("%Y-%m-%d %H:%M:%S"))
                            str_count = str(count) + " "
                            name_file.write(str_count)
                            name_file.write(text)
                            name_file.write("\n")
                            count += 1
