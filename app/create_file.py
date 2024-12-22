import sys
import os
import datetime as dt


def filling_content(file_name: str) -> None:
    try:
        with open(file_name, "a") as f:
            timestamp = dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            f.write(f"\n{timestamp}\n")

            number_line = 0
            while True:

                text_input = input("Enter content line: ")
                if text_input == "stop":
                    break
                f.write(f"{number_line} {text_input}")
                number_line += 1
    except Exception as e:
        print(f"Error writing to file: {e}")


def create_file() -> None:

    args = sys.argv[1:]

    if not args:
        print("No arguments provided.")
        return
    try:
        if "-d" in args:
            d_index = args.index("-d") + 1
            dir_path = os.path.join(*args[d_index:])
            os.makedirs(dir_path, exist_ok=True)
            print(f"Directory created: {dir_path}")

            if "-f" in dir_path:
                f_index = args.index("-f") + 1
                file_name = args[f_index]
                file_path = os.path.join(dir_path, file_name)
                filling_content(file_path)

        elif "-f" in args:
            f_index = args.index("-f") + 1
            file_name = args[f_index]
            filling_content(file_name)
            return
    except Exception as e:
        print(f"Error: {e}")
