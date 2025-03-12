def get_server_settings() -> dict:
    """Get server settings as is.

    Returns:
        dict: Server settings.
    """
    pass


def get_default_settings() -> dict:
    """Get default settings from server.

    Returns:
        dict: Default settings.
    """
    pass


def get_settings_exceptions() -> dict:
    """Get settings exceptions from server.

    Returns:
        dict: Settings exceptions.
    """
    pass


def get_settings_override() -> dict:
    """Get settings local overrides.

    Returns:
        dict: Settings overrides.
    """
    pass


# Not sure about this function name.
# Needs to be product specific?
def get_applied_settings(
    allow_exceptions: bool = True, allow_overrides: bool = True
) -> dict:
    """Get settings after applying settings exceptions and settings overrides.

    This goes as follows:
    - Default settings are fetched.
    - Settings exceptions are used to update the settings dict.
    - Settings overrides are used to update the settings dict.
    - The resulting dict is returned.

    Args:
        allow_exceptions (bool): Applies settings exceptions if True.
            Defaults to True.
        allow_overrides (bool): Applies settings overrides if True.
            Defaults to True.

    Returns:
        dict: Applied settings.
    """
    pass
