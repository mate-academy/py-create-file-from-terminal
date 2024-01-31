import sys
import os
import datetime


def get_directory_list(cmd_ls: list) -> str | None:
    if cmd_ls.count("-d"):
        if cmd_ls.count("-f"):
            directory = cmd_ls[cmd_ls.index("-d") + 1: cmd_ls.index("-f")]
        else:
            directory = cmd_ls[cmd_ls.index("-d") + 1:]
        return directory


def get_file_name(cmd_ls: list) -> str | None:
    if cmd_ls.count("-f"):
        return cmd_ls[-1]


def create_file(cmd_ls: list) -> None:
    time_now = datetime.datetime.now()
    final_path = os.path.join(os.getcwd())

    if directory_list := get_directory_list(cmd_ls):
        try:
            for directory in directory_list:
                final_path = os.path.join(final_path, directory)
                os.mkdir(final_path)

        except FileExistsError:
            final_path = os.path.join(os.getcwd(), *directory_list)

    if file_name := get_file_name(cmd_ls):
        date = (
            f'{time_now.strftime("%Y-%m-%d")}'
            f' {time_now.strftime("%X")} \n'
        )
        with open(os.path.join(final_path, file_name), "a") as file_in:
            file_in.writelines(date)
            count = 1
            while True:
                user_input = input("content line: ")
                if user_input != "stop":
                    file_in.writelines(f"{count} {user_input}\n")
                    count += 1
                else:
                    file_in.writelines("\n")
                    break


if __name__ == "__main__":
    create_file(sys.argv)
