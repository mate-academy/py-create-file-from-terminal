import datetime
import sys
import os


def main() -> None:
    directory_path = []
    f_argument = False
    d_argument = False
    for argument in sys.argv:
        if argument == "-d":
            d_argument = True
            f_argument = False

        if argument == "-f":
            f_argument = True
            d_argument = False

        if d_argument and argument != "-d":
            directory_path.append(argument)
            if not os.path.isdir(os.path.join(*directory_path)):
                os.mkdir(os.path.join(*directory_path))

        if f_argument and argument != "-f":
            name_of_file = argument
            text_for_file = ""
            string_count = 1
            while True:
                next_string = input("Enter content line: ")
                if next_string == "stop":
                    break
                text_for_file += f"{string_count} {next_string}\n"
                string_count += 1

            text_for_file = \
                (f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
                 f"\n{text_for_file}")

            if os.path.exists(os.path.join(*directory_path, name_of_file)):
                text_for_file = f"\n{text_for_file}"
                with open(
                        os.path.join(*directory_path, name_of_file), "a"
                ) as file:
                    file.write(text_for_file)
            else:
                with open(
                        os.path.join(*directory_path, name_of_file
                                     ), "w") as file:
                    file.write(text_for_file)


if __name__ == "__main__":
    main()
