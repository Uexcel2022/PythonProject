
def EmailRegex(Email):
    email = Email.lower()
    import time
    import re
    time.sleep(0.2)
    validEmail = ''
    accept = "[a-z0-9]*[._]?[a-z0-9]+[_.]?[a-z0-9]+[@][a-z]+[.]?[a-z]*[.][a-z]+"
    check = re.fullmatch(accept, email)
    if check:
        validEmail += email
    if len(validEmail) > 0:

        return validEmail


# EmailRegex("yt@gmail.com")
