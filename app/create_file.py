import os
from datetime import datetime


def create_file() -> None:
    path = input()
    words = path.split()
    flag = words[0]
    if flag == "-d":
        create_directory_from_input(words)
    elif flag == "-f":
        create_file_from_input(words[1])


def create_directory_from_input(words: list[str]) -> None:
    path = ""
    for i in range(1, len(words)):
        if words[i] == "stop":
            return
        if words[i] == "-f":
            create_file_from_input(words[i + 1], path)
            return
        path = os.path.join(path, words[i])
    os.makedirs(path, exist_ok=True)


def create_file_from_input(word: str, path: str = "") -> str:
    full_path = os.path.join(path, word)
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    open(full_path, "a").close()
    return full_path


def add_content(content: list[str]) -> None:
    with open("content.txt", "a", encoding="utf-8") as file:
        file.write(str(datetime.now().strftime("%Y-%m-%d %H:%M:%S")) + "\n")
        file.write("\n".join(content) + "\n")
