while True:
    pwd = input('Введите пароль: ')
    isupper = False
    islower = False

    for char in pwd:
        if char.islower():
            islower = True
        elif char.isupper():
            isupper = True

    if len(pwd) > 8 and isupper and islower:
        print('Пароль: Oк')
        break
    else:
        print('Пароль слишком простой')


