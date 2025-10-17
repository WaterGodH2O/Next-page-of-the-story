class player:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.inventory = []
        self.HP = 10
        self.alive = True

    def backpackContent(self):
        return self.backpack