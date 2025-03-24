import sys
from app.sup_funcs import write_line_by_line, make_dirs_and_file


passed_params = list(sys.argv[1:])

# Only -f
if "-d" not in passed_params and "-f" in passed_params:
    passed_params.remove("-f")
    write_line_by_line(passed_params[0])


# Only -d
elif "-d" in passed_params and "-f" not in passed_params:
    passed_params.remove("-d")
    make_dirs_and_file(passed_params)

# Both
elif "-d" in passed_params and "-f" in passed_params:
    file_name = None
    dir_list = []
    for i in range(0, len(passed_params)):
        if passed_params[i] == "-f":
            file_name = passed_params[i + 1]

        elif passed_params[i] == "-d":
            for serach_index in range(i + 1, len(passed_params)):
                if passed_params[serach_index] == "-f":
                    break
                dir_list.append(passed_params[serach_index])

    make_dirs_and_file(dir_list, file_name)

# Nothing
else:
    print("You didn't pass anything!")
