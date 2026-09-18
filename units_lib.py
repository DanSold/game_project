class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.max_health = 100
        self.damage = 20
        self.defense = 5
        self.level = 1
        self.xp = 0
        self.gold = 0
        self.reputation = 0
        self.inventory = []
        self.artifacts = []
