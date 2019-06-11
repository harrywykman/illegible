import tcod as libtcod

from game_states import GameStates
import render_functions as rfs
import game_messages


def kill_player(player):
    player.char = '%'
    player.color = libtcod.dark_red

    return game_messages.Message('You died!', libtcod.red), GameStates.PLAYER_DEAD


def kill_monster(monster):
    death_message = death_message = game_messages.Message('{0} is dead!'.format(monster.name.capitalize()), libtcod.orange)

    monster.char = '%'
    monster.color = libtcod.dark_red
    monster.blocks = False
    monster.fighter = None
    monster.ai = None
    monster.name = 'remains of ' + monster.name
    monster.render_order = rfs.RenderOrder.CORPSE

    return death_message
