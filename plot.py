import random
import time

class Person:
    role = {
        '1': 'Воин',
        '2': 'Лучник',
        '3': 'Маг'
    }

    classes = {
        'Воин': {
            'здоровье': 100,
            'атака': 50,
            'защита': 25,
            'навыки': {
                'щит': 20
            }
        },
        'Лучник': {
            'здоровье': 70,
            'атака': 80,
            'защита': 15,
            'навыки': {
                'убежать': 10
            }
        },
        'Маг': {
            'здоровье': 50,
            'атака': 90,
            'защита': 15,
            'навыки': {
                'магический щит': 45,
                'лечение': 20
            }
        }
    }


    def __init__(self, name, person_class, is_enemy):
        self.name = name
        self.person_class = self.classes[person_class]
        self.health = self.person_class['здоровье']
        self.attack = self.person_class['атака']
        self.defence = self.person_class['защита']
        self.money = 1000.0
        self.skills = self.person_class['навыки']
        self.inventory = ['яблоко', 'шаурма']
        self.is_alive = True
        self.is_enemy = is_enemy

    def get_person_class(self):
        choise = input("Выбери персонажа: 1-Воин, 2-Лучник, 3-Маг. ")
        return self.role[choise]

        print(f"{self.name} - {self.person_class}.")
        print("У него такие характеристики: ")
        print(f"здоровье - {self.health}, \n атака - {self.attack}, \n защита - {self.defence}.")

    def get_person_class2(self):
        if self.is_enemy:
            random_choice = random.choice(list(self.role.keys()))
            return self.role[random_choice]
        else:
            choice = input(f"Введите роль: 1-Воин, 2-Лучник, 3-Маг. ")
            return self.role

    def attack_enemy(self, enemy1, enemy2):
        print(f"{green_color}{enemy1.name}{white_color} атакует {red_color}{enemy2.name}!{whine_color}")
        time.sleep(2)

        damage = enemy1.attack - enemy2.defence
        if damage < 0:
            damage = 1
        enemy2.health -=damage

        print(f"{enemy1.name} наносит {red_color}{damage} урона {white_color} и у {enemy2.name} остаётся {green_color}{enemy2.health} здоровья!{white_color}")

    def fight_for_the_win(self, attacker, defender):
        while attacker.is_alive and defender.is_alive:
            time.sleep(2)

            if attacker.health > 0:
                self.attack_enemy(attacker, defender)
            else:
                print(f"{red_color}{attacker.name} потерпел поражение!{white_color}")
                attacker.is_alive = False
                return False

            if defender.health > 0:
                self.attack_enemy(defender, attacker)
            else:
                print(f"{green_color}{defender.name} потерпел поражение!{white_color}")
                defender.is_alive = False
                return True

class Player(Person):
    def __init__(self, name, person_class, is_enemy):
        Player.__init__(self, name)
        Player.__init__(self, person_class)
        Player.__init__(self, health)
        Player.__init__(self, attack)
        Player.__init__(self, defence)
        Player.__init__(self, skills)
        Player.__init__(self, is_alive)
    def attack_enemy(self, enemy1, enemy2):
        Player.attack_enemy(self, enemy1)
        Player.attack_enemy(self, enemy2)
    def fight_for_the_win(self, attacker, defender):
        Player.fight_for_the_win(self, attacker)
        Player.fight_for_the_win(self, defender)

class Enemy(Person):
    def __init__(self, name, person_class, is_enemy):
        Enemy.__init__(self, name)
        Enemy.__init__(self, person_class)
        Enemy.__init__(self, health)
        Enemy.__init__(self, attack)
        Enemy.__init__(self, defence)
        Enemy.__init__(self, skills)
        Enemy.__init__(self, is_alive)
    def attack_enemy(self, enemy1, enemy2):
        Enemy.attack_enemy(self, enemy1)
        Enemy.attack_enemy(self, enemy2)
    def fight_for_the_win(self, attacker, defender):
        Enemy.fight_for_the_win(self, attacker)
        Enemy.fight_for_the_win(self, defender)

class Item:
    def __init__(self, name):
        self.name = name
        self.__value = 0

    # Возвращает значение предмета для использования
    def use(self):
        return self.__value

# Продолжи писать решение тут
class Food(Item):
    def __init__(self, name):
        Item.__init__(self, name)
        self.__velue = random.randint(1, 8)