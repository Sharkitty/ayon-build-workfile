from ayon_applications import PostLaunchHook
from ayon_harmony.api import send


class PostHarmonyLaunch(PostLaunchHook):

    def execute(self):
        send(
            {
                "function": "ayon_build_workfile.hosts.harmony.ui.addButton"
            }
        )
