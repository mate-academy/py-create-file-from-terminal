import sys
import datetime
import os


def create_directories(directory_names: list) -> None:
    directory_path = os.path.join(*directory_names)
    os.makedirs(directory_path, exist_ok=True)


def create_file(file_name: str) -> None:
    with open(file_name, "a") as f:
        f.write(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")
        while True:
            text = input("Enter content line: ") + "\n"
            if text == "stop\n":
                break
            f.write(text)


def main() -> None:
    if "-f" in sys.argv:
        key_index_f = sys.argv.index("-f") + 1
        file_path = sys.argv[key_index_f]

        if "-d" in sys.argv:
            key_index_d = sys.argv.index("-d") + 1
            create_directories(sys.argv[key_index_d:key_index_f - 1])
            current_way = (sys.argv[key_index_d:key_index_f - 1]
                           + sys.argv[key_index_f:])
            create_file(os.path.join(*current_way))

        else:
            create_file(file_path)

    elif "-d" in sys.argv:
        key_index = sys.argv.index("-d") + 1
        create_directories(sys.argv[key_index:])


if __name__ == "__main__":
    main()
