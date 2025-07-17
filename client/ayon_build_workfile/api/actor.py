import re

from ayon_core.pipeline.load import get_loaders_by_name, switch_container

from .settings_manager import (
    get_server_settings,
    get_main_settings,
    get_settings_exceptions,
)

class Actor:
    product_name: str = None
    product_type: str = None
    # Or loader class?
    loader: type = None
    # type: reference to a product
    container = None

    def __init__(
        self,
        actor: dict,
        server_settings: dict = None,
        settings_overrides: dict = None,
        container = None,
    ):
        self.product_name = actor.get("name")
        self.product_type = actor.get("asset_type_name")

        main_settings = get_main_settings(server_settings)
        settings_exceptions = get_settings_exceptions(server_settings)

        loader_regex = None
        if (
            settings_overrides
            and self.product_name in settings_overrides.get("entity_names", [])
            and settings_overrides.get("loader_regex")
        ):
            loader_regex = settings_overrides.get("loader_regex")
        elif (
            settings_exceptions
            and self.product_name in settings_exceptions.get("entity_names", [])
            and settings_exceptions.get("loader_regex")
        ):
            loader_regex = settings_exceptions.get("loader_regex")
        else:
            loader_regex = main_settings.get("loader_regex")

        for loader in discover_loader_plugins():
            if re.match(loader_regex, loader.__name__):
                self.loader = loader
                break

        self.container = container

    def __init__(
        self,
        actor: dict,
        main_settings: dict,
        settings_exceptions: dict,
        settings_overrides: dict = None,
        container = None,
    ):
        self.product_name = actor.get("name")
        self.product_type = actor.get("asset_type_name")

        loaders = get_loaders_by_name()
        loader_regex = None
        if (
            settings_overrides
            and self.product_name in settings_overrides.get("entity_names", [])
            and settings_overrides.get("loader_regex")
        ):
            loader_regex = settings_overrides.get("loader_regex")
        elif (
            settings_exceptions
            and self.product_name in settings_exceptions.get("entity_names", [])
            and settings_exceptions.get("loader_regex")
        ):
            loader_regex = settings_exceptions.get("loader_regex")
        else:
            loader_regex = main_settings.get("loader_regex")

        for loader in discover_loader_plugins():
            if re.match(loader_regex, loader.__name__):
                self.loader = loader
                break

        self.container = container

    def __init__(
        self,
        product_name: str,
        product_type: str,
        server_settings: dict = None,
        settings_overrides: dict = None,
        container = None,
    ):
        self.product_name = product_name
        self.product_type = product_type

        main_settings = get_main_settings(server_settings)
        settings_exceptions = get_settings_exceptions(server_settings)

        loaders = get_loaders_by_name()
        loader_regex = None
        if (
            settings_overrides
            and self.product_name in settings_overrides.get("entity_names", [])
            and settings_overrides.get("loader_regex")
        ):
            loader_regex = settings_overrides.get("loader_regex")
        elif (
            settings_exceptions
            and self.product_name in settings_exceptions.get("entity_names", [])
            and settings_exceptions.get("loader_regex")
        ):
            loader_regex = settings_exceptions.get("loader_regex")
        else:
            loader_regex = main_settings.get("loader_regex")

        for loader in loaders:
            if re.match(loader_regex, loader.__name__):
                self.loader = loader
                break

        self.container = container

    def __init__(
        self,
        product_name: str,
        product_type: str,
        main_settings: dict,
        settings_exceptions: dict,
        settings_overrides: dict = None,
        container = None,
    ):
        self.product_name = product_name
        self.product_type = product_type

        loaders = get_loaders_by_name()
        loader_regex = None
        if (
            settings_overrides
            and self.product_name in settings_overrides.get("entity_names", [])
            and settings_overrides.get("loader_regex")
        ):
            loader_regex = settings_overrides.get("loader_regex")
        elif (
            settings_exceptions
            and self.product_name in settings_exceptions.get("entity_names", [])
            and settings_exceptions.get("loader_regex")
        ):
            loader_regex = settings_exceptions.get("loader_regex")
        else:
            loader_regex = main_settings.get("loader_regex")

        for loader in discover_loader_plugins():
            if re.match(loader_regex, loader.__name__):
                self.loader = loader
                break

        self.container = container

    def build(self, context):
        if self.container:
            # switch product
            switch_container(
                self.container,
                self.container.get("representation"),
                loader_plugin=self.loader,
            )
        else:
            # load product
            self.loader.load(context)
