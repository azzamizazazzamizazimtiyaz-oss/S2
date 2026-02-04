from hero import Hero # panggil class Hero.

class Marksman(Hero):
    def __init__(self, name, level, hp, mana):
        super().__init__(name, level, hp, mana, role="marksman")
