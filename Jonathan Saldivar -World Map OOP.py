class Room(object):
    # This is the constructor
    def __init__(self, name, description, north=None, south=None, east=None, west=None, up=None, down=None):
        self.name = name
        self.north = north
        self.south = south
        self.east = east
        self.west = west
        self.description = description
        self.up = up
        self.down = down


class Player(object):
    def __init__(self, starting_location):
        self.health = 100
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


# These are the instances of the rooms (Instantiation)


# Option 1 - Use the Variables, but fix later
mansion = Room("A Mansion", "This is the room you are in.", None, None, "right_hallway",
               "left_hallway", None, None)
right_hallway = Room("Right Hallway", "There is nothing but a big carpet here.", None, "living_room",
                     None, "mansion", None, None)
left_hallway = Room("Left Hallway", "There is nothing but a big carpet here.", None,
                    "kitchen", "mansion", None, None, None)
kitchen = Room("A Kitchen", "There is a lot of kitchen equipment in here.", "left_hallway",
               "room", None, None, None, None)
living_room = Room("A Living Room", "There is nothing but a tv and a couch here.",
                   "right_hallway", None, None, "gaming_room", None, None)
gaming_room = Room("A Gaming Room", "There are a lot of games in here.", None,
                   "garage", "living_room", None, None, None)
room = Room("A Room", "There is a bed and cabinets here.", "kitchen", None, "dining_room", None,
            None, None)
garage = Room("A Garage", "There are two cars and gym equipment here.", "gaming_room", "office",
              None, None, None, None)
dining_room = Room("A Dining Room", "There is a tv and couch her.", None, "master_room", None,
                   "room",  None, None)
office = Room("A Office", "There are a lot of papers in here.", "garage", "closet", None, None,
              None, None)
master_room = Room("A Master Room", "There is furniture, a bed, and tv in here.", "dining_room",
                   None, None, "restroom", None, None)
closet = Room("A Closet", "There are a lot of clothes and shoes in here.", None, None, None, "office",
              "right_attic", None)
restroom = Room("A Restroom", "There is a toilet and sink in here.", None, None, "master_room", None,
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

directions = ['north', 'south' 'east', 'west', 'up', 'down']
playing = True

# Controller
while playing:
    print(player.current_location.name)

    command = input(">_")
    if command.lower() in ['q', 'quit', 'exit']:
        playing = False
    elif command in directions:
        try:
            next_room = player.find_room(command)
            player.find_room(command)
        except KeyError:
            print("I can't go that way")
    else:
        print("Command not recognized.")
