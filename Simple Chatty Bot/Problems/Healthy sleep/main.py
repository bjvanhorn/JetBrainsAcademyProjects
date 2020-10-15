A, B, H = int(input()), int(input()), int(input())

if A <= H:
    if H <= B:
        print("Normal")
    else:
        print("Excess")
else:
    print("Deficiency")
