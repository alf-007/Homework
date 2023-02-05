# Попросіть користувача ввести список страв, що треба подати до вечері (може бути будь-яка кількість), розділені комами.
# Після обробки треба вивести чек із назвою страви і ціною (ціна “розраховується” через модуль random)
# pip install tabulate

import random
from tabulate import tabulate

dish_for_lunch_1 = input("What do you prefer to eat for main dish?  ").strip().capitalize()
dish_for_lunch_2 = input("What do you prefer to eat for second dish?  ").strip().capitalize()
dish_for_lunch_3 = input("What do you prefer to eat for desert?  ").strip().capitalize()
dish_for_lunch_4 = input("What do you prefer for drink?  ").strip().capitalize()


price_1 = random.randint(100, 500)
price_2 = random.randint(70, 600)
price_3 = random.randint(60, 170)
price_4 = random.randint(50, 200)

check_cost = price_1 + price_2 + price_3 + price_4

table = [['Dish', 'Price', 'Currency'],
         [dish_for_lunch_1, price_1, 'грн'],
         [dish_for_lunch_2, price_2, 'грн'],
         [dish_for_lunch_3, price_3, 'грн'],
         [dish_for_lunch_4, price_4, 'грн'],
         ['Total', check_cost, 'грн']]


print('''—--Кафе “У Монті”---''')
print(tabulate(table, headers='firstrow', tablefmt='fancy_grid'))



