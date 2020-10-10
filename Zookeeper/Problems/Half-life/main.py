initial_quantity = int(input())
final_quantity = int(input())
half_life_periods = 0

while initial_quantity >= final_quantity:
    initial_quantity /= 2
    half_life_periods += 1

print(half_life_periods * 12)
