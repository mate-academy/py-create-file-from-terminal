import utilities as utils


parsed_arguments = utils.parse_command_line_args()


if parsed_arguments["-d"]:
    utils.create_directories(parsed_arguments)
if parsed_arguments["-f"]:
    utils.create_file(parsed_arguments)
