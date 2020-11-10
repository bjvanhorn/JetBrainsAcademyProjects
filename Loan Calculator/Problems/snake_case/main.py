phrase_camel = input()
phrase_snake = str()
for i in phrase_camel:
    if i.isupper():
        phrase_snake = phrase_snake + '_' + i.lower()
    else:
        phrase_snake = phrase_snake + i
print(phrase_snake)
