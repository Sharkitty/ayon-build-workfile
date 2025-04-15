from ayon_server.settings import BaseSettingsModel, SettingsField


class MainSettingsModel(BaseSettingsModel):
    execute_synchronously: bool = SettingsField(
        False, title="Execute Synchronously"
    )
    loader_regex: rstring = SettingsField(r"", title="Loader")
    hero_version: bool = SettingsField(False, title="Hero Version")


class SettingsExceptionsModel(BaseSettingsModel):
    entity_names: list[rstring] = SettingsField(
        title="Entity Names", default_factory=list
    )
    task_types: list[rstring] = SettingsField(
        title="Task Types", default_factory=list
    )
    use_other_task_workfile: bool = SettingsField(
        False, title="Use Other Task Workfile"
    )
    # TODO Should appear only if `use_other_task_workfile` is set to True
    other_task: string = SettingsField("", title="Other Task")


class BuildWorkfileSettings(BaseSettingsModel):
    main_settings: MainSettingsModel = SettingsField(
        title="Main Settings", default_factory=MainSettingsModel
    )

    settings_exceptions: list[SettingsExceptionsModel] = SettingsField(
        title="Settings Exceptions", default_factory=list
    )


DEFAULT_VALUES = {
    "main_settings": None,
    "settings_exceptions": None,
}
