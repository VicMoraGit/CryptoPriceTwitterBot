"""
    Custom exceptions module
"""
class SettingsNotLoadedException(Exception):
    """Exception raised when configuration file is not in proper format

    Args:
        Exception (_type_): inherits from Exception class
    """

    def __init__(self) -> None:
        self.message = "Settings not loaded correctly"
        super().__init__(self.message)
