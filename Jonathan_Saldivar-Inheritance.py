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
        print("You have %d lasers left" % self.usage)


class BlueLaser(LaserGun):
    def __init__(self):
        super(BlueLaser, self).__init__("Blue Laser")


class RedLaser(LaserGun):
    def __init__(self):
        super(RedLaser, self).__init__("Red Laser")


class Shotgun(Item):
    def __init__(self, name):
        super(Shotgun, self).__init__(name)
        self.damage = 200
        self.usage = 50

    def shoot(self):
        self.usage -= 1
        print("You have %d shells left" % self.usage)


class DoubleBarrel(Shotgun):
    def __init__(self):
        super(DoubleBarrel, self).__init__("Double Barrel")


class CombatShotgun(Shotgun):
    def __init__(self):
        super(CombatShotgun, self).__init__("Combat Shotgun")


class AssaultRifle(Item):
    def __init__(self, name):
        super(AssaultRifle, self).__init__(name)
        self.damage = 150
        self.usage = 100

    def shoot(self):
        self.usage -= 1
        print("You have %d bullets left" % self.usage)


class M16(AssaultRifle):
    def __init__(self):
        super(M16, self).__init__("M16")


class AK47(AssaultRifle):
    def __init__(self):
        super(AK47, self).__init__("AK47")


class Sword(Item):
    def __init__(self, name):
        super(Sword, self).__init__(name)
        self.damage = 100
        self.usage = 20

    def swing(self):
        self.usage -= 1
        print("You have %d swings left" % self.usage)


class LongSword(Sword):
    def __init__(self):
        super(LongSword, self).__init__("Long Sword")


class BroadSword(Sword):
    def __init__(self):
        super(BroadSword, self).__init__("Broad Sword")


class Axe(Item):
    def __init__(self, name):
        super(Axe, self).__init__(name)
        self.damage = 100
        self.usage = 20

    def swing(self):
        self.usage -= 1
        print("You have %d swings left" % self.usage)


class BattleAxe(Axe):
    def __init__(self):
        super(BattleAxe, self).__init__("Battle Axe")


class TacticalAxe(Axe):
    def __init__(self):
        super(TacticalAxe, self).__init__("Tactical Axe")


class Pipe(Item):
    def __init__(self, name):
        super(Pipe, self).__init__(name)
        self.damage = 75
        self.usage = 20

    def swing(self):
        self.usage -= 1
        print("You have %d swings left" % self.usage)


class CopperPipe(Pipe):
    def __init__(self):
        super(CopperPipe, self).__init__("Copper Pipe")


class MetalPipe(Pipe):
    def __init__(self):
        super(MetalPipe, self).__init__("Metal Pipe")


class Potion(Item):
    def __init__(self, name):
        super(Potion, self).__init__(name)
        self.heal = 50

    def use(self):
        return self.heal
    print("You have regained 50 of your health")


class ShieldPotion(Potion):
    def __init__(self):
        super(ShieldPotion, self).__init__("Shield Potion")


class BigPotion(Item):
    def __init__(self, name):
        super(BigPotion, self).__init__(name)
        self.heal = 100

    def use(self):
        return self.heal
    print("You have regained 100 of your health")


class BigShieldPotion(BigPotion):
    def __init__(self):
        super(BigShieldPotion, self).__init__("Big Shield Potion")


class ChestArmor(Item):
    def __init__(self, name):
        super(ChestArmor, self).__init__(name)
        self.protect = 50


class GoldenChestArmor(ChestArmor):
    def __init__(self):
class Helmet(Item):
    def __init__(self, name):
        super(Helmet, self).__init__(name)
        self.protect = 50

    def protects(self):
        self.protect -= 1


class ArmoredHelmet(Helmet):
    def __init__(self):
        super(ArmoredHelmet, self).__init__("Armored Helmet")


class Boots(Item):
    def __init__(self, name):
        super(Boots, self).__init__(name)
        self.protect = 50

    def protects(self):
        self.protect -= 1


class ArmoredBoots(Boots):
    def __init__(self):
        super(ArmoredBoots, self).__init__("Armored Boots")


class Pants(Item):
    def __init__(self, name):
        super(Pants, self).__init__(name)
        self.protect = 50

    def protect(self):
        self.protect -= 1


class ArmoredPants(Pants):
    def __init__(self):
        super(ArmoredPants, self).__init__("Armored Pants")


class Backpack(Item):
    def __init__(self, name):
        super(Backpack, self).__init__(name)
        self.carry = 50

    def carry(self):
        self.carry -= 1
        print("You carried an item")


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


class Item(object):
    def __init__(self, name):
        self.name = name


class Weapon(Item):
    def __init__(self, name, damage):
        super(Weapon, self).__init__(name)
        self.damage = damage


class Armor(Item):
    def __init__(self, name, armor_amt):
        super(Armor, self).__init__(name)
        self.armor_amt = armor_amt


class Character(object):
    def __init__(self, name, health, weapon, armor):
        self.name = name
        self.health = health
        self.weapon = weapon
        self.armor = armor

    def take_damage(self, damage):
        if damage < self.armor.armor_amt:
            print("No damage is done because of some FABULOUS armor!")
        else:
            self.health -= damage - self.armor.armor_amt
            if self.health < 0:
                self.health = 0
                print("%s has fallen" % self.name)
        print("%s has %d health left" % (self.name, self.health))

    def attack(self, target):
        print("%s attacks %s for %d damage" %
              (self.name, target.name, self.weapon.damage))
        target.take_damage(self.weapon.damage)
# Items


Sword = Weapon("Sword", 10)
canoe = Weapon("Canoe", 84)
wiebe_armor = Armor("Armor of the Gods", 100000000000000000)

# Characters
orc = Character("Orc", 100, sword, Armor("Generic Armor", 2))
Wiebe = Character("Wiebe", 1000000000000, canoe, wiebe_armor)

orc.attack(Wiebe)
Wiebe.attack(orc)
Wiebe.attack(orc)
