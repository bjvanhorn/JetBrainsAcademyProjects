score, maximum_score = int(input()), int(input())
percent_score = score / maximum_score
if percent_score < 0.6:
    print("F")
elif percent_score < 0.7:
    print("D")
elif percent_score < 0.8:
    print("C")
elif percent_score < 0.9:
    print("B")
else:
    print("A")
