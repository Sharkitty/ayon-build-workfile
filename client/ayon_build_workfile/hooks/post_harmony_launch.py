from ayon_applications import PostLaunchHook
import ayon_hamony.aspi as harmony


class PostHarmonyLaunch(PostLaunchHook):

    def execute(self):
        harmony.send(
            {
                "function": "ayon_build_workfile.hosts.harmony.ui.addButton"
            }
        )
