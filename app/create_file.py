import os
import sys
from datetime import datetime


class CreateFile:
    def __init__(self) -> None:
        self.file_name = ""
        self.file_content = ""
        self.path_list = []

        args = sys.argv
        current_flag = None
        for arg in args[1:]:
            if arg == "-d" or arg == "-f":
                current_flag = arg
            elif current_flag == "-d":
                self.path_list.append(arg)
            elif current_flag == "-f":
                self.file_name = arg

    def create_directory(self) -> str:
        if len(self.path_list) == 0:
            return ""

        path = os.path.join(*self.path_list)

        try:
            os.makedirs(path, exist_ok=True)
        except OSError:
            raise OSError

        return path

    def fill_file(self, path: str = "") -> None:
        if self.file_name == "":
            return

        with open(os.path.join(path, self.file_name),
                  "a", encoding="utf-8") as file:
            if file.tell() != 0:
                file.write("\n")

            file.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")

            index = 1
            while True:
                index += 1
                line_content = input("Enter content line: ")
                if line_content == "stop":
                    break

                file.write(str(index) + " " + line_content + "\n")

    def process_all(self) -> None:
        path = self.create_directory()
        self.fill_file(path)


create_file = CreateFile()
create_file.process_all()
