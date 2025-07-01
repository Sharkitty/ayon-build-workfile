from typing import Type

from ayon_server.addons import BaseServerAddon

from .settings import BuildWorkfileSettings, DEFAULT_VALUES


class BuildWorkfileAddon(BaseServerAddon):
    settings_model: Type[BuildWorkfileSettings] = BuildWorkfileSettings

    async def get_default_settings(self):
        settings_model_cls = self.get_settings_model()
        # FIX ME default values can't be None
        return settings_model_cls(**DEFAULT_VALUES)
