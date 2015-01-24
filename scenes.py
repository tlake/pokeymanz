db = {

"beginning_town": {
    "name": "Beginning Town",
    "desc": "The air in this tiny little hamlet is clean and fresh. It " \
        "smells of new beginnings! Which is appropriate, since this is the town "  \
        "whence your journey (an incredible one, to be sure, and not just like " \
        "everybody else who's ever played any kind of pokeyman game) begins! " \
        "There is grass! There are houses! There are ostensibly other people " \
        "living in this town!\n\nOf import to you, dear player, are your own " \
        "home, a pokeycenter, an item shop, and the northern exit to Route 1.",
    "exits": {
        "Home": "player_home",
        "Pokeycenter": "pokeycenter",
        "Item Shop": "item_shop",
        "Route 1": "route_1a"
        }
},


"player_home": {
    "name": "Home",
    "desc": "Home sweet home! You've got a bed and one of whatever the most \
        recent pokeyman-related gaming systems is. Your mom's also hanging around, \
        doing mom things that you're probably too young to understand.",
    "exits": {
        "Outside": "beginning_town"
        },
    "people": {
        "Mom": "people.mom"
        }
},


"pokeycenter": {
    "name": "Pokeyman Center",
    "desc": "It's a pokeyman center! A waiting area occupies one side of \
        the room, populated with almost-comfortable chairs and low tables seeded \
        with outdated copies of unpopular magazines. The other side of the room \
        contains a single computer hooked up to the pokeynet. At the back of the \
        room is a long desk, staffed by a woman with pink hair; no doubt one of \
        uncountable clones created by some shadow-science organization for the \
        sole purpose of staffing pokeyman centers. Creepy.",
    "exits": {
        "Outside": "game_data['last_scene']"
        },
    "people": {
        "Nurse": "people.pokeycenter_nurse"
        },
    "objects": {
        "PC": "objects.pokeyman_computer"
        }
},


"item_shop": {
    "name": "Item Shop",
    "desc": "Cut-rate tile covers the floor, illuminated by the harsh light \
        of overhead fluorescent lighting. Display racks line the walls and feature \
        prominently in the center of the store. To one side of the room is the \
        cash register and checkout desk, attended by a nondescript man.",
    "exits": {
        "Outside": "game_data['last_scene']"
        },
    "people": {
        "Clerk": "people.item_shop_clerk"
        }
},


"route_1a": {
    "name": "Route 1",
    "desc": "A small dirt path winds its way through the short grass along \
        this part of Route 1, trampled out by countless (okay, fine, several) \
        meanderings of folk to and from Beginning Town. Occasionally, some yards \
        away from the path, the grass grows taller and can sometimes be seen to \
        rustle with the doings and goings-on and hip-happenings of pokeymanz. \
        You could probably HUNT in the GRASS for a wild pokeyman if you wanted.",
    "exits": {
        "Beginning Town": "beginning_town"
        },
    "hunts": {
        "Grass": {
            "Ratatta": ["Ratatta", 5]
            }
        }
},


}
