import sys
import os
from datetime import datetime

def create_file():
    args = sys.argv[1:]
    directory_parts, file_name = [], None

    if '-d' in args:
        d_index = args.index('-d') + 1
        while d_index < len(args) and not args[d_index].startswith('-'):
            directory_parts.append(args[d_index])
            d_index += 1
    if '-f' in args:
        f_index = args.index('-f') + 1
        if f_index < len(args) and not args[f_index].startswith('-'):
            file_name = args[f_index]

    base_path = os.path.join(os.getcwd(), *directory_parts) if directory_parts else os.getcwd()
    if directory_parts:
        os.makedirs(base_path, exist_ok=True)

    if not file_name:
        print(f"Directory created at: {base_path}")
        return

    content_lines = []
    line_num = 1
    while True:
        line = input("Enter content line: ")
        if line.strip().lower() == "stop":
            break
        content_lines.append(f"{line_num} {line}")
        line_num += 1

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    content_block = [timestamp] + content_lines

    file_path = os.path.join(base_path, file_name)
    file_exists = os.path.exists(file_path)
    with open(file_path, 'a', encoding='utf-8') as f:
        if file_exists:
            f.write('\n\n')
        f.write('\n'.join(content_block) + '\n')

    print(f"File saved at: {file_path}")


if __name__ == "__main__":
    create_file()
