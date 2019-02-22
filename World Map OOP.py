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

# These are the instances of the rooms (Instantiation)


# Option 1 - Use the Variables, but fix later
mansion = Room("A Mansion", "This is the room you are in.")
right_hallway = Room("Right Hallway", "There is nothing but a big carpet here.")
left_hallway = Room("Left Hallway", "There is nothing but a big carpet here.")
kitchen = Room("A Kitchen", "There is a lot of kitchen equipment in here.")
living_room = Room("A Living Room", "There is nothing but a tv and a couch here.")
gaming_room = Room("A Gaming Room", "There are a lot of games in here.")
room = Room("A Room", "There is a bed and cabinets here.")
garage = Room("A Garage", "There is are two cars and gym equipment here.")
dining_room = Room("A Dining Room", "There is a tv and couch her.")
office = Room("A Office", "There are a lot of papers in here.")
master_room = Room("A Master Room", "There is furniture, a bed, and tv in here.")
closet = Room("A Closet", "There are a lot of clothes and shoes in here.")
restroom = Room("A Restroom", "There is a toilet and sink in here.")
right_attic = Room("A Attic", "There are a lot of boxes up here.")
left_attic = Room("A Attic", "There are a lot of boxes up here.")

mansion.east = right_hallway
mansion.west = left_hallway
right_hallway.south = living_room
left_hallway.south = kitchen
living_room.west = gaming_room
kitchen.south = room
gaming_room.south = garage
room.east = dining_room
garage.south = office
dining_room.south = master_room
office.east = closet
master_room.west = restroom
closet.up = right_attic
restroom.up = left_attic
