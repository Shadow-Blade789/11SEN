class Item:
    def __init__ (self, name, description):
        self.description = description
        self.name = name
    def GetItemName(self):
        return self.name
    def GetItemDesc(self):
        return self.description
    