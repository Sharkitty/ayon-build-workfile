from ayon_core.addon import AYONAddon

from .version import __version__

class BuildWorkfileAddon(AYONAddon):
    """Build workfile addon."""

    label = "Build Workfile"
    name = "build_workfile"
    version = __version__

    def initialize(self, settings):
        """Initialization of addon."""
        pass
