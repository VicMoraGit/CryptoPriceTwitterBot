"""
    Bot settings class
"""

import json


class Settings:
    """
        Imports, store and exports bot settings
    """
    def __init__(self) -> None:
        self.is_first_run = None

    def load(self, config_file_path:str) -> bool:

        """Loads all the config file parameters to the settings class

        Args:
            config_file_path (str): Configuration file path

        Returns:
            bool: returns whether settings loading process was or not successful
        """
        try:
            settings = self._parse_config_file(config_file_path)
            self.is_first_run = settings["isFirstRun"]

        except Exception:

            return False
        return True

    def _parse_config_file(self, config_file_path:str):
        """Returns a json object from the configuration file contents

        Args:
            config_file_path (str): Configuration file path

        Returns:
            dict: Contains configuration parameters as a json object
        """
        settings = json.loads(self._open_file(config_file_path))
        return settings

    def _open_file(self, file_path:str):
        """Opens a file

        Args:
            file_path (str): file path

        Returns:
            str: file content
        """
        with open(file=file_path, mode="r", encoding="UFT-8") as file:
            json_content = file.read()
            file.close()
        return json_content
