from cave import Cave
from Character import Enemy
import random
from Character import Enemy
cavern = Cave("Cavern")
cavern.set_description("A dank and dirty cave ")
dungeon = Cave("Dungeon")
dungeon.set_description("A large cave with a rack")
dungeon.SetCharacter("Harry")
grotto = Cave("Grotto")
grotto.set_description("A small cave with ancient graffiti")
harry = Enemy("Harry", "A smelly Wumpus")
harry.set_conversation("Hangry…Hanggrry")
harry.SetWeakness()


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
            harry.talk()
        else:
            print("Talking to oneself is the root of insanity.")
    elif command.lower() == "fight":
        if inhabitant == 'Harry':
            # Fight with the inhabitant, if there is one
            print("What will you fight with?")
            fight_with = input().lower()
            if harry.fight(fight_with) == True:
                # What happens if you win?
                print("Bravo,hero you won the fight!")
                current_cave.set_character(None)
            else:
                print("Scurry home, you lost the fight.")
                dead = True
        else:
            print("There is no one here to fight with, you punch yourself.")