
def PhoneNumber(item):
    import re
    import time
    time.sleep(0.2)
    validPhone = ''
    x = re.fullmatch("\+234[7-9][0-1][0-9]{8}|0[7-9][0-1][0-9]{8}", item)
    if x:
        validPhone += item

    if len(validPhone) > 1:
        return item


# PhoneNumber('+09089026573')


