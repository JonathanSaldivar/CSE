class Item(object):
    def __init__(self, name):
        self.name = name


class LaserGun(Item):
    def __init__(self, name):
        super(LaserGun, self).__init__(name)
        self.damage = 150
        self.usage = 100

    def shoot(self):
        self.usage -= 1
        print("You use a bullet.")
        print('This gun does 150 damage')


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


class M16(AssaultRifle):
    def __init__(self):
        super(M16, self).__init__("M16")


class Sword(Item):
    def __init__(self, name):
        super(Sword, self).__init__(name)
        self.damage = 100


class LongSword(Sword):
    def __init__(self):
        super(LongSword, self).__init__("LongSword")


class Hatchet(Item):
    def __init__(self, name):
        super(Hatchet, self).__init__(name)
        self.damage = 100


class BattleAxe(Hatchet):
    def __init__(self):
        super(BattleAxe, self).__init__("BattleAxe")


class Pipe(Item):
    def __init__(self, name):
        super(Pipe, self).__init__(name)
        self.damage = 75


class CopperPipe(Pipe):
    def __init__(self):
        super(CopperPipe, self).__init__("Copper Pipe")


class Potion(Item):
    def __init__(self, name):
        super(Potion, self).__init__(name)
        self.heal = 50


class ShieldPotion(Potion):
    def __init__(self):
        super(ShieldPotion, self).__init__("Shield Potion")


class BigPotion(Item):
    def __init__(self, name):
        super(BigPotion, self).__init__(name)
        self.heal = 100


class BigShieldPotion(BigPotion):
    def __init__(self):
        super(BigShieldPotion, self).__init__("Big Shield Potion")


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
