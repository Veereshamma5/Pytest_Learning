DEFAULT_ERROR_MESSAGE = "An unexpected error message has occured"


class DuplicateRecordException(Exception):
    def __init__(self, msg=DEFAULT_ERROR_MESSAGE, *args, **kwargs):
        super().__init__(msg, *args)


class CreateRecordFailedException(Exception):
    def __init__(self, msg, *args, **kwargs):
        super().__init__(msg, *args)
