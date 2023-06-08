import sys
import os
import datetime
terminal_input = ['-d', 'dir1', 'dir2']

print(terminal_input)

def argument_parser() -> None:

    terminal_input = sys.argv[1::]

    if len(terminal_input) <= 1:
        return
    path = os.getcwd() #TODO: delete?

    if "-d" in terminal_input and "-f" in terminal_input:

        folders = terminal_input[terminal_input.index("-d") + 1:
                                 terminal_input.index("-f"):]
        for folder in folders:
            path = os.path.join(path, folder)

        create_dir(path)
        create_file(os.path.join(path, terminal_input[-1]))
        return

    if "-d" in terminal_input:
        create_path(cr_dir=True)
        create_dir(path)
        return

    if "-f" in terminal_input:
        create_file(path=os.getcwd())
        return


if __name__ == "__main__":
    argument_parser()
