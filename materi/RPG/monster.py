class Monster:
     def __init__(self, name, level, hp, mana, role):
        self.name = name
        self.level = level
        self.hp = hp
        self.mana = mana
        print(f"✨ Monster {self.name} telah di-summon!")

    def __str__(self):
        status = "🟢 HIDUP" 
        if self.hp == 0:
            status = "💀 MATI"
            
        return f"[Monster] {self.name}| HP: {self.hp} | STATUS: {status}"