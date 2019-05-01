class ServerException(Exception):
    def __init__(self, error):
        self.error = error


class TempliteSyntaxError(Exception):
    def __init__(self, error):
        self.error = error

