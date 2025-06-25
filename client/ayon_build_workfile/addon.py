import asyncio

from ayon_core.addon import AYONAddon
from ayon_core.pipeline.context_tools import get_current_context
import ayon_harmony.api as harmony

from .version import __version__
from .api.casting_manager import get_casting
from .settings_manager import (
    get_server_settings,
    get_settings_overrides,
    get_applied_settings,
)


class BuildWorkfileAddon(AYONAddon):
    """Build workfile addon."""

    label = "Build Workfile"
    name = "build_workfile"
    version = __version__

    def __init__(self):
        """Initialization of addon."""
        harmony.send(
            {
                "function": "ayon_build_workfile.hosts.harmony.ui.addButton"
            }
        )

    def build_workfile(self, local_overrides: dict = None):
        """Build current workfile.

        Args:
            local_overrides (dict): Local settings overrides. Defaults to None.
        """
        context = get_current_context()

        for actor in get_casting():
            actor.build(context)
