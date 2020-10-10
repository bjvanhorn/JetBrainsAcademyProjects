# put your python code here
duration = int(input())
food_per_day = int(input())
flight_cost = int(input())
one_day_hotel = int(input())
print(flight_cost * 2 + food_per_day * duration + one_day_hotel * (duration - 1))
