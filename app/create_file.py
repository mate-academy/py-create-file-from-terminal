from datetime import datetime
from sys import argv
from os import mkdir, path


FILE_NAME_FLAG = '-f'
FILE_PATH_FLAG = '-d'


def get_content():
    content = []
    while (line := input('Enter content line: ')).lower() != 'stop':
        content.append(line + '\n')

    return content


def check_sys_argv():
    return ((FILE_PATH_FLAG in argv and FILE_NAME_FLAG in argv)
            or (FILE_NAME_FLAG in argv))


def parse_sys_args():
    if not check_sys_argv():
        raise Exception('Called with wrong arguments')

    parsed_argv = {'file_name': None, 'file_path': None}
    if FILE_PATH_FLAG in argv:
        path_index = argv.index(FILE_PATH_FLAG)
        name_index = argv.index(FILE_NAME_FLAG)
        end_index = name_index if name_index > path_index else len(argv)
        parsed_argv['file_path'] = '\\'.join(argv[path_index + 1: end_index])
    if FILE_NAME_FLAG in argv:
        parsed_argv['file_name'] = argv[argv.index(FILE_NAME_FLAG) + 1]

    return parsed_argv


def main():
    config = parse_sys_args()
    file_dir = config['file_path'] or ''
    file_name = config['file_name'] or None
    print(file_dir, file_name)
    if file_dir and not path.isdir(file_dir):
        mkdir(file_dir)

    with open(file=file_dir + '\\' + file_name, mode='a') as fout:
        content = get_content()
        fout.write(datetime.now().strftime('%Y-%m-%d %H:%M:%S\n'))
        fout.writelines(content)


if __name__ == '__main__':
    main()
