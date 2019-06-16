import tcod as libtcod

import game_messages


def heal(*args, **kwargs):
    entity = args[0]
    amount = kwargs.get("amount")

    results = []

    if entity.fighter.hp == entity.fighter.max_hp:
        results.append(
            {
                "consumed": False,
                "message": game_messages.Message(
                    "You are already at full health", libtcod.yellow
                ),
            }
        )
    else:
        entity.fighter.heal(amount)
        results.append(
            {
                "consumed": True,
                "message": game_messages.Message(
                    "Your wounds start to feel better!", libtcod.green
                ),
            }
        )

    return results
