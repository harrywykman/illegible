import tcod as libtcod

import game_messages


class Fighter:
    def __init__(self, hp, defense, power, xp=0):
        self.max_hp = hp
        self.hp = hp
        self.defense = defense
        self.power = power
        self.xp = xp

    def take_damage(self, amount):
        results = []

        self.hp -= amount

        if self.hp <= 0:
            results.append({"dead": self.owner, "xp": self.xp})

        return results

    def heal(self, amount):
        self.hp += amount

        if self.hp > self.max_hp:
            self.hp = self.max_hp

    def attack(self, target):
        results = []

        damage = self.power - target.fighter.defense

        if damage > 0:
            results.append(
                {
                    "message": game_messages.Message(
                        "{0} attacks {1} for {2} hit points.".format(
                            self.owner.name.capitalize(), target.name, str(damage)
                        ),
                        libtcod.white,
                    )
                }
            )
            results.extend(target.fighter.take_damage(damage))
        else:
            results.append(
                {
                    "message": game_messages.Message(
                        "{0} attacks {1} but does no damage.".format(
                            self.owner.name.capitalize(), target.name
                        ),
                        libtcod.white,
                    )
                }
            )

        return results
