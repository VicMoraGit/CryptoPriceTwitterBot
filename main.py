"""
    Runs bot main process.

"""

from custom_exceptions import SettingsNotLoadedException
from settings import Settings


if __name__ == "__main__":

    #Set bot settings

    settings = Settings("")

    IS_LOADED = settings.load()

    if not IS_LOADED:
        raise SettingsNotLoadedException()
