class Cave:
    def __init__(self, cave_name):
        self.name = cave_name
        self.description = None
        self.linked_caves = {}
        self.character = None
        self.item = None
    def GetCharacter(self):
        return self.character
    def SetCharacter(self, character):
        self.character = character
    def get_name(self):
        return self.name
    def get_description(self):
        return self.description
    def set_description(self, cave_description):
        self.description = cave_description
    def describe(self):
        print(self.description)
    def link_cave(self, cave_to_link, direction):
        self.linked_caves[direction] = cave_to_link
    def get_details(self):
        for direction in self.linked_caves:
            cave = self.linked_caves[direction]
            print( "The " + cave.get_name() + " is " + direction)
    def move(self, direction):
        if direction in self.linked_caves:
            return self.linked_caves[direction]
        else:
            print("You can't go that way")
            return self
    def SetItem(self, itemname, desc):
        self.itemname = itemname
        self.desc = desc
        if self.item is not None:
            print(f"Item: {self.itemname} is here. {self.desc}")
    def GetItem(self):
        return self.item