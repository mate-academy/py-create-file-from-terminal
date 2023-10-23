class WrongNumberOfArguments(Exception):
    def __init__(self,
                 number_of_arguments: int,
                 message: str = None) -> None:
        self.number_of_arguments = number_of_arguments
        self.message = message
        if not message:
            self.message = (f"Wrong number of arguments passed! "
                            f"Got: {self.number_of_arguments}")
        super().__init__(self.message)


class ArgumentsCantBeParsed(Exception):
    pass
