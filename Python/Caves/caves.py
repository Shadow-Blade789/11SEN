class Cave:
    def __init__ (self, location, typeofcave):
        self.location = location
        self.typeofcave = typeofcave
        
    def GetLocation():
        if self.typeofcave == "Cavern":
            self.location = "Central"
        
    def GetType():
        if playerpos == "n":
            pass
        
playerpos = "Centre"
def Q():
    command = input("What Direction? ").lower()
    if command == "n":
        playerpos = "North"
        #find current cave function
        #print current cave description/other stuff
    elif command == "s":
        playerpos = "South"
    elif command == "e":
        playerpos = "East"
    elif command == "w":
        playerpos = "West"
    else:
        command = input("What direction? ").lower()

while True:
    Q()