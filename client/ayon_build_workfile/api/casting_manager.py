import gazu

from .actor import Actor
from .server_settings import get_server_settings, get_settings_overrides


def get_casting(asset_name: str) -> dict:
    # TODO get entity id
    entity_id = "TODO"

    entity = gazu.get_entity(entity_id)

    assert entity, "Kitsu entity not found."

    # TODO get entity type
    entity_type = "asset"

    casting = None
    if entity_type == "asset":
        casting = gazu.casting.get_asset_casting(entity)
    elif entity_type == "shot":
        casting = gazu.casting.get_shot_casting(entity)
    else:
        raise RuntimeError(f"{entity_type} is not a recognized entity type.")

    assert casting, "Casting not found."

    actors = []
    server_settings = get_server_settings()
    settings_overrides = get_settings_overrides()
    for actor in casting:
        product_reference = None

        # TODO find if actor exists in scene

        # TODO create new Actor object and append it to `actors`
        actors.append(
            Actor(actor, server_settings, settings_overrides)
        )

    return actors
