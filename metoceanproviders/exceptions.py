class DatasetNameError(Exception):
    """Custom error for invalid dataset"""

    def __init__(self, message, name=None):
        self.message = message
        self.dataset_name = name
        super().__init__(message)


class CredentialsError(Exception):
    """Custom error for incorrect credentials"""

    def __init__(self, username: str, password: str, message: str):
        self.username = username
        self.password = password
        self.message = message
        super().__init__(message)
