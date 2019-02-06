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
            'SOUTH': 'KITCHEN'
        }
    },
    'KITCHEN': {
        'NAME': "A Kitchen",
        'DESCRIPTION': "There are a lot of spoons, forks, and knifes here",
        'PATHS': {
            'SOUTH': 'ROOM'
        }
    },
    'LIVING_ROOM': {
        'NAME': "A Living Room",
        'DESCRIPTION': "There is nothing but a tv and a couch here.",
        'PATHS': {
            'WEST': 'DOOR'
        }
    },
    'ROOM': {
        'NAME': "A Room",
        'DESCRIPTION': "There is a bed and cabinets here",
        'PATHS': {
            'SOUTH': ''
        }
    },
    'DOOR': {
        'NAME': "A Door",
        'DESCRIPTION': "There is a window",
        'PATHS': {
            'SOUTH': ''
        }
    }
}

# Other Variables
directions = ["NORTH", "SOUTH", "EAST", "WEST", "UP", "DOWN"]
current_node = world_map["R19A"]  # This is your current location
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
