
def EmailRegex(Email):
    email = Email.lower()
    import time
    import re
    time.sleep(0.2)
    if check := re.fullmatch(r"^[a-z0-9]+.?[a-z0-9]*.?[a-z0-9]*@[a-z0-9.]+[a-z]+(\.[a-z]+)$", email):
        return check.group()

#print(EmailRegex("ma.la@cs50.harvard.com"))
