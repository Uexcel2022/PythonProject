
def EmailRegex(Email):
    email = Email.lower()
    import time
    import re
    time.sleep(0.2)
    if check := re.fullmatch("[a-z0-9]*[._]?[a-z0-9]+[_.]?[a-z0-9]+[@][a-z]+[.]?[a-z]*[.][a-z]+", email):
        return check.group()


#EmailRegex("k.ez_902@gmail.com")
