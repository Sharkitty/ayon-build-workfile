from ayon_server.settings import BaseSettingsModel


class DefaultSettingsModel(BaseSettingsModel):
    pass


class SettingsExceptionsModel(BaseSettingsModel):
    pass


class BuildWorkfileSettings(BaseSettingsModel):
    default_settings: DefaultSettingsModel = None

    settings_exceptions: SettingsExceptionsModel = None


DEFAULT_VALUES = {
    "default_settings": None,
    "settings_exceptions": None,
}
