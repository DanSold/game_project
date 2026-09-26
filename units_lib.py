class Player:
    def __init__(self, name: str) :
        self.name = name
        self.health = 100
        self.max_health = 100
        self.damage = 20
        self.defense = 5
        self.level = 1
        self.xp = 0
        self.gold = 0
        self.reputation = 0
        self.inventory = []         # inventory = [small_potion, leather_armor, ...] -> list(Item)
        self.equipped_weapon = []   # equipped_weapon = [steel_sword] -> only one item in list class Item(Weapon)
        self.equipped_armor = []    # equipped_armor = [steel_armor] -> only one item in list class Item(Armor)
        self.artifacts = []         # artifacts = ["All-seeing Eye", "Eternal Fire", ...] -> list(str)
        self.quests = []            # quests = ["Old Stories", ...] -> list(str)
        self.completed_quests = []  # completed_quests = ["Gold, gold, gold...", ...] -> list(str)
        self.quests_items = []      # quests_items = ["Cart", ...] -> list(str)


class Enemy:
    def __init__(self, name: str, health: int, damage: int, defense: int, xp: int, gold: int):
        self.name = name
        self.health = health
        self.damage = damage
        self.defense = defense
        self.xp = xp
        self.gold = gold


class Item:
    def __init__(self, name: str, cost: int, item_type: str):
        self.name = name
        self.cost = cost
        self.item_type = item_type


class Potion(Item):
    def __init__(self, name: str, health_up: int, cost: int):
        super().__init__(name, cost, item_type="potion")
        self.health_up = health_up


class Weapon(Item):
    def __init__(self, name: str, damage_bonus: int, cost: int, level:int, coef_up: float):
        super().__init__(name, cost, item_type="weapon")
        self.damage_bonus = damage_bonus
        self.level = level
        self.upgrade_cost = round(cost // 2)
        self.coef_up = coef_up


class Armor(Item):
    def __init__(self, name: str, defense_bonus: int, cost: int, level: int, coef_up: float):
        super().__init__(name, cost, item_type="armor")
        self.defense_bonus = defense_bonus
        self.level = level
        self.upgrade_cost = round(cost // 2)
        self.coef_up = coef_up


small_potion = Potion("Small Potion", 10, 5)
mid_potion = Potion("Medium Potion", 25, 12)
large_potion = Potion("Large Potion", 50, 25)

copper_sword = Weapon("Copper Sword", damage_bonus=5, cost=30, level=1, coef_up=1.2)
steel_sword = Weapon("Steel Sword", damage_bonus=10, cost=50, level=1, coef_up=1.4)

leather_armor = Armor("Leather Armor", defense_bonus=2, cost=30, level=1, coef_up=1.3)
ring_mail = Armor("Ring-mail Armor", defense_bonus=3, cost=35, level=1, coef_up=1.5)
steel_armor = Armor("Steel Armor", defense_bonus=4, cost=45, level=1, coef_up=1.4)

trash = Item("Trash", 2, "trash")
poison = Item("Poison", 1, "poison")
goods = Item("Goods", 30, "goods")

shop_inventory = [small_potion, mid_potion, large_potion, copper_sword, steel_sword, leather_armor, ring_mail,
                  steel_armor, poison]

bandit = Enemy("Bandit", 70, 15, 2, 20, 15)
group_bandits = Enemy("Group of Bandits", 110, 20, 1, 60, 45)
knight = Enemy("Knight", 100, 18, 3, 40, 30)
