import datetime
import sys
import os


def create_file() -> None:
    current_time = datetime.datetime.now()
    if "-d" in sys.argv:
        index_d = sys.argv.index("-d")
        directory_path = sys.argv[index_d + 1:]
        directory_path = os.path.join(*directory_path)
        os.makedirs(directory_path, exist_ok=True)

    if "-f" in sys.argv:
        index_f = sys.argv.index("-f")
        output_filename = sys.argv[index_f + 1]

        if output_filename:
            with open(output_filename, "a") as file:
                file.write(f"{current_time.strftime('%Y-%m-%d %H:%M:%S')}\n")
                count_lines = 1

                while True:
                    user_typing = input("Enter content line:")
                    if user_typing == "stop":
                        file.write("\n")
                        break
                    file.write(f"{count_lines} {user_typing}" + "\n")
                    count_lines += 1


create_file()
