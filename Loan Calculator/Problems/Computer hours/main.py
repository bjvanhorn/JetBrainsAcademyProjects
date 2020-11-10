time_on_pc = int(input())
if time_on_pc < 2:
    print("That seems reasonable")
elif 2 <= time_on_pc < 4:
    print("Do you have time for anything else?")
else:
    print("Don't forget to take breaks!")
