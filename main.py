from abc import ABC, abstractmethod


# Шаг 1: Создание абстрактного класса для оружия
class Weapon(ABC):
    @abstractmethod
    def attack(self):
        pass

    @abstractmethod
    def __str__(self):
        pass


# Шаг 2: Реализация конкретных типов оружия
class Sword(Weapon):
    def attack(self):
        return "удар мечом"

    def __str__(self):
        return "меч"


class Bow(Weapon):
    def attack(self):
        return "выстрел из лука"

    def __str__(self):
        return "лук"


class Axe(Weapon):
    def attack(self):
        return "удар топором"

    def __str__(self):
        return "топор"


# Шаг 3: Модификация класса Fighter
class Fighter:
    def __init__(self, name):
        self.name = name
        self.weapon = None

    def change_weapon(self, weapon: Weapon):
        self.weapon = weapon
        print(f"{self.name} выбирает {self.weapon}.")

    def attack(self, monster):
        if self.weapon:
            attack_message = self.weapon.attack()
            print(f"{self.name} наносит {attack_message}.")
            monster.take_damage()
        else:
            print(f"{self.name} не выбрал оружие.")


class Monster:
    def __init__(self, health=100):
        self.health = health

    def take_damage(self):
        self.health -= 50  # Условный урон для примера
        if self.health <= 0:
            print("Монстр побежден!")
        else:
            print(f"Монстр получил урон, оставшееся здоровье: {self.health}")


fighter = Fighter("Боец")
monster = Monster()

sword = Sword()
bow = Bow()
axe = Axe()

fighter.change_weapon(sword)
fighter.attack(monster)

fighter.change_weapon(bow)
fighter.attack(monster)

fighter.change_weapon(axe)
fighter.attack(monster)
