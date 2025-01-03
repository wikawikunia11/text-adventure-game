from random import randint


class Monster_level_1:
    def __init__(self, monster: dict) -> None:
        self.type = 'monster'
        self.level = monster['level']
        self.health = monster['health']
        self.name = monster['name']
        self.item = monster['item']
        self.description = monster['description']

    def get_damage(self, hit_strength: int):
        if self.is_alive(hit_strength):
            self.health -= hit_strength
        else:
            self.die()

    def give_item(self):
        return self.item

    def is_alive(self, damage: int):
        return ((self.health-damage) > 0)

    def die(self):
        self.give_item()
        # usuwanie z mapy


class Monster_level_2(Monster_level_1):
    def __init__(self, monster: dict):
        super.__init__(self, monster)
        self.hit_strength = monster['hit strength']

    def attack_player(self):
        return self.hit_strength


class Monster_level_3(Monster_level_2):
    def __init__(self, monster: dict):
        super.__init__(self, monster)

    def heal(self, damage):
        if randint(1, 4) == 4:
            self.health += damage

    def attack_player(self):
        if randint(1, 4) == 4:
            return self.hit_strength*2
        else:
            return self.hit_strength
