# definisikan class nama class
class Cat:
    # masih class kosongan
    # _init_ = constructor = yg pertama kali di akses
    # definisikan atributnya di dalam constructor
    def __init__(self, color, height, width):
        self.color = color
        self.height = height
        self.width = width

# buat objek dari class Cat
garfield = Cat("oren", 25, 15)
tom = Cat("abu-abu", 30, 20)
# cek objek di memory kita, muncul address 0x1*****
print("Obj garfield:", garfield)
print("Obj tom:", tom)
#  panggil nama atribut dari objek
print(f"warna garfield: {garfield.color}")
print(f"tinggi garfield: {garfield.height}")
print(f"lebar garfield: {garfield.width}")
print(f"warna tom: {tom.color}")
print(f"tinggi tom: {tom.height}")
print(f"lebar tom: {tom.width}")