import os
import sys
from datetime import datetime


class CreateFile:
    def __init__(self) -> None:
        self.args = sys.argv
        self.destination = []
        self.file_name = None
        self._args()

    def _args(self) -> None:
        arguments = self.args[1:]
        mode = None

        for arg in arguments:
            if arg == "-d":
                mode = "dir"
                continue
            elif arg == "-f":
                mode = "file"
                continue

            if mode == "dir":
                self.destination.append(arg)
            elif mode == "file":
                if not self.file_name:
                    self.file_name = arg

    def create_dir(self) -> None:
        path_dir = os.path.join(*self.destination)
        os.makedirs(path_dir, exist_ok=True)

    def create_file(self) -> None:
        path_to_file = os.path.join(*self.destination, self.file_name)

        with open(path_to_file, "a") as file:
            if os.path.getsize(path_to_file) > 0:
                file.write("\n")

            file.write(
                datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n"
            )

            line_counter = 1
            while True:
                content = input("Enter content line: ")

                if content.lower() == "stop":
                    break

                file.write(f"{line_counter} {content}\n")
                line_counter += 1

    def run(self) -> None:
        if self.destination:
            self.create_dir()

        if self.file_name:
            self.create_file()


if __name__ == "__main__":
    creator = CreateFile()
    creator.run()
