from hero import Hero
from monster import Monster

class Archer(Hero):
    def init(self, name: str, hp: int):
        super().init(name, hp, job="Archer")

    def ultimate(self, enemy: Monster):
        dmg = 110
        print(f"{self.name} menggunakan ultimate skill: WIND ARROW! | {dmg} DMG")
        enemy.take_damage(dmg)