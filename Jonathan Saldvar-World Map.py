world_map = {
    'MANSION': {
        "NAME": "A Mansion",
        "DESCRIPTION": "This is the room you are in.",
        "PATHS": {
            'EAST': "RIGHT_HALLWAY",
            'WEST': "LEFT_HALLWAY"
        }
    },
    'RIGHT_HALLWAY': {
        'NAME': "Right Hallway",
        'DESCRIPTION': "There is nothing but a big carpet here.",
        'PATHS': {
            'SOUTH': 'LIVING_ROOM'
        }
    },
    'LEFT_HALLWAY': {
        'NAME': "Left Hallway",
        'DESCRIPTION': "There is nothing but a big carpet here.",
        'PATHS': {
            'SOUTH': 'KITCHEN',
        }
    },
    'KITCHEN': {
        'NAME': "A Kitchen",
        'DESCRIPTION': "There are a lot of spoons, forks, and knifes here.",
        'PATHS': {
            'SOUTH': 'ROOM',
            'NORTH': 'LEFT_HALLWAY'
        }
    },
    'LIVING_ROOM': {
        'NAME': "A Living Room",
        'DESCRIPTION': "There is nothing but a tv and a couch here.",
        'PATHS': {
            'WEST': 'GAMING_ROOM',
            'NORTH': 'RIGHT_HALLWAY'
        }
    },
    'ROOM': {
        'NAME': "A Room",
        'DESCRIPTION': "There is a bed and cabinets here.",
        'PATHS': {
            'EAST': 'DINING_ROOM',
            'NORTH': 'KITCHEN'
        }
    },
    'GAMING ROOM': {
        'NAME': "A Gaming Room",
        'DESCRIPTION': "There are a lot of games in here.",
        'PATHS': {
            'SOUTH': 'GARAGE',
            'EAST': 'LIVING_ROOM'
        }
    },
    'DINING_ROOM': {
        'NAME': "A Dining Room",
        'DESCRIPTION': "There is a tv and couch her.",
        'PATHS': {
            'SOUTH': 'RESTROOM',
            'WEST': 'ROOM'
        }
    },
    'GARAGE': {
        'NAME': "A Garage",
        'DESCRIPTION': "There is are two cars and gym equipment here.",
        'PATHS': {
            'SOUTH': 'OFFICE',
            'NORTH': 'GAMING_ROOM'
        }
    },
    'OFFICE': {
        'NAME': "A OFFICE",
        'DESCRIPTION': "There are a lot of papers in here.",
        'PATHS': {
            'EAST': 'CLOSET',
            'NORTH': 'GARAGE'
        }
    },
    'RESTROOM': {
        'NAME': "A Restroom",
        'DESCRIPTION': "There are a lot of restroom equipment in here.",
        'PATHS': {
            'WEST': '',
            'NORTH': 'DINING_ROOM'
        }
    },
    'CLOSET': {
        'NAME': "A Closet",
        'DESCRIPTION': "There are a lot of clothes and shoes in here.",
        'PATHS': {
            'SOUTH': '',
            'WEST': 'OFFICE'
        }
    },
}

# Other Variables
directions = ["NORTH", "SOUTH", "EAST", "WEST", "UP", "DOWN"]
current_node = world_map["MANSION"]  # This is your current location
playing = True

# Controller
while playing:
    print(current_node['NAME'])

    command = input(">_")
    if command.lower() in ['q', 'quit', 'exit']:
        playing = False
    elif command in directions:
        try:
            room_name = current_node["PATHS"][command]
            current_node = world_map[room_name]
        except KeyError:
            print("I can't go that way")
    else:
        print("Command not recognized.")
