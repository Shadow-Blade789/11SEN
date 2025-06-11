import random
class Character():
    def __init__(self, char_name, char_description):
        self.name = char_name
        self.description = char_description
        self.conversation = None
    # Describe this character
    def describe(self):
        print( self.name + " is here!" )
        print( self.description )
    # Set what this character will say when talked to
    def set_conversation(self, conversation):
        self.conversation = conversation
    # Talk to this character
    def talk(self):
        if self.conversation is not None:
            print("[" + self.name + " says]: " + self.conversation)
        else:
            print(self.name + " doesn't want to talk to you")
    # Fight with this character
    def fight(self, combat_item):
        print(self.name + " doesn't want to fight with you")
        return True
# Add your code here (first line unindented)
class Enemy(Character):
    def __init__ (self, char_name, char_description):
        super().__init__(char_name, char_description)
        wek = [
            "banana", "smashed ostrich", "apple magic mouse", "effective literary devices", "loud noises",
            "garlic", "silver glitter", "purple light", "condensed water", "electricity",
            "spiders", "maths", "jazz music", "tofu", "chalk",
            "kittens", "paper cuts", "clowns", "salt", "wind",
            "bubble wrap", "gluten", "lasers", "velcro", "magnets"
        ]
        self.weakness = random.choice(wek)
    def GetWeakness(self):
        return self.weakness
    def fight(self, combat_item):
        print(self.weakness)
        if combat_item == self.weakness:
            print("You fend " + self.name + " off with the " + combat_item )
            return True
        else:
            print(self.name + " swallows you, little wimp")
            return False
