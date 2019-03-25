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
            'SOUTH': 'LIVING_ROOM',
            'WEST': 'MANSION'
        }
    },
    'LEFT_HALLWAY': {
        'NAME': "Left Hallway",
        'DESCRIPTION': "There is nothing but a big carpet here.",
        'PATHS': {
            'SOUTH': 'KITCHEN',
            'EAST': 'MANSION'
        }
    },
    'KITCHEN': {
        'NAME': "A Kitchen",
        'DESCRIPTION': "There is a lot of kitchen equipment in here.",
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
    'GAMING_ROOM': {
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
            'SOUTH': 'MASTER_ROOM',
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
    'MASTER_ROOM': {
        'NAME': "A Master Room",
        'DESCRIPTION': "There is furniture, a bed, and tv in here.",
        'PATHS': {
            'WEST': 'RESTROOM',
            'NORTH': 'DINING_ROOM'
        }
    },
    'CLOSET': {
        'NAME': "A Closet",
        'DESCRIPTION': "There are a lot of clothes and shoes in here.",
        'PATHS': {
            'UP': 'RIGHT_ATTIC',
            'WEST': 'OFFICE'
        }
    },
    'RESTROOM': {
        'NAME': "A Restroom",
        'DESCRIPTION': "There is a toilet and sink in here.",
        'PATHS': {
            'UP': 'LEFT_ATTIC',
            'EAST': 'MASTER_ROOM'
        }
    },
    'RIGHT_ATTIC': {
        'NAME': "A Attic",
        'DESCRIPTION': "There are a lot of boxes up here.",
        'PATHS': {
            'DOWN': 'CLOSET'
        }
    },
    'LEFT_ATTIC': {
        'NAME': "Attic Right",
        'DESCRIPTION': "There are a lot of boxes up here.",
        'PATHS': {
            'DOWN': 'RESTROOM'
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
