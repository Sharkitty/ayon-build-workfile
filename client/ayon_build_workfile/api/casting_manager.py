import gazu
from ayon_api import get_folder_by_path
from ayon_core.pipeline.context_tools import (
    get_current_folder_path,
    get_current_project_name,
    registered_host,
)

from .actor import Actor
from .settings_manager import get_server_settings, get_settings_overrides


# TODO separate get current casting and get asset casting (where you can choose the asset)
def get_casting() -> dict:
    # Get zou entity
    zou_entity = gazu.entity.get_entity(
        get_folder_by_path(
            get_current_project_name(), get_current_folder_path()
        )["data"]["kitsuId"]
    )

    assert zou_entity, "Kitsu entity not found."

    entity_type = gazu.entity.get_entity_type(zou_entity["entity_type_id"])

    casting = None
    if entity_type == "asset":
        casting = gazu.casting.get_asset_casting(zou_entity)
    elif entity_type == "shot":
        casting = gazu.casting.get_shot_casting(zou_entity)
    else:
        raise RuntimeError(f"{entity_type} is not a recognized entity type.")

    assert casting, "Casting not found."

    actors = []
    server_settings = get_server_settings()
    settings_overrides = get_settings_overrides()

    host = registered_host()
    containers = host.get_containers()

    for actor in casting:
        # Get loaded container
        container = None
        for c in containers:
            if actor.get("name") == c.get("representation", {}).get("name"):
                container = c

        actors.append(
            Actor(actor, server_settings, settings_overrides, container=container)
        )

        # Remove container from list, so we can account for product and actor amounts
        containers.pop(container)

    return actors
