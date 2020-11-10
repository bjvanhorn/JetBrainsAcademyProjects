amount_of_money = int(input())
if amount_of_money >= 6769:
    print(amount_of_money // 6769, "sheep")
elif amount_of_money >= 3848:
    print(amount_of_money // 3848, "cow")
elif amount_of_money >= 1296:
    number_of_animals = amount_of_money // 1296
    print(number_of_animals, "pigs" if number_of_animals > 1 else "pig")
elif amount_of_money >= 678:
    print(amount_of_money // 678, "goat")
elif amount_of_money >= 23:
    number_of_animals = amount_of_money // 23
    print(number_of_animals, "chickens" if number_of_animals > 1 else "chicken")
else:
    print("None")

# can have:
# unlimited sheep
# one cow
# 2 pigs
# one goat
# 29 chickens
