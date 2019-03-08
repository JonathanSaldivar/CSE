class Item(object):
    def __init__(self, name):
        self.name = name


class LaserGun(Item):
    def __init__(self, name):
        super(LaserGun, self).__init__(name)
        self.damage = 150


class BlueLaser(LaserGun):
    def __init__(self):
        super(BlueLaser, self).__init__("BlueLaser")


class Shotgun(Item):
    def __init__(self, name):
        super(Shotgun, self).__init__(name)
        self.damage = 200


class DoubleBarrel(Shotgun):
    def __init__(self):
        super(DoubleBarrel, self).__init__("DoubleBarrel")


class AssaultRifle(Item):
    def __init__(self, name):
        super(AssaultRifle, self).__init__(name)
        self.damage = 150


class Sword(Item):
    def __init__(self, name):
        super(Sword, self).__init__(name)
        self.damage = 100


class Hatchet(Item):
    def __init__(self, name):
        super(Hatchet, self).__init__(name)
        self.damage = 100


class Wrench(Item):
    def __init__(self, name):
        super(Wrench, self).__init__(name)
        self.damage = 75


class Potion(Item):
    def __init__(self, name):
        super(Potion, self).__init__(name)
        self.heal = 50


class BigPotion(Item):
    def __init__(self, name):
        super(BigPotion, self).__init__(name)
        self.heal = 100


class ChestArmor(Item):
    def __init__(self, name):
        super(ChestArmor, self).__init__(name)
        self.protect = 50


class Helmet(Item):
    def __init__(self, name):
        super(Helmet, self).__init__(name)
        self.protect = 50


class Boots(Item):
    def __init__(self, name):
        super(Boots, self).__init__(name)
        self.protect = 50


class Pants(Item):
    def __init__(self, name):
        super(Pants, self).__init__(name)
        self.protect = 50


class Backpack(Item):
    def __init__(self, name):
        super(Backpack, self).__init__(name)
        self.carry = 50


laser_gun = Item("A Laser Gun")
shotgun = Item("A shotgun")
assault_rifle = Item("An assault rifle")
sword = Item("A sword")
hatchet = Item("A hatchet")
wrench = Item("A wrench")
potion = Item("A potion")
big_potion = Item("A big potion")
chest_armor = Item("A chest armor")
helmet = Item("A helmet")
boots = Item("A pair of boots")
armor_pants = Item("A pair of armored pants")
backpack = Item("A backpack")
