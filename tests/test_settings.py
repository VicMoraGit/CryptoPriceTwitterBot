"""
    Tests for settings class
"""

from settings import Settings

#Save method tests

def test_save_method_correct_config_file_path():
    """
    Tests save method works with correct configuration file path

    """

    settings = Settings("config.example")

    assert settings.save() is True

def test_save_method_wrong_config_file_path():
    """
    Tests save method works with wrong configuration file path

    """
    settings = Settings("thisFileDoesNotExist.example")

    assert settings.save() is False

def test_load_method_correct_config_file_path():
    """
    Tests load method works with correct configuration file path

    """

    settings = Settings("config.example")

    assert settings.load() is True

def test_load_method_wrong_config_file_path():
    """
    Tests load method works with wrong configuration file path

    """
    settings = Settings("thisFileDoesNotExist.example")

    assert settings.load() is False
