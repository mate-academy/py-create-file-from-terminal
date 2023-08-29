import sys

def parse_console_input() -> None:
    terminal_input = sys.argv[1:]

    if "-f" in terminal_input and "-d" in terminal_input:
        read_file_name_index = terminal_input.index("-f")
        read_directory_name_index = terminal_input.index("-d")

        if read_file_name_index < read_directory_name_index:
            file_name = terminal_input[read_file_name_index + 1]
            directory_name = terminal_input[read_directory_name_index + 1]
        else:
            file_name = terminal_input[read_file_name_index + 1]
            directory_name = terminal_input[read_directory_name_index + 1]
    else:
        print("Необходимо указать и флаг -f, и флаг -d.")
        return

    print("Имя файла:", file_name)
    print("Имя директории:", directory_name)

parse_console_input()
