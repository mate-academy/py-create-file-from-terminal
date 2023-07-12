from argparse import ArgumentParser, Namespace
from datetime import datetime
from os import makedirs
from os.path import isfile, join as compose_path


class TextEditorApp:
    def __init__(self) -> None:
        self.full_path: str = ""

        self.process_the_arguments()

    @staticmethod
    def parse_args() -> Namespace:
        parser = ArgumentParser()
        parser.add_argument("-d", "--dir", nargs="+")
        parser.add_argument("-f", "--file", type=str)

        args = parser.parse_args()

        return args

    def process_the_arguments(self) -> None:
        app_args = self.parse_args()

        path = app_args.dir
        file_name = app_args.file

        if path:
            dir_path = compose_path(*path)

            makedirs(dir_path)
            self.full_path = dir_path

        if not file_name:
            exit()

        self.full_path = compose_path(self.full_path, file_name)

    @staticmethod
    def make_data() -> str:
        data = list()

        while True:
            line = input("Enter content line: ")

            if line == "stop":
                break

            data.append(line)

        return "\n".join(f"{i + 1} {line}" for i, line in enumerate(data))

    def write_file(self, data: str) -> None:
        is_file_old = isfile(self.full_path)
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        with open(self.full_path, "a") as file:
            if is_file_old:
                file.write("\n\n")

            file.write(f"{timestamp}\n")
            file.write(data)

    def start(self) -> None:
        data = self.make_data()

        self.write_file(data)


if __name__ == "__main__":
    app = TextEditorApp()

    app.start()
