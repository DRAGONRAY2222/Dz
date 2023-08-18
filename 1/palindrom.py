

def palindrom():
    word = str(input('Введите слово: '))
    drow = word[::-1]
    if word == drow:
        return True
    else:
        return False

print(palindrom())