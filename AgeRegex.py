def AgeRegex(Age):
    import time
    import re
    time.sleep(.2)
    if match := re.fullmatch(r"^[1-9][8-9]|[2-9][0-9]|1[0-5][0-9]",Age):
        return match.group()

#AgeRegex('18')

