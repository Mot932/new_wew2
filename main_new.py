from random import choice, randint

first_names = ("Жран", "Дрын", "Брысь", "Жлыг", "Паша")
last_name = ("Ужасный", "Зловонный", "Борзый", "Жирный", "Кровавый")


def make_hero(
        name=None,
        hp_now=None,
        lvl=1,
        xp_now=0,
        xp_next=1000,
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

p1 = make_hero()
p2 = make_hero()
p3 = make_hero(name="Вася",money=0)

print(p1)
print(p2)
print(p3)
