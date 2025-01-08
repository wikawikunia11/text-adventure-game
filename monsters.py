from random import randint


class Monster_level_1:
    def __init__(self, monster: dict) -> None:
        try:
            self.type = 'monster'
            self.level = monster['level']
            if monster['health'] >= 0:
                self.health = monster['health']
                self._max_health = monster['health']
            else:
                raise ValueError('Monsters health has to be positive')
            self.name = monster['name']
            if monster['coins'] < 0:
                raise ValueError('Number of coins can not be negative')
            else:
                self.coins = monster['coins']
            self.description = monster['description']
        except KeyError:
            raise KeyError('The dictionary should contain keys:'
                           'type, level, health, name, coins, description')

    def get_damage(self, damage: int) -> None:
        if damage < 0:
            raise ValueError('Damage must be positive')
        if self.is_alive(damage):
            self.health -= damage
        else:
            self.die()

    def give_coins(self) -> int:
        return self.coins

    def is_alive(self, damage: int) -> bool:
        return (self.health - damage > 0)

    def die(self) -> None:
        self.health = 0


class Monster_level_2(Monster_level_1):
    def __init__(self, monster: dict) -> None:
        super().__init__(monster)
        try:
            if monster['hit strength'] > 0:
                self.hit_strength = monster['hit strength']
            else:
                raise ValueError('Hit strength must be a positive int')
        except KeyError:
            raise KeyError('The dictionary should contain key: hit strength')

    def attack_player(self) -> int:
        if randint(1, 4) == 4:
            return self.hit_strength
        else:
            return 0


class Monster_level_3(Monster_level_2):
    def __init__(self, monster: dict) -> None:
        super().__init__(monster)

    def heal(self, damage: int) -> None:
        if not isinstance(damage, int) or damage < 0:
            raise ValueError('Damage must be a positive int')
        if randint(1, 4) == 4:
            if self.health + damage < self._max_health:
                self.health += damage
            else:
                self.health = self._max_health
            print("Oh no the monster healed!")

    def attack_player(self) -> None:
        if randint(1, 4) == 4:
            if randint(1, 4) == 4:
                return self.hit_strength*2
            else:
                return self.hit_strength
        else:
            return 0
