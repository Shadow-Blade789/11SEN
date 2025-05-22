from cave import Cave     
maincave = Cave("Centre", "Cavern")
northcave = Cave("North", "Rock Wall")
southcave = Cave("South", "Rocky")
eastcave = Cave("East", "Dark")
westcave = Cave("West", "Wet")

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