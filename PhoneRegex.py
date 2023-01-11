
def PhoneNumber(item):
    import re
    import time
    time.sleep(0.2)
    if match := re.fullmatch("\+234[7-9][0-1][0-9]{8}|0[7-9][0-1][0-9]{8}", item):
        print(match.group())
        return match.group()

# PhoneNumber('09089026570')


