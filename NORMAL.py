class Person:
    def __init__(self, health, damage, armor):
        self.health = health
        self.damage = damage
        self.armor = armor

    def take_damage(self, damage):
        effective_damage = max(damage - self.armor, 0)
        self.health -= effective_damage
        return effective_damage

    def is_alive(self):
        return self.health > 0


class Player(Person):
    def __init__(self, health, damage, armor):
        super().__init__(health, damage, armor)

    def attack(self, enemy):
        print(f"Игрок атакует врага на {self.damage} урона.")
        damage_dealt = enemy.take_damage(self.damage)
        print(f"Враг получил {damage_dealt} урона. Осталось здоровья: {enemy.health}.")


class Enemy(Person):
    def __init__(self, health, damage, armor):
        super().__init__(health, damage, armor)

    def attack(self, player):
        print(f"Враг атакует игрока на {self.damage} урона.")
        damage_dealt = player.take_damage(self.damage)
        print(f"Игрок получил {damage_dealt} урона. Осталось здоровья: {player.health}.")


class Game:
    def __init__(self, player, enemy):
        self.player = player
        self.enemy = enemy

    def start_battle(self):
        turn = 0

        while self.player.is_alive() and self.enemy.is_alive():
            if turn == 0:
                self.player.attack(self.enemy)
                turn = 1
            else:
                self.enemy.attack(self.player)
                turn = 0

        if self.player.is_alive():
            print("Игрок победил!")
        else:
            print("Враг победил!")


player = Player(health=100, damage=20, armor=5)
enemy = Enemy(health=80, damage=15, armor=3)


game = Game(player, enemy)
game.start_battle()
