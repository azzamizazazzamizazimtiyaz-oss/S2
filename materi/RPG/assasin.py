from hero import Hero
from monster import Monster

class Assasin(Hero):
    def init(self, name: str, hp: int):
        super().init(name, hp, job="Assasin")

    def ultimate(self, enemy: Monster):
        dmg = 130
        print(f"{self.name} menggunakan ultimate skill: SHADOW KILL! | {dmg} DMG")
        enemy.take_damage(dmg)