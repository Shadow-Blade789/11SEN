from cave import Cave
from Character import Enemy
import random
from Character import Enemy
from item import Item
cavern = Cave("Cavern")
cavern.set_description("A dank and dirty cave ")
dungeon = Cave("Dungeon")
dungeon.set_description("A large cave with a rack")
dungeon.SetCharacter("Harry")
grotto = Cave("Grotto")
grotto.set_description("A small cave with ancient graffiti")
harry = Enemy("Harry", "A smelly Wumpus")
harry.set_conversation("Hangry…Hanggrry")

items = [
    "rusty pickaxe", "oil lantern", "torn map fragment", "healing mushroom",
    "iron key", "silver dagger", "rope coil", "traveler’s satchel",
    "runed stone tablet", "crystal of echoes", "broken arrowhead",
    "pebble with a face", "moldy bread crust", "cave bat droppings",
    "dented tin cup", "empty scroll case", "cracked mirror shard",
    "worm-eaten book", "chewed leather glove", "world's okayest adventurer medal",
    "whispering skull", "black ring of hollow flame", "blood-stained doll",
    "mirror of regret", "grasping roots", "cursed coin", "lantern of false light",
    "bone charm of the forgotten", "veil of the lost miner", "book of unreadable names"
]
descriptions = [
    "an old pickaxe, its edge worn but still capable of breaking stone.",
    "a dented lantern filled with thick, amber oil — it casts a flickering light.",
    "a fragile piece of parchment with faded ink markings and cryptic symbols.",
    "a pale blue mushroom with a faint, pleasant scent — it looks safe to eat.",
    "a heavy iron key, cold to the touch, clearly meant for an old lock.",
    "a finely crafted dagger with a glinting silver blade and ornate hilt.",
    "a sturdy length of rope, coiled tightly and ready for use.",
    "a leather satchel with worn straps, but plenty of room inside.",
    "a flat stone engraved with unfamiliar runes glowing faintly in the dark.",
    "a small, clear crystal that hums softly when held near your ear.",
    "a chipped arrowhead made of flint — long past its usefulness.",
    "a smooth pebble that eerily resembles a smiling face.",
    "a crust of bread long turned green and brittle with age.",
    "a pile of foul-smelling droppings, best left undisturbed.",
    "a lightweight tin cup with a large dent and rusted rim.",
    "a hollow scroll case, its contents long since removed or lost.",
    "a shard of mirror glass, cracked and cold, reflecting distorted shapes.",
    "a fragile old book, its pages riddled with holes and unreadable text.",
    "a single leather glove with tooth marks — the other is missing.",
    "a small medal stamped with 'world's okayest adventurer'.",
    "a weathered skull with empty eye sockets that seem to follow you.",
    "a dark metal ring, unnaturally cold, with a faint flicker inside.",
    "a porcelain doll stained red, sitting oddly upright in the dust.",
    "a small mirror framed in black, reflecting your face… differently.",
    "a tangled mass of roots, dry yet oddly warm to the touch.",
    "a golden coin that glints even in the deepest dark.",
    "a lantern that burns with a blue flame and no apparent fuel.",
    "a carved bone trinket tied with faded string and beads.",
    "a worn cloth veil, soft and moth-eaten, with a miner's tag attached.",
    "a thick leather-bound book filled with incomprehensible symbols."
]

item = Item((chosen := random.choice(items)), descriptions[items.index(chosen)])
inventory = []
inventory.append(item.name)
print(inventory)
grotto.SetItem(item.name, item.description)


cavern.link_cave(dungeon, "east")
dungeon.link_cave(cavern, "west")
grotto.link_cave(cavern, "north")
cavern.link_cave(grotto, "south")
harry = Enemy("Harry", "A smelly Wumpus")
#harry.describe()
current_cave = cavern          

dead = False

while dead == False:		
    print("\n")         
    current_cave.get_details()      
    inhabitant = current_cave.GetCharacter()
    if inhabitant is not None:
        if inhabitant == "Harry":
            harry.describe()
        else:
            pass  
    command = input("> ")
    if command.lower() == "north":
        current_cave = current_cave.move(command)
    elif command .lower() == "south":
        current_cave = current_cave.move(command)
    elif command.lower() == "east":
        current_cave = current_cave.move(command)
    elif command.lower() == "west":
        current_cave = current_cave.move(command)
    elif command.lower() == "talk":
     #Talk to the inhabitant - check whether there is one!
        if inhabitant is not None:
            inhabitant.talk()
        else:
            print("Talking to oneself is the root of insanity.")
    elif command.lower() == "fight":
        if inhabitant == 'Harry':
            # Fight with the inhabitant, if there is one
            print(harry.GetWeakness())
            print("What will you fight with?")
            combat_item = input().lower()
            if harry.fight(combat_item) == True:
                # What happens if you win?
                print("Bravo,hero you won the fight!")
                current_cave.SetCharacter(None)
            else:
                print("Scurry home, you lost the fight.")
                dead = True
        else:
            print("There is no one here to fight with, you punch yourself.")
    elif command.lower() == "exit":
        dead = True