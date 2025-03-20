import gazu


def get_casting(asset_name: str) -> dict:
    # TODO get entity id
    entity_id = "TODO"

    entity = gazu.get_entity(entity_id)

    assert entity, "Kitsu entity not found."

    # TODO get entity type
    entity_type = "asset"

    if entity_type == "asset":
        return gazu.casting.get_asset_casting(entity)
    elif entity_type == "shot":
        return gazu.casting.get_shot_casting(entity)
    else:
        raise RuntimeError(f"{entity_type} is not a recognized entity type.")
