"""
    Custom exceptions module
"""

class SettingsNotLoadedException(Exception):

    def __init__(self) -> None:
        self.message = "Settings not loaded correctly"
        super().__init__(self.message)
