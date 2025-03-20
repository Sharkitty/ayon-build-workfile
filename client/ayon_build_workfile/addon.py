import asyncio

from ayon_core.addon import AYONAddon

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

    async def build_actor(
        self, actor: dict, server_settings: dict, settings_overrides: dict
    ):
        """Build a single actor into the scene.

        Args:
            actor (dict): Casted actor.
            server_settings (dict): Server settings.
            settings_overrides: Settings local overrides.
        """
        applied_settings = get_applied_settings(
            server_settings=server_settings,
            settings_overrides=settings_overrides,
        )

        # TODO Load asset

    # TODO get product type
    async def switch_product(
        self, product, server_settings: dict, settings_overrides: dict
    ):
        """Switch a product based on settings.

        Args:
            product (TODO): Product loaded in scene.
            server_settings (dict): Server settings.
            settings_overrides (dict): Settings local overrides.
        """
        applied_settings = get_applied_settings(
            server_settings=server_settings,
            settings_overrides=settings_overrides,
        )

        # TODO check if product needs to be switched
        product_needs_switching = True
        if product_needs_switching:
            # TODO switch product
            pass

    def build_from_scratch(self):
        """Build workfile from scratch."""
        casting_task = asyncio.create_task(get_casting())
        server_settings_task = asyncio.create_task(get_server_settings())
        settings_overrides_task = asyncio.create_task(get_settings_overrides())

        casting, server_settings, settings_overrides = asyncio.gather(
            casting_task, server_settings_task, settings_overrides_task
        )

        casting = casting.result()
        server_settings = server_settings.result()
        settings_overrides = settings_overrides.result()

        tasks = []
        for actor in casting:
            tasks.append(
                asyncio.create_task(
                    self.build_actor(
                        actor, server_settings, settings_overrides
                    )
                )
            )

        # TODO error handling
        asyncio.gather(tasks)

    def build_from_other_task_workfile(self):
        """Build workfile using the workfile of another task as a base."""
        server_settings_task = asyncio.create_task(get_server_settings())
        settings_overrides_task = asyncio.create_task(get_settings_overrides())

        server_settings, settings_overrides = asyncio.gather(
            server_settings_task, settings_overrides_task
        )

        server_settings = server_settings.result()
        settings_overrides = settings_overrides.result()

        # TODO get products in scene
        products_in_scene = []

        tasks = []
        for product in products_in_scene:
            tasks.append(
                asyncio.create_task(
                    product, server_settings, settings_overrides
                )
            )

        # TODO error handling
        asyncio.gather(tasks)
