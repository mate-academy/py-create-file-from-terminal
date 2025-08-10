import sys
import os
import datetime


def create_file(
        parts_directory: list[str],
        file_name: str,
        file_content: list[str]
) -> None:
    if parts_directory:
        directory_path = os.path.join(*parts_directory)
        os.makedirs(directory_path, exist_ok=True)
        if file_name:
            filepath = os.path.join(directory_path, file_name)
    else:
        filepath = file_name

    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if file_name:
        if file_content:
            file_exists = os.path.exists(filepath)
            with open(filepath, "a") as f:
                if file_exists:
                    f.write("\n")
                f.write(timestamp + "\n")
                for i, content_line in enumerate(file_content, start=1):
                    f.write(f"{i} {content_line}\n")

        else:
            with open(filepath, "w") as f:
                f.write(timestamp + "\n")


def main() -> None:
    argv = sys.argv[1:]

    directory = None
    filename = None
    content = []

    if "-d" in argv and "-f" in argv:
        d_index = argv.index("-d") + 1
        f_index = argv.index("-f") + 1
        if d_index < f_index:
            directory = argv[d_index: f_index - 1]
            filename = argv[f_index]
        else:
            directory = argv[d_index:]
            filename = argv[f_index]
    elif "-d" in argv:
        d_index = argv.index("-d") + 1
        directory = argv[d_index:]
    elif "-f" in argv:
        filename_index = argv.index("-f") + 1
        filename = argv[filename_index]

    # if not filename:
    #     print("Please provide a filename.")
    #     return
    if filename:
        while True:
            line = input("Enter content line: ")
            if line == "stop":
                break
            content.append(line)

    create_file(
        parts_directory=directory or [],
        file_name=filename,
        file_content=content
    )


if __name__ == "__main__":
    main()
