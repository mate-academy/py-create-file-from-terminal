import sys
import os
import datetime


def parse_input(arguments: str) -> dict:
    actions = {"file_name": "", "directory_path": []}
    paths_with_flags = arguments.split("-")
    for single_command in paths_with_flags:
        if single_command[0] == "f":
            actions["file_name"] = single_command[2:]
            continue
        actions["directory_path"].append(single_command[2:])
    return actions


def create_directory(directory_path: dict) -> str:
    destination_directory = os.path.join(os.getcwd(), *directory_path)
    os.makedirs(destination_directory)
    return destination_directory


def add_content_to_file(directory: str, file_name: str) -> bool:
    if not os.path.exists(directory):
        return False
    content = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n"
    with open(os.path.join(directory, str(file_name)), "a") as file:
        file.write(content)
        counter = 1
        content = input(f"Enter content line: Line{counter}")
        while content != "stop":
            file.write(f"line{counter} " + content + "\n")
            content = input(f"Enter content line: Line{counter}")
            counter += 1


if __name__ == "__main__":
    input_string = " ".join(sys.argv[1:])
    file_name, directory_path = parse_input(input_string).values()
    print(directory_path)
    directory_path = create_directory(directory_path)
    add_content_to_file(directory_path, file_name)

# print(type(sys.argv))
# print(sys.argv)
# print(type(" ".join(sys.argv)))
# print(" ".join(sys.argv))
