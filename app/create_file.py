import sys
import os
import datetime


class Command:
    def __init__(self, commands: list) -> None:
        self.commands = commands
        self.index_d = (self.commands.index("-d") + 1
                        if "-d" in self.commands
                        else 0)
        self.index_f = (self.commands.index("-f")
                        if "-f" in self.commands
                        else len(self.commands))

    def create_file(self) -> None:

        file_to_open = self.commands[-1]

        if "-d" in self.commands:
            path_to_put_file = ("/".join
                                (self.commands[self.index_d:self.index_f]))
            file_to_open = (f"{path_to_put_file}"
                            f"/{file_to_open}")

        with open(file_to_open, "a") as file:
            time_now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            file.write(time_now + "\n")
            while True:
                data = input("Enter content line: ")
                if data == "stop":
                    file.write("\n")
                    break
                file.write(data + "\n")

    def create_directory(self) -> None:

        path = "/".join(self.commands[self.index_d:self.index_f])
        if os.path.exists(path):
            return

        directory_path = self.commands[self.index_d:self.index_f]
        nested_directory = os.path.join(*directory_path)
        os.makedirs(nested_directory)

    def activate(self) -> None:

        if "-d" in self.commands:
            self.create_directory()
        if "-f" in self.commands:
            self.create_file()


command = Command(sys.argv)
command.activate()
