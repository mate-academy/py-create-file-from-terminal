import datetime
import os

"""
    Функция которая получает строку с путём к файлу
        пример 'python create_file.py -d dir1 dir2 -f file.txt'
    в зависимости от наличия в строке флажков '-d'-создаём папку и '-f' создаём файл
    или и то и другое
"""


def write_new_file_with_input(file_path: str):
    if "-d" in file_path and "-f" in file_path:  # проверяем флаги
        create_path(file_path)  # если нет то создаём директорию
        create_file(file_path)  # и создаем файл и записываем туда весь ввод
    elif "-d" in file_path:
        create_path(file_path)  # если только такой флаг то только создаём папки
    else:
        create_file(file_path)  # если только ф то создаём файл


"""
Function create a path from string
"""


def create_path(check_flag_d: str):
    if "-d" in check_flag_d:
        ind = check_flag_d.index("-d")
        x = check_flag_d[ind + 3:].split()
        x.remove("-f")
        x.remove('file.txt')
        os.makedirs("/".join(x))
        os.chdir(r"C:\Users\Igor\PycharmProjects\pythonProject\py-create-file-from-terminal\app\dir1\dir2")
        print(os.getcwd())


"""Function takes string, create a file and save all inputs before "stopp"
"""


def create_file(check_flag_f: str):
    time_today = datetime.datetime.now()  # берём сегодняшнюю дату с модуля datetime
    daytime_strf = time_today.strftime("%Y-%m-%d %H:%M:%S" + "\n")  # форматируем дату в нужный вид
    if "-f" in check_flag_f:  # если есть флаг -f в строке тогда выполняем
        file_name = check_flag_f.split(" ")[-1]  # создаём переменную с последнего индекса списка входящего аргумента
        if os.path.exists("file.txt"):  # если такой файл есть то записываем в него
            print("1")
            with open(file_name, "a") as add_newline:  # если есть то открываем с флажком append,
                add_newline.write(f"{daytime_strf}\n")  # записываем в файл дату
                lines_num = 1  # считаем кол-во строк для записи
                print("2")
                while True:
                    line = input("Enter content line: ")  # вводим и записываем в нужном формате
                    add_newline.write(f"{lines_num} Another {line} content \n")
                    if line.lower() == "stop":  # когда вводят стоп цикл останавливается
                        break
                    print("3")
                    lines_num += 1

        if not os.path.exists("file.txt"):  # если файла нет тогда создаём файл
            print("1.1")
            with open(file_name, "a") as f:
                f.write(f"{daytime_strf}\n")  # записываем отформатированную дату
                lines_num = 1
                print("1.2")
                while True:
                    content = input(f"Enter content line: ")  # открываем поле для ввода
                    f.write(f"{lines_num} {content} content \n")  # то что ввели записываем в нужном формате
                    if "stop" in content.lower():  # если получили стоп цикл прерывается
                        break
                    lines_num += 1
                    print("1.3")
            f.close()
            print("finish")

print(write_new_file_with_input('python create_file.py -d dir1 dir2 -f file.txt'))
