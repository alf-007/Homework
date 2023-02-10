import random

input_from_user = input("What will you eat for dinner? (write by a comma)")

dishes_for_lunches = input_from_user.split(',')

print('''—--Кафе “У Монті”---''')
total_price = 0


for i in dishes_for_lunches:
    i = i.strip()
    price = random.randint(55, 590)
    total_price = total_price + price
    print("{} ....... {} uah".format(i, price))


print("Total is {} uah".format(total_price))
