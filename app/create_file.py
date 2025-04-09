import sys
import os
import datetime


def main():
    dir_flag = '-d' in sys.argv
    file_flag = '-f' in sys.argv

    directory_path = ""
    file_name = ""

    if dir_flag:
        dir_index = sys.argv.index('-d')
        directory_parts = sys.argv[dir_index + 1:]

        if file_flag:
            file_index = sys.argv.index('-f')
            directory_parts = directory_parts[:file_index - dir_index - 1]

        directory_path = os.path.join(*directory_parts)

        os.makedirs(directory_path, exist_ok=True)

    if file_flag:
        file_index = sys.argv.index('-f')
        file_name = sys.argv[file_index + 1]

        if directory_path:
            file_path = os.path.join(directory_path, file_name)
        else:
            file_path = file_name

        content_lines = []
        print("Wprowadź linię zawartości: ")
        while True:
            line = input()
            if line.lower() == "stop":
                break
            content_lines.append(line)

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(file_path, 'a') as file:
            file.write(f"{timestamp}\n")
            for i, line in enumerate(content_lines, start=1):
                file.write(f"{i} {line}\n")

if __name__ == "__main__":
    main()