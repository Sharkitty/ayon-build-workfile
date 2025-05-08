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
        actor: dict,
        server_settings: dict = None,
        settings_overrides: dict = None,
        product_reference = None,
    ):
        self.product_name = actor.get("name")
        # TODO product_type from kitsu_actor

        main_settings = get_main_settings(server_settings)
        settings_exceptions = get_settings_exceptions(server_settings)

        self.product_reference = product_reference

    def __init__(
        actor: dict,
        main_settings: dict,
        settings_exceptions: dict,
        settings_overrides: dict = None,
        product_reference = None,
    ):
        self.product_name = actor.get("name")

        self.product_reference = product_reference

    def __init__(
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

        self.product_reference = product_reference

    def __init__(
        product_name: string,
        product_type: string,
        main_settings: dict,
        settings_exceptions: dict,
        settings_overrides: dict = None,
        product_reference = None,
    ):
        self.product_name = product_name
        self.product_type = product_type

        self.product_reference = product_reference

    def build(context):
        if product_reference:
            # switch product
            pass
        else:
            # load product
            self.loader.load(context)
