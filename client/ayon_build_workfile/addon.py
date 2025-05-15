import asyncio

from ayon_core.addon import AYONAddon
from ayon_core.pipeline.context_tools import get_current_context

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

    def initialize(self, settings):
        """Initialization of addon."""
        pass

    def build_workfile(self, local_overrides: dict = None):
        """Build current workfile.

        Args:
            local_overrides (dict): Local settings overrides. Defaults to None.
        """
        # Resolve casting
        casting = get_casting()

        server_settings = get_server_settings()

        # Was supposed to only apply overrides if they're not None
        # but if they're None they're just ignored by this method
        applied_settings = get_applied_settings(
            server_settings, local_overrides
        )

        for actor in casting:
            actor.build(get_current_context())
