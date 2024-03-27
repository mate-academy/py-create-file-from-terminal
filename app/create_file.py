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
        os.makedirs(str(directory_path), exist_ok=True)
        filepath = os.path.join(str(directory_path), str(file_name))
    else:
        filepath = file_name

    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    if file_content:
        mode = "a" if os.path.exists(filepath) else "w"
        with open(filepath, mode) as f:
            f.write(timestamp + "\n")
            for i, content_line in enumerate(file_content, start=1):
                f.write(f"{i} {content_line}\n")
                if content_line.strip().lower() == "stop":
                    break
    else:
        with open(filepath, "w") as f:
            f.write(timestamp + "\n")


if __name__ == "__main__":
    flags = sys.argv[1:]

    directory = None
    filename = None
    content = []

    if "-d" in flags and "-f" in flags:
        start_directory_index = flags.index("-d")
        end_directory_index = flags.index("-f")
        directory = flags[start_directory_index + 1:end_directory_index]
        filename = flags[end_directory_index + 1:]
    elif "-f" in flags:
        filename_index = flags.index("-f")
        filename = flags[filename_index + 1]

    if filename:
        while True:
            line = input("Enter content line: ")
            content.append(line)
            if line == "stop":
                break

    create_file(
        parts_directory=directory,
        file_name=filename,
        file_content=content
    )
