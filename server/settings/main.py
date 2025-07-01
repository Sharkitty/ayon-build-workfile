from ayon_server.settings import BaseSettingsModel, SettingsField


class MainSettingsModel(BaseSettingsModel):
    execute_synchronously: bool = SettingsField(
        False, title="Execute Synchronously"
    )
    loader_regex: str = SettingsField(r"", title="Loader")
    hero_version: bool = SettingsField(False, title="Hero Version")


class SettingsExceptionsModel(BaseSettingsModel):
    entity_names: list[str] = SettingsField(
        title="Entity Names", default_factory=list
    )
    task_types: list[str] = SettingsField(
        title="Task Types", default_factory=list
    )
    loader_regex: str = SettingsField(r"", title="Loader")
    use_other_task_workfile: bool = SettingsField(
        False, title="Use Other Task Workfile"
    )
    # TODO Should appear only if `use_other_task_workfile` is set to True
    other_task: str = SettingsField("", title="Other Task")


class BuildWorkfileSettings(BaseSettingsModel):
    main_settings: MainSettingsModel = SettingsField(
        title="Main Settings", default_factory=MainSettingsModel
    )

    settings_exceptions: list[SettingsExceptionsModel] = SettingsField(
        title="Settings Exceptions", default_factory=list
    )


DEFAULT_VALUES = {
    "main_settings": {
        "execute_synchronously": False,
        "loader_regex": r"",
        "hero_version": False,
    },
    "settings_exceptions": {
        "entity_names": [],
        "task_types": [],
        "loader_regex": r"",
        "use_other_task_workfile": False,
        "other_task": "",
    },
}
