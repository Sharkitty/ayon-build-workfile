from ayon_core.pipeline.load.utils import get_loaders_by_name

from .settings_manager import (
    get_server_settings,
    get_main_settings,
    get_settings_exceptions,
)

class Actor:
    product_name: string = None
    product_type: string = None
    # Or loader class?
    loader: type = None
    # type: reference to a product
    product_reference = None

    def __init__(
        self,
        actor: dict,
        server_settings: dict = None,
        settings_overrides: dict = None,
        product_reference = None,
    ):
        self.product_name = actor.get("name")
        self.product_type = actor.get("asset_type_name")

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
            and self.product_name in settings_exceptions.get("entity_names". [])
            and settings_exceptions.get("loader_regex")
        ):
            loader_regex = settings_exceptions.get("loader_regex")
        else:
            loader_regex = main_settings.get("loader_regex")

        self.product_reference = product_reference

    def __init__(
        self,
        actor: dict,
        main_settings: dict,
        settings_exceptions: dict,
        settings_overrides: dict = None,
        product_reference = None,
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
            and self.product_name in settings_exceptions.get("entity_names". [])
            and settings_exceptions.get("loader_regex")
        ):
            loader_regex = settings_exceptions.get("loader_regex")
        else:
            loader_regex = main_settings.get("loader_regex")

        self.product_reference = product_reference

    def __init__(
        self,
        product_name: string,
        product_type: string,
        server_settings: dict = None,
        settings_overrides: dict = None,
        product_reference = None,
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
            and self.product_name in settings_exceptions.get("entity_names". [])
            and settings_exceptions.get("loader_regex")
        ):
            loader_regex = settings_exceptions.get("loader_regex")
        else:
            loader_regex = main_settings.get("loader_regex")

        self.product_reference = product_reference

    def __init__(
        self,
        product_name: string,
        product_type: string,
        main_settings: dict,
        settings_exceptions: dict,
        settings_overrides: dict = None,
        product_reference = None,
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
            and self.product_name in settings_exceptions.get("entity_names". [])
            and settings_exceptions.get("loader_regex")
        ):
            loader_regex = settings_exceptions.get("loader_regex")
        else:
            loader_regex = main_settings.get("loader_regex")

        self.product_reference = product_reference

    def build(self, context):
        if product_reference:
            # switch product
            pass
        else:
            # load product
            self.loader.load(context)
