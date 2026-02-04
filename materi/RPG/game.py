from hero import Hero
from mage import Mage
from tank import Tank
from assasin import Assasin
from marksman import Marksman

alpha = Hero("alpha", 80, 100, 100, "Fighter")
valir = Mage("valir", 85, 100, 100)
belerick = Tank("belerick", 90, 150, 100)
assasin = Assasin("yi sun-shin", 95, 80, 100)
marksman = Marksman("claude", 88, 90, 100)


print(alpha)
print(valir)

valir.attack(alpha)
alpha.damaged(10)
valir.critical(alpha)
print(alpha)
print(valir)