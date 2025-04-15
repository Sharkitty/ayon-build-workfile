def get_server_settings() -> dict:
    """Get server settings as is.

    Returns:
        dict: Server settings.
    """
    pass


def get_main_settings(server_settings: dict = None) -> dict:
    """Get main settings from server.

    Args:
        server_settings (dict): Server settings (optional). Defaults to None.

    Returns:
        dict: Main settings.
    """
    if not server_settings:
        server_settings = get_server_settings()

    # TODO


def get_settings_exceptions(server_settings: dict = None) -> dict:
    """Get settings exceptions from server.

    Args:
        server_settings (dict): Server settings (optional). Defaults to None.

    Returns:
        dict: Settings exceptions.
    """
    if not server_settings:
        server_settings = get_server_settings()

    # TODO


def get_settings_overrides() -> dict:
    """Get settings local overrides.

    Returns:
        dict: Settings overrides.
    """
    pass


# Not sure about this function name.
# Needs to be product specific?
def get_applied_settings(
    allow_exceptions: bool = True,
    allow_overrides: bool = True,
    server_settings: dict = None,
    settings_overrides: dict = None,
) -> dict:
    """Get settings after applying settings exceptions and settings overrides.

    This goes as follows:
    - Main settings are fetched.
    - Settings exceptions are used to update the settings dict.
    - Settings overrides are used to update the settings dict.
    - The resulting dict is returned.

    Args:
        allow_exceptions (bool): Applies settings exceptions if True.
            Defaults to True.
        allow_overrides (bool): Applies settings overrides if True.
            Defaults to True.
        server_settings (dict): Server settings (optional). Defaults to None.
        settings_overrides (dict): Settings overrides (optional).
            Defaults to None.

    Returns:
        dict: Applied settings.
    """
    if not server_settings:
        server_settings = get_server_settings()

    if not settings_overrides:
        settings_overrides = get_settings_overrides()

    # TODO
