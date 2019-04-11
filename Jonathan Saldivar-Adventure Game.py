# Classes
class Room(object):
    # This is the constructor
    def __init__(self, name, description, items, north=None, south=None, east=None, west=None, up=None, down=None):
        self.name = name
        self.description = description
        self.item = items
        self.north = north
        self.south = south
        self.east = east
        self.west = west
        self.up = up
        self.down = down


class Player(object):
    def __init__(self, starting_location):
        self.health = 200
        self.inventory = []
        self.current_location = starting_location

    def move(self, new_location):
        """This method moves a player to a new location

        :param new_location: The room object that we move to
        """
        self.current_location = new_location

    def find_room(self, direction):
        """This method takes a direction, and finds the variable of the room.

        :param direction: A String (all lowercase), with a cardinal direction
        :return: A room object if it exists, None if it does not
        """
        return getattr(self.current_location, direction)


# Items
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


class ShieldPotion(Potion):
    def __init__(self):
        super(ShieldPotion, self).__init__("Shield Potion")


class BigPotion(Item):
    def __init__(self, name):
        super(BigPotion, self).__init__(name)
        self.heal = 100

    def use(self):
        return self.heal


class BigShieldPotion(BigPotion):
    def __init__(self):
        super(BigShieldPotion, self).__init__("Big Shield Potion")


class ChestArmor(Item):
    def __init__(self, name):
        super(ChestArmor, self).__init__(name)
        self.protect = 25


class GoldenChestArmor(ChestArmor):
    def __init__(self):
        super(GoldenChestArmor, self).__init__("Golden Chest Armor")
        self.protect = 50


class DiamondChestArmor(ChestArmor):
    def __init__(self):
        super(DiamondChestArmor, self).__init__("Diamond Chest Armor")
        self.protect = 75


class Helmet(Item):
    def __init__(self, name):
        super(Helmet, self).__init__(name)
        self.protect = 25


class GoldenHelmet(Helmet):
    def __init__(self):
        super(GoldenHelmet, self).__init__("Golden Helmet")
        self.protect = 50


class DiamondHelmet(Helmet):
    def __init__(self):
        super(DiamondHelmet, self).__init__("Diamond Helmet")
        self.protect = 75


class Boots(Item):
    def __init__(self, name):
        super(Boots, self).__init__(name)
        self.protect = 25


class GoldBoots(Boots):
    def __init__(self):
        super(GoldBoots, self).__init__("Gold Boots")
        self.protect = 50


class DiamondBoots(Boots):
    def __init__(self):
        super(DiamondBoots, self).__init__("Diamond Boots")
        self.protect = 75


class Pants(Item):
    def __init__(self, name):
        super(Pants, self).__init__(name)
        self.protect = 50

    def protect(self):
        self.protect -= 1


class GoldPants(Pants):
    def __init__(self):
        super(GoldPants, self).__init__("Gold Pants")
        self.protect = 50


class DiamondPants(Pants):
    def __init__(self):
        super(DiamondPants, self).__init__("Diamond Pants")
        self.protect = 75


class Backpack(Item):
    def __init__(self, name):
        super(Backpack, self).__init__(name)
        self.carry = 50

    def carry(self):
        self.carry -= 1


class Character(object):
    def __init__(self, enemy, 200, sword, armor):
        self.name = orc
        self.health = 200
        self.weapon = sword
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


laser_gun = Item("A Laser Gun")
shotgun = Item("A shotgun")
assault_rifle = Item("An assault rifle")
sword = Item("A sword")
hatchet = Item("A hatchet")
pipe = Item("A pipe")
potion = Item("A potion")
big_potion = Item("A big potion")
chest_armor = Item("A chest armor")
helmet = Item("A helmet")
boots = Item("A pair of boots")
armor_pants = Item("A pair of armored pants")
backpack = Item("A backpack")

# Rooms
mansion = Room("A Mansion", "This is the room you are in.", Backpack("Backpack"), None, None, "right_hallway",
               "left_hallway", None, None)
right_hallway = Room("Right Hallway", "There is nothing but a big carpet here.", Sword("Sword"), None, "living_room",
                     None, "mansion", None, None)
left_hallway = Room("Left Hallway", "There is nothing but a big carpet here.", AssaultRifle("AssaultRifle"), None,
                    "kitchen", "mansion", None, None, None)
kitchen = Room("A Kitchen", "There is a lot of kitchen equipment in here.", ChestArmor("ChestArmor"), "left_hallway",
               "room", None, None, None, None)
living_room = Room("A Living Room", "There is nothing but a tv and a couch here.", Boots("boots"),
                   "right_hallway", None, None, "gaming_room", None, None)
gaming_room = Room("A Gaming Room", "There are a lot of games in here.", Pants("Pants"), None,
                   "garage", "living_room", None, None, None)
room = Room("A Room", "There is a bed and cabinets here.", Helmet("Helmet"), "kitchen", None, "dining_room", None,
            None, None)
garage = Room("A Garage", "There are two cars and gym equipment here.", Shotgun("Shotgun"), "gaming_room", "office",
              None, None, None, None)
dining_room = Room("A Dining Room", "There is a tv and couch her.", Axe("Axe"), None, "master_room", None,
                   "room",  None, None)
office = Room("A Office", "There are a lot of papers in here.", BigPotion("BigPotion"), "garage", "closet", None, None,
              None, None)
master_room = Room("A Master Room", "There is furniture, a bed, and tv in here.", LaserGun("LaserGun"), "dining_room",
                   None, None, "restroom", None, None)
closet = Room("A Closet", "There are a lot of clothes and shoes in here.", Pipe("Pipe"), None, None, None, "office",
              "right_attic", None)
restroom = Room("A Restroom", "There is a toilet and sink in here.", Potion("Potion"), None, None, "master_room", None,
                "left_attic", None)
right_attic = Room("A Attic", "Congratulations you have beat the game.", None, None, None, None, None, "closet")
left_attic = Room("A Attic", "Congratulations you have beat the game.", None, None, None, None, None, "restroom")

mansion.east = right_hallway
mansion.west = left_hallway
right_hallway.south = living_room
left_hallway.south = kitchen
living_room.west = gaming_room
living_room.north = right_hallway
kitchen.south = room
kitchen.north = left_hallway
gaming_room.south = garage
gaming_room.east = living_room
room.east = dining_room
room.north = kitchen
garage.south = office
garage.north = gaming_room
dining_room.south = master_room
dining_room.west = room
office.east = closet
office.north = garage
master_room.west = restroom
master_room.north = dining_room
closet.up = right_attic
closet.west = office
restroom.up = left_attic
restroom.east = master_room
right_attic.down = closet
left_attic.down = restroom

player = Player(mansion)

directions = ['north', 'south', 'east', 'west', 'up', 'down']
short_directions = ['n', 's', 'e', 'w', 'u', 'd']
playing = True

# Controller
while playing:
    print(player.current_location.name)
    print(player.current_location.description)
    if player.current_location.item is not None:
        print(player.current_location.item.name)
    print()

    if len(player.inventory) > 0:
        print("You have these items:")
        for item in player.inventory:
            print(item.name)
    command = input(">_")
    if command in short_directions:
        pos = short_directions.index(command)
        command = directions[pos]

    if command.lower() in ['q', 'quit', 'exit']:
        playing = False
    elif command in directions:
        try:
            next_room = player.find_room(command)
            if next_room is None:
                raise KeyError
            player.move(next_room)
        except KeyError:
            print("I can't go that way")

    elif "take" in command.lower():
        if player.current_location.item is not None:
            item_name = command[5:]
            found_item = None
            if player.current_location.item.name.lower() == item_name.lower():
                item_found = player.current_location.item

            if found_item is not None:
                player.inventory.append(found_item)
                player.current_location.item = None
        else:
            print("There are no items in this room")

    elif "drop" in command.lower():
        if player.current_location.items is None:
            item_name = command[5:]
            drop_item = None
            for item in player.inventory:
                if item.name.lower() == item_name.lower():
                    drop_item = item

            if drop_item is not None:
                player.current_location.item = drop_item
                player.inventory.remove(drop_item)

        else:
            print("There's already an item here")

    else:
        print("Command not recognized")
