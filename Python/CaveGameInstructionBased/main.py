from cave import Cave
from Character import Enemy
import random
cavern = Cave("Cavern")
cavern.set_description("A dank and dirty cave ")
dungeon = Cave("Dungeon")
dungeon.set_description("A large cave with a rack")
grotto = Cave("Grotto")
grotto.set_description("A small cave with ancient graffiti")

cavern.link_cave(dungeon, "east")
dungeon.link_cave(cavern, "west")
grotto.link_cave(cavern, "north")
cavern.link_cave(grotto, "south")
harry = Enemy("Harry", "A smelly Wumpus")
harry.describe()
current_cave = cavern          
while True:		
    print("\n")         
    current_cave.get_details()         
    command = input("> ")    
    current_cave = current_cave.move(command)  

