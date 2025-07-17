import os

from ayon_core.addon import AYONAddon
from ayon_core.pipeline.context_tools import get_current_context

from .version import __version__
from .api.casting_manager import get_casting

# TODO - use pathlib
BUILD_WORKFILE_ADDON_ROOT_DIR = os.path.dirname(os.path.abspath(__file__))


class BuildWorkfileAddon(AYONAddon):
    """Build workfile addon."""

    label = "Build Workfile"
    name = "build_workfile"
    version = __version__

    def initialize(self, settings):
        """Initialization of addon."""
        pass

    def get_launch_hook_paths(self, app):
        return [os.path.join(BUILD_WORKFILE_ADDON_ROOT_DIR, "hooks")]

    def build_workfile(self, local_overrides: dict = None):
        """Build current workfile.

        Args:
            local_overrides (dict): Local settings overrides. Defaults to None.
        """
        context = get_current_context()

        for actor in get_casting():
            actor.build(context)
