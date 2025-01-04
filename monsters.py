from random import randint


class Monster_level_1:
    def __init__(self, monster: dict) -> None:
        try:
            self.type = 'monster'
            self.level = monster['level']
            if monster['health'] > 0:
                self.health = monster['health']
                self._max_health = monster['health']
            else:
                raise ValueError('Monsters health has to be positive')
            self.name = monster['name']
            self.item = monster['item']
            self.description = monster['description']
        except KeyError:
            raise KeyError('The dictionary should contain keys:'
                           'type, level, health, name, item, description')

    def get_damage(self, damage: int):
        if damage < 10:
            raise ValueError('Damage must be positive')
        if self.is_alive(damage):
            self.health -= damage
        else:
            self.die()

    def give_item(self):
        if self.item is not None:
            return self.item

    def is_alive(self, damage: int):
        return ((self.health-damage) > 0)

    def die(self):
        self.give_item()
        self.health = 0
        # usuwanie z mapy


class Monster_level_2(Monster_level_1):
    def __init__(self, monster: dict):
        super().__init__(monster)
        try:
            if monster['hit strength'] > 0:
                self.hit_strength = monster['hit strength']
            else:
                raise ValueError('Hit strength must be a positive int')
        except KeyError:
            raise KeyError('The dictionary should contain key: hit strength')

    def attack_player(self):
        return self.hit_strength


class Monster_level_3(Monster_level_2):
    def __init__(self, monster: dict):
        super().__init__(monster)

    def heal(self, damage):
        if damage < 0:
            raise ValueError('Damage must be a positive int')
        if randint(1, 4) == 4:
            if self.health + damage < self._max_health:
                self.health += damage
                return 'The monster has healed!'
            else:
                self.health = self._max_health

    def attack_player(self):
        if randint(1, 4) == 4:
            return self.hit_strength*2
        else:
            return self.hit_strength
