class Hero:
    def __init__(self, name, role, hp, hero_type="hero"):
        self.name = name
        self.role = role
        self.max_hp = hp
        self.hp = hp
        self.type = hero_type
        self.rage = False

        print(f"✨ {self.name} memasuki lane offdone!")

    def is_alive(self):
        return self.hp > 0
    
    def is_dead(self):
        return self.hp <= 0
    
    def __str__(self):
        status = "🟢 HIDUP" if self.is_alive() else "💀 MATI"
        return f"[{self.type.upper()}] {self.name} | Role: {self.role} | HP: {self.hp}/{self.max_hp} | STATUS: {status}"

    def attack(self, enemy, damage):
        if not self.is_alive():
            print(f"💀 {self.name} sudah mati dan tidak bisa menyerang!")
            return
        
        if damage <= 0:
            print("❌ Damage tidak valid!")
            return
        
        # Boss rage mode
        if self.type == "boss" and self.hp <= self.max_hp / 2 and not self.rage:
            self.rage = True
            print("😈 BOSS MASUK RAGE MODE!")

        if self.type == "boss" and self.rage:
            damage *= 2
            print(f"🔥 CRITICAL HIT! Damage menjadi {damage}")

        print(f"⚔️ {self.name} menyerang {enemy.name} sebesar {damage} damage!")
        enemy.take_damage(damage)

    def take_damage(self, damage):
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0
        
        print(f"❤️ {self.name} HP sekarang: {self.hp}/{self.max_hp}")

        if self.is_dead():
            print(f"☠️ {self.name} telah gugur!")

    def heal(self):
        if not self.is_alive():
            print(f"💀 {self.name} sudah mati dan tidak bisa heal!")
            return
        
        if self.role == "Tank":
            amount = 20
        elif self.role == "Mage":
            amount = 30
        elif self.role == "Marksman":
            amount = 25
        else:
            amount = 15

        self.hp += amount
        if self.hp > self.max_hp:
            self.hp = self.max_hp

        print(f"💚 {self.name} heal +{amount} HP ({self.hp}/{self.max_hp})")


moskov = Hero("Moskov", "Marksman", 100)
julian = Hero("Julian", "hayper", 100)
belerick = Hero("Belerick", "Tank", 100)
yu_zhong = Hero("Yu zhong", "Fighter", 100)
valir = Hero("Valir", "Mage", 100)   
    
print("\n--- MUSUH MUNCUL ---")
Turtle = Hero("Turtle", "Monster", 100, "normal")

print("\n--- PERTARUNGAN DIMULAI ---")
belerick.attack(Turtle, 25)
moskov.attack(Turtle, 50)
julian.attack(Turtle, 60)

print("\n--- LORD BOSS TELAH MUNCUL ---")
Lord = Hero("Lord", "Boss", 1000, "boss")

print("\n--- PERTARUNGAN LAWAN LORD DIMULAI ---")
belerick.attack(Lord, 100)
moskov.attack(Lord, 300)
valir.attack(Lord, 100)
yu_zhong.attack(Lord, 200)
julian.attack(Lord, 350)