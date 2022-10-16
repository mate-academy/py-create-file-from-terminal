import os
from sys import argv
from datetime import datetime


class CreateFile:
    path: str = "app"
    file_data: list[str] = []

    def create_file(self) -> None:
        self.file_data = argv
        if self.file_data[0] == "app/create_file.py":
            try:
                self.create_dirs_path()
                self.create_file_path()
            except (IndexError, ValueError):
                print("You don't Enter the name of file!")
                exit()
            with open(self.path, "a") as f:
                f.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
                while True:
                    input_data: str = input("Enter content line: ")
                    if input_data == "stop":
                        f.write("\n")
                        break
                    f.write(f"{input_data}\n")

    def create_dirs_path(self) -> None:
        if self.file_data[1] == "-d":
            no_index: int = 2
            while self.file_data[no_index] != "-f":
                self.path = os.path.join(self.path, self.file_data[no_index])
                no_index += 1
            os.makedirs(self.path, exist_ok=True)

    def create_file_path(self) -> None:
        if self.file_data[-2] == "-f":
            self.path = os.path.join(self.path, self.file_data[-1])
        else:
            raise ValueError


CreateFile().create_file()
