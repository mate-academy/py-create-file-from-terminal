from datetime import datetime
import sys
import os


def main() -> None:
    user_text = sys.argv[1:]

    if not user_text:
        return

    path_part = []
    file_name = None
    index = 0

    while index < len(user_text):
        if user_text[index] == "-d":
            index += 1
            while (index < len(user_text)
                   and not user_text[index].startswith("-")):
                path_part.append(user_text[index])
                index += 1
        elif user_text[index] == "-f":
            index += 1
            if index < len(user_text):
                file_name = user_text[index]
                index += 1
        else:
            index += 1

    # Build full path
    dir_path = os.path.join(*path_part) if path_part else ""
    if dir_path:
        if os.path.isdir(dir_path):
            print(f"Directory already exists: {dir_path}")
        else:
            os.makedirs(dir_path, exist_ok=True)
            print(f"Directory created: {dir_path}")
    if file_name:
        file_path = os.path.join(dir_path, file_name)\
            if dir_path else file_name

        with open(file_path, "a", encoding="utf-8") as f:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            if os.path.exists(file_path) and os.path.getsize(file_path) > 0:
                f.write(f"\n{timestamp}\n")
            else:
                f.write(f"{timestamp}\n")

            line_num = 1
            while True:
                line = input("Enter content line: ")
                if line == "stop":
                    break
                f.write(f"{line_num} {line}\n")
                line_num += 1

        print(f"File saved at: {file_path}")

    elif path_part:  # only -d flag used
        print(f"Done. Directory path is ready: {dir_path}")
    else:
        print("No -d or -f flag provided.")


if __name__ == "__main__":
    main()
