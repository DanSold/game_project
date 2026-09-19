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
        self.quests = []
        self.completed_quests = []

class Enemy:
    def __init__(self, name, health, damage, defense, xp, gold):
        self.name = name
        self.health = health
        self.damage = damage
        self.defense = defense
        self.xp = xp
        self.gold = gold

bandit = Enemy( "Bandit", 70, 18, 2, 25, 20 )