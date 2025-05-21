class Cave:
    def __init__ (self, location, typeofcave):
        self.location = location
        self.typeofcave = typeofcave
        
    def GetLocation(self):
        self.location = playerpos
        
    def CaveDesc(self):
        if self.typeofcave == "Cavern":
            description = "Big"
            print(description)
        
cavetest = Cave("Centre", "Cavern")
northcave = Cave("North", "Rock Wall")
southcave = Cave("South", "Rocky")
eastcave = Cave("East", "d")
westcave = Cave("West", "d")

playerpos = "Centre"
def Q():
    command = input("What Direction? ").lower()
    if command == "n":
        playerpos = "North"
        #find current cave function
        #print current cave description/other stuff
    elif command == "s":
        playerpos = "South"
        cavetest.CaveDesc()
    elif command == "e":
        playerpos = "East"
    elif command == "w":
        playerpos = "West"
    else:
        command = input("What direction? ").lower()

while True:
    Q()