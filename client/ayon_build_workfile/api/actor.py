from .server_settings import get_main_settings, get_settings_exceptions

class Actor:
    product_name: string = None
    product_type: string = None
    # Or loader class?
    loader: string = None
    # type: reference to a product
    product_to_switch = None

    def __init__(
        kitsu_actor: dict,
        server_settings: dict = None,
        settings_overrides: dict = None,
    ):
        # TODO get product_name and product_type from kitsu_actor

        main_settings = get_main_settings(server_settings)
        settings_exceptions = get_settings_exceptions(server_settings)

    def __init__(
        kitsu_actor: dict,
        main_settings: dict,
        settings_exceptions: dict,
        settings_overrides: dict = None,
    ):
        pass

    def __init__(
        product_name: string,
        product_type: string,
        server_settings: dict = None,
        settings_overrides: dict = None,
    ):
        self.product_name = product_name
        self.product_type = product_type

        main_settings = get_main_settings(server_settings)
        settings_exceptions = get_settings_exceptions(server_settings)

    def __init__(
        product_name: string,
        product_type: string,
        main_settings: dict,
        settings_exceptions: dict,
        settings_overrides: dict = None,
    ):
        self.product_name = product_name
        self.product_type = product_type

    def build():
        pass
