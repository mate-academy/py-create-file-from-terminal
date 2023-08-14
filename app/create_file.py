from dirs_and_file_handling import create_path
from dirs_and_file_handling import create_new_file
from dirs_and_file_handling import parse_arguments


def main() -> None:
    args = parse_arguments()
    directories = args.d
    file_name = args.f

    if not directories and not file_name:
        raise ValueError("No arguments provided. Use -d to create directories "
                         "and/or -f to create a file_name.")

    if directories and not file_name:
        create_path(directory_list=directories)
        print("Folder(s) created.")

    elif file_name and not directories:
        create_new_file(filename=file_name)
        print("File created in the current directory.")

    elif directories and file_name:
        create_path(directories)
        create_new_file(directory_list=directories, filename=file_name)
        print("The file_name has been appended with your "
              "content in the specified directory.")


if __name__ == "__main__":
    main()
