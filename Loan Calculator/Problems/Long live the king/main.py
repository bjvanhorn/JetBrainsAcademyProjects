# (c,r)
# if 1 < c < 8 and if 1 < r < 8, 8 moves
# if 1 < c < 8 xor if 1 < r < 8, 5 moves
# if c == 1 or c == 8 and r == 1 or r == 8, 3 moves

column, row = int(input()), int(input())
if column in [1, 8] and row in [1, 8]:
    print("3")
elif 1 < column < 8 and row in [1, 8]:
    print("5")
elif column in [1, 8] and 1 < row < 8:
    print("5")
else:
    print("8")
