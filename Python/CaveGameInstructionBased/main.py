from cave import Cave
from Character import Enemy
import random
from Character import Enemy
cavern = Cave("Cavern")
cavern.set_description("A dank and dirty cave ")
dungeon = Cave("Dungeon")
dungeon.set_description("A large cave with a rack")
dungeon.set_character("Harry")
grotto = Cave("Grotto")
grotto.set_description("A small cave with ancient graffiti")
harry = Enemy("Harry", "A smelly Wumpus")
harry.set_conversation("Hangry…Hanggrry")
harry.set_weakness()


cavern.link_cave(dungeon, "east")
dungeon.link_cave(cavern, "west")
grotto.link_cave(cavern, "north")
cavern.link_cave(grotto, "south")
harry = Enemy("Harry", "A smelly Wumpus")
harry.describe()
current_cave = cavern          

print("What will you fight with?")
fight_with = input()
harry.fight(fight_with)

while True:		
    print("\n")         
    current_cave.get_details()      
    inhabitant = current_cave.get_character()
    if inhabitant is not None:
        inhabitant.describe()  
    command = input("> ")    
    current_cave = current_cave.move(command)  


