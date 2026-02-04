from hero import Hero # panggil class Hero.

class Assasin(Hero):
    def __init__(self, name, level, hp, mana):
        super().__init__(name, level, hp, mana, role="Assasin")


    def critical(self, target):
        dmg = 50
        print(f"🔥 {self.name} menggunakan HELLFIRE METEOR")
        print(f"👺 {target.name} terkena critical {dmg} DMG!")
        self.attack(target)
        target.damaged(dmg)

    def cast_spell(self, target):
        dmg = 10
        print(f"🔥 {self.name} menggunakan magic attack")
        self.attack(target)
        target.damaged(dmg)