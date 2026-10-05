# define rooms and items
#All Items
import time
import copy
from IPython.display import display, Image


couch = {
    "name": "couch",
    "type": "furniture",
}

piano = {
    "name": "piano",
    "type": "furniture",
}

dresser = {
    "name": "dresser",
    "type": "furniture",
}

queen_bed = {
    "name": "queen bed",
    "type": "furniture",
}

double_bed = {
    "name": "double bed",
    "type": "furniture",
}

dining_table = {
    "name": "dining table",
    "type": "furniture",
}

fridge = {
    "name": "fridge",
    "type": "furniture",
    "code": "91526"
}

kitchen_cabinet = {
    "name": "cabinet",
    "type": "furniture",
}

kitchen_sink = {
    "name": "kitchen sink",
    "type": "furniture",
}

trash_can = {
    "name": "trash can",
    "type": "furniture",
}

bedside_table = {
    "name": "bedside table",
    "type": "furniture",
}

sofa = {
    "name": "sofa",
    "type": "furniture",
}

coffee_table = {
    "name": "coffee table",
    "type": "furniture",
}

shelf = {
    "name": "shelf",
    "type": "furniture",
}

toolbox = {
    "name": "toolbox",
    "type": "furniture",
}

#All Doors

door_a = {
    "name": "door a",
    "type": "door",
}

door_b = {
    "name": "door b",
    "type": "door",
}

door_c = {
    "name": "door c",
    "type": "door",
}

door_d = {
    "name": "door d",
    "type": "door",
}

door_e = {
    "name": "door e",
    "type": "door",
}

door_f = {
    "name": "door f",
    "type": "door",
}

door_g = {
    "name": "door g",
    "type": "lock",
    "code": "91526"
}

window = {
    "name": "window",
    "type": "door",
}

#All Keys and Items

key_a = {
    "name": "key for door a",
    "type": "key",
    "target": door_a,
}

key_b = {
    "name": "key for door b",
    "type": "key",
    "target": door_b,
}

key_c = {
    "name": "key for door c",
    "type": "key",
    "target": door_c,
}

key_d = {
    "name": "key for door d",
    "type": "key",
    "target": door_d,
}

key_e = {
    "name": "key for door e",
    "type": "key",
    "target": door_e,
}

aa_battery_1 = {
    "name": "AA+ Battery",
    "type": "key",
    "target": "flashlight",
}

aa_battery_2 = {
    "name": "AA+ Battery",
    "type": "key",
    "target": "flashlight",
}

flashlight = {
    "name": "flashlight",
    "type": "furniture",
    "target": None,
}

hammer = {
    "name": "hammer",
    "type": "key",
    "target": window,
}


#All Rooms

game_room = {
    "name": "game room",
    "type": "room",
    "image": "game_room.jfif",
}

bedroom_1 = {
    "name": "bedroom 1",
    "type": "room",
    "image": "bedroom_1.jfif",
}

bedroom_2 = {
    "name": "bedroom 2",
    "type": "room",
    "image": "bedroom_2.jfif",
}

living_room = {
    "name": "living room",
    "type": "room",
    "description": "Remote on the coffee table but no TV? So weird...",
    "image": "living_room.jfif",
}

kitchen = {
    "name": "kitchen",
    "type": "room",
    "description": "Hmm...there's postcard on the fridge and the sink is making a strange noise",
    "image": "kitchen.jfif",
}

storage_room = {
    "name": "storage room",
    "type": "room",
    "description": "Lets see if I can find something to light up the stairs",
    "image": "storage_room.jfif",
}

stairs = {
    "name": "stairs",
    "type": "room",
    "description": "What a dark place to be in, I can barely see",
}

basement = {
    "name": "basement",
    "type": "room",
    "description": "There's a window maybe I can get out of here",
    "image": "basement.jpg",
}

outside = {
    "name": "outside",
    "image": "the_end.jpg"
}

all_rooms = [game_room, bedroom_1, bedroom_2, living_room, kitchen, storage_room, stairs, basement, outside]

all_doors = [door_a, door_b, door_c, door_d, door_e, door_f, door_g, window]

# define which items/rooms are related

INIT_OBJECT_RELATIONS = {
    #Items
    "piano": [key_a],
    "queen bed": [key_b],
    "dresser": [key_d],
    "double bed": [key_c],
    "kitchen sink": [key_e],
    "bedside table": [aa_battery_1],
    "coffee table": [aa_battery_2],
    "shelf": [flashlight],
    "toolbox": [hammer],

    #Rooms
    "game room": [couch, piano, door_a],
    "bedroom 1": [queen_bed, bedside_table, door_a, door_b, door_c],
    "bedroom 2": [double_bed, dresser, door_b],
    "living room": [dining_table, coffee_table, sofa, door_c, door_d, door_f],
    "kitchen": [door_d, door_e, fridge, kitchen_cabinet, kitchen_sink, trash_can],
    "storage room": [door_e, shelf, toolbox],
    "stairs": [door_f, door_g],
    "basement": [door_g, window],
    "outside": [window],
    
    #Doors & Locks
    "door a": [game_room, bedroom_1],
    "door b": [bedroom_1, bedroom_2],
    "door c": [living_room, bedroom_1],
    "door d": [living_room, kitchen],
    "door e": [kitchen, storage_room],
    "door f": [living_room, stairs],
    "door g": [stairs, basement],
    "basement window" : [basement, outside]
}

colors = {
    "green": "\033[1;38;5;46m",
    "yellow": "\033[1;38;5;226m",
    "red": "\033[1;38;5;196m",
    "bold": "\033[1m",
    "cyan": "\033[1;96m",
    "reset": "\033[0m"
}

# define game state. Do not directly change this dict. 
# Instead, when a new game starts, make a copy of this
# dict and use the copy to store gameplay state. This 
# way you can replay the game multiple times.

INIT_GAME_STATE = {
    "current_room": game_room,
    "items_collected": [],
    "target_room": outside,
    "start_time": None,
    "time_limit": 450,
    "has_light": False
}



def linebreak():
    """
    Print a line break
    """
    print("\n\n")

def start_game():
    global game_state

    game_state = INIT_GAME_STATE.copy()

    game_state["items_collected"] = []
    
    game_state["start_time"] = time.time()

    object_relations = copy.deepcopy(INIT_OBJECT_RELATIONS)

    for room in all_rooms:
        if "image_shown" in room:
            del room["image_shown"]
        if "description_shown" in room:
            del room["description_shown"]
    """
    Start the game
    """
    print(colors["yellow"] + "You wake up on a couch and find yourself in a strange house with no windows which you have never been to before. You don't remember why you are here and what had happened before. You have a timer on your wrist with a countdown, you need to get out, NOW!" + colors["reset"])
    play_room(game_state["current_room"])

def play_room(room):
    """
    Play a room. First check if the room being played is the target room.
    If it is, the game will end with success. Otherwise, let player either 
    explore (list all items in this room) or examine an item found here.
    """
        
    game_state["current_room"] = room
    if not check_timer(show_time=False): #If time runs out, game over
        return
    if(game_state["current_room"] == game_state["target_room"]):
        print(colors["yellow"] + "'a massive explosion collapses the entire house behind you!'" + colors["reset"] )
        print("Congrats! You escaped just in time!")
        try: # Displays the final winning image
            display(Image(filename=room["image"], format="jpeg"))
            room["image_shown"] = True
        except FileNotFoundError:
            print(colors["red"] + "Could not find image." + colors["reset"])
    else:
        print("You are now in " + room["name"])

        #Descriptions helps the player know what to do in each room by retrieving the description from the dictionaries
        #It adds the image_shown key to each room prevent from keeping displaying the description if player goes back to the same room
        if "description" in room and "description_shown" not in room:
                print(colors["cyan"] + room["description"] + colors["reset"])
                room["description_shown"] = True              
        
        # Displays the image of a room when player enters for the first time in a room
        #It adds the image_shown key to each room prevent from keeping displaying the image if player goes back to the same room
        if "image" in room and "image_shown" not in room:
            try:
                display(Image(filename=room["image"], format="jpeg"))
                room["image_shown"] = True
            except FileNotFoundError:
                print(colors["red"] + "Could not find image." + colors["reset"])
                
        #Instead of asking to always type "explore" or "examine" a change to the code was made
        #so that the user has to type "1" for "explore", "2" for "examine and "3" to check timer, making more interactive
        print("What would you like to do? " + colors["cyan"] + "Type [1] to explore, [2] to examine or [3] to check timer?" + colors["reset"])
        intended_action = input("> ").strip()
        if intended_action == "1":
            explore_room(room)
            play_room(room)
        elif intended_action == "2":
            examine_item(input("What would you like to examine?").strip())
        elif intended_action == '3':
            is_alive = check_timer(show_time=True)
            if is_alive:
                play_room(room)
        else:
            print("Not sure what you mean. " + colors["cyan"] + "Type [1], [2] or [3]." + colors["reset"])
            play_room(room)
        linebreak()

def explore_room(room):
    """
    Explore a room. List all items belonging to this room.
    """
    items = [i["name"] for i in object_relations[room["name"]]]
    print("You explore the room. This is the " + room["name"] + "." + colors["yellow"] + " You find " + ", ".join(items) + colors["reset"] )

def get_next_room_of_door(door, current_room):
    """
    From object_relations, find the two rooms connected to the given door.
    Return the room that is not the current_room.
    """
    connected_rooms = object_relations[door["name"]]
    for room in connected_rooms:
        if(not current_room == room):
            return room

            
def check_timer(show_time=False):
    current_time = time.time()
    time_passed = current_time - game_state["start_time"]
    time_left = game_state["time_limit"] - time_passed
    """
    import time library and use the time function to calculate how
    much time passed since the player woke up
    the game state start_time value is None that will keep adding up with time.time()
    """
    if time_left <= 0:
        print(colors["red"] + "'EXPLOSION!!!!, you've failed to get out in time'" + colors["reset"])
        try:
            display(Image(filename="game_over.jpg", format="jpeg"))
        except FileNotFoundError:
            print(colors["red"] + "Could not find image." + colors["reset"])
        return False

    if show_time:
        minutes = int(time_left // 60)
        seconds = int(time_left % 60)
        print(f"Time remaining: {minutes}:{seconds:02d}")
    return True
    
def examine_item(item_name):
    """
    Examine an item which can be a door or furniture.
    First make sure the intended item belongs to the current room.
    Then check if the item is a door. Tell player if key hasn't been 
    collected yet. Otherwise ask player if they want to go to the next
    room. If the item is not a door, then check if it contains keys.
    Collect the key if found and update the game state. At the end,
    play either the current or the next room depending on the game state
    to keep playing.
    """
    current_room = game_state["current_room"]
    next_room = ""
    output = None

    if (flashlight in game_state["items_collected"] and
        aa_battery_1 in game_state["items_collected"] and
        aa_battery_2 in game_state["items_collected"]):
        game_state["has_light"] = True
    
    for item in object_relations[current_room["name"]]:
        if(item["name"] == item_name):
            output = "You examine " + item_name + "."
            
            # Exception for the Door F that its always opened
            if item["name"] == "door f":
                if current_room["name"] == "stairs":
                    output += colors["green"] + "It's open." + colors["reset"]
                    next_room = get_next_room_of_door(item, current_room)
                elif game_state.get("has_light",False):
                    output += "You opened door f and went down the stairs"
                    next_room = get_next_room_of_door(item, current_room)
                else:
                    output += colors["yellow"] + "It's pitch black, you need something to light up the way." + colors["reset"]
                    
            # Hammer do break the window and exit
            elif item["name"] == "window":
                has_hammer = hammer in game_state["items_collected"]

                if has_hammer:
                    output = colors["green"] + "CRASH! You use the hammer to shatter the window" + colors["reset"] + "."
                    next_room = outside
                else:
                    output = "The glass is too thick to " + colors["red"] + "break with your bare hands" + colors["reset"] + "."
                    next_room = None  

            # Function that unlocks all doors with their respective keys
            elif(item["type"] == "door"):
                have_key = False
                for key in game_state["items_collected"]:
                    if(key["target"] == item):
                        have_key = True
                if(have_key):
                    output += "You " + colors["green"] + "unlock " + colors["reset"] + "it with a key you have" + "."
                    next_room = get_next_room_of_door(item, current_room)
                else:
                    output += "It is " + colors["red"] + "locked " + colors["reset"] + "but you don't have the key" + "."
            
            # Clock begins to run
            elif item["type"] == "clock":
                check_timer()

            # Lock condition to insert 5 digit numbers or else fails
            elif item["type"] == "lock" or item["name"] == "door g":
                if not game_state.get("has_light", False):
                    output += "It's pitch black, you need something to light up the way."
                else:
                    password = input("What's the 5-digit password?: ").strip()
                    if password == item["code"]:
                        output = colors["green"] + "Door Unlocked" + colors["reset"] + "."
                        next_room = get_next_room_of_door(item, current_room)
                    else:
                        output = colors["red"] + "Incorrect Password" + colors["reset"] + "."
                    
                
            # Postcard code on the fridge with a code "date:9-15-26, code:91526" to insert into door g
            elif "code" in item:
                output += "You can see a postcard with " + colors["yellow"] + "Italy 9-15-26." + colors["reset"] + "."  
            
            else:
                if(item["name"] in object_relations and len(object_relations[item["name"]])>0):
                    item_found = object_relations[item["name"]].pop()
                    game_state["items_collected"].append(item_found)
                    output += colors["green"] + "You find " + item_found["name"] + colors["reset"] + "."
                else:
                    output += "There isn't anything interesting about it."
            
            print(output)
            break

    if(output is None):
        print("The item you requested is not found in the current room.")
    
    if(next_room and input("Do you want to go to the next room? Enter 'yes' or 'no'").strip() == 'yes'):
        play_room(next_room)
    else:
        play_room(current_room)



