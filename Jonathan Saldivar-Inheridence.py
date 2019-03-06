class Item(object):
    def __init__(self, name):
        self.name = name


class Laser_Gun(Item):
    def __init__(self, name):
        super(Laser_Gun, self).__init__(name)
        self.damage = 150


class AK47(Item):
    def __init__(self, name):
        super(AK47, self).__init__(name)
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
        self.damage = 100


class Potion(Item):
    def __init__(self, name):
        super(Potion, self).__init__(name)
        self.heal = 50


class Big_Potion(Item):
    def __init__(self, name):
        super(Big_Potion, self).__init__(name)
        self.heal = 100


class Bandage(Item):
    def __init__(self, name):
        super(Bandage, self).__init__(name)
        self.heal = 25


class Backpack(Item):
    def __init__(self):
        super(Backpack, self).__init__(name)
        self.carry = 50