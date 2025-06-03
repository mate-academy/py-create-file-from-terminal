import os
from datetime import datetime
from typing import List, Union


def create_directory(path_parts: Union[List[str], str]) -> None:
    if isinstance(path_parts, str):
        path_parts = [path_parts]
    path = os.path.join(*path_parts)
    os.makedirs(path, exist_ok=True)
    print(f"Directory created: {path}")


def create_file(file_path: str) -> None:
    content_lines = []
    print("Enter content line (type 'stop' to finish):")

    while True:
        line = input("Enter content line: ")
        if line.lower() == "stop":
            break
        content_lines.append(line)

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    numbered_content = (
        "\n".join(f"{i + 1}{line}" for i, line in enumerate(content_lines))
    )

    if os.path.exists(file_path):
        with open(file_path, "a") as f:
            f.write(f"{timestamp}\n{numbered_content}\n")
    else:
        with open(file_path, "w") as f:
            f.write(f"{timestamp}\n{numbered_content}\n")

    print(f"File created/updated: {file_path}")
