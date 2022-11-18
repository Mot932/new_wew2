from random import choice, randint

first_names = ("Жран", "Дрын", "Брысь", "Жлыг", "Паша")
last_name = ("Ужасный", "Зловонный", "Борзый", "Жирный", "Кровавый")


def make_hero(
        name=None,
        hp_now=None,
        lvl=1,
        xp_now=0,
        xp_next=100,
        attack=1,
        defence=0,
        luck=1,
        money=None,
        inventory=None,
) -> list:
    """
    Персонаж - это список
    [0] name - имя
    [1] hp_now - здоровье сейчас
    [2] hp_max - здоровье максимальное
    [3] lvl - уровень
    [4] xp_now - опыт текущий
    [5] xp_next - опыт до след.уровня
    [6] attack - атака
    [7] defence - защита
    [8] luck - удача
    [9] money - деньги
    [10] inventory - список предмет
    """
    if not name:
        name = choice(first_names) + " " + choice(last_name)

    if not hp_now:
        hp_now = randint(1, 100)
        hp_max = hp_now

    if not inventory:
        inventory = []

    if money is None:
        money = randint(0, 100)

    return [
        name,
        hp_now,
        hp_max,
        lvl,
        xp_now,
        xp_next,
        attack,
        defence,
        luck,
        money,
        inventory
]


def show_hero(hero):
    print("имя:", hero[0])
    print("здоровье сейчас:", hero[1])
    print("здоровье максимальное:", hero[2])
    print("уровень:", hero[3])
    print("опыт текущий:", hero[4])
    print("опыт до след.уровня:", hero[5])
    print("атака:", hero[6])
    print("защита:", hero[7])
    print("удача:", hero[8])
    print("деньги:", hero[9])
    print("список предмет:", hero[10])
    print(" ")

def levelup(hero: list) -> None:
    if hero[4] >= hero[5]:
        hero[3] += 1
        hero[5] = hero[3] * 100
        print(f"{hero[0]} получил {hero[3]} уровень")
        print(" ")

def buy_item(hero, price):
    if hero[9] >= price:
        hero[9] -= price
        hero[10].append("зелье")
        print(f"{hero[0]} купил {price} зелья")
        print(" ")
    else:
        print(f"{hero[0]} нет столько  монет")

def consume_item(hero: list, item: str) -> None:
    """
    Найти предмет в инвентаре героя
    Этот предмет удаляется из инвентаря
    Герой получает эффект от этого предмета
    """

p1 = make_hero()
show_hero(p1)
p2 = make_hero(money=100000)
show_hero(p2)
p3 = make_hero(name="Паша",money=0.0001)
show_hero(p3)

p1[4] += 100
levelup(p1)

p3[4] += 50
levelup(p3)

show_hero(p1)
show_hero(p2)
show_hero(p3)

buy_item(p2, 10)

show_hero(p1)
show_hero(p2)
show_hero(p3)