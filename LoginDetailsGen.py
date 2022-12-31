def GenerateCode():
    from string import printable
    from random import randint
    pin = str(randint(1000, 9999))
    userPrbKey = ''
    for i in range(7):
        rand = randint(10, 61)
        key = printable[rand]
        userPrbKey += key

    userPubKey = ''
    for i in range(10):
        rand = randint(10, 61)
        key = printable[rand]
        userPubKey += key

    return pin, userPrbKey, userPubKey

