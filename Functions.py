
def EmailRegex(Email):
    email = Email.lower()
    import time
    import re
    time.sleep(0.2)
    if check := re.fullmatch(r"^[a-z0-9]+[_.]?[a-z0-9]+[_.]?[a-z0-9]+@[a-z0-9]+\.?[a-z]*\.([a-z]{3}|[a-z]{2})", email):
        return check.group()

def AgeRegex(Age):
    import time
    import re
    time.sleep(.2)
    if match := re.fullmatch(r"^[1-9][8-9]|[2-9][0-9]|1[0-5][0-9]",Age):
        return match.group()

def PhoneNumber(item):
    import re
    import time
    time.sleep(0.2)
    if match := re.fullmatch("\+234[7-9][0-1][0-9]{8}|0[7-9][0-1][0-9]{8}", item):
        return match.group()

def insert(FirstName, SurName, Phone, Age,  EmailAddress, Pin, PrivateKey, PublicKey):
    import sqlite3
    import time
    try:

        conn = sqlite3.connect('USER DETAILS.db')
        cur = conn.cursor()
        cur.execute('INSERT INTO UserInfoTable VALUES (?, ?, ?, ?, ?, ?)',
                    (FirstName, SurName, Phone, Age, EmailAddress, 0))
        conn.commit()
        conn.close()

        time.sleep(2)

        conn = sqlite3.connect('USER DETAILS.db')
        cur = conn.cursor()
        cur.execute('INSERT INTO UserLogTable VALUES (?, ?, ? ,?)', (Phone, Pin, PrivateKey, PublicKey))
        conn.commit()
        conn.close()

    except sqlite3.OperationalError:
        return 'OperationalError'

def languages(item):
    lan = ['afrikaans' 'albanian', 'amharic', 'arabic', 'armenian', 'assamese', 'aymara', 'azerbaijani',
           'bambara', 'basque', 'belarusian', 'bengali', 'bhojpuri', 'bosnian', 'bulgarian', 'catalan', 'cebuano',
           'chichewa', 'chinese', 'chinese', 'corsican', 'croatian', 'czech', 'danish', 'dhivehi', 'dogri', 'dutch',
           'english', 'esperanto', 'estonian', 'ewe', 'filipino', 'finnish', 'french', 'frisian', 'galician',
           'georgian',
           'german', 'greek', 'guarani', 'gujarati', 'haitian', 'hausa', 'hawaiian', 'hebrew', 'hindi', 'hmong',
           'hungarian', 'icelandic', 'igbo', 'ilocano', 'indonesian', 'irish', 'italian', 'japanese', 'javanese',
           'kannada', 'kazakh', 'kinyarwanda', 'konkani', 'korean', 'krio', 'kurdish', 'kurdish', 'kyrgyz',
           'lao', 'latin', 'latvian', 'lingala', 'lithuanian', 'luganda', 'luxembourgish', 'macedonian', 'maithili',
           'malagasy', 'malay', 'malayalam', 'maltese', 'maori', 'marathi', 'meiteilon (manipuri)', 'mni-Mtei',
           'mizo',
           'mongolian', 'myanmar', 'nepali', 'norwegian', 'odia (oriya)', 'oromo', 'pashto', 'persian', 'polish',
           'portuguese', 'punjabi', 'quechua', 'romanian', 'russian', 'samoan', 'sanskrit', 'scots gaelic',
           'sepedi',
           'serbian', 'sesotho', 'shona', 'sindhi', 'sinhala', 'slovak', 'slovenian', 'somali', 'spanish',
           'sundanese',
           'swahili', 'swedish', 'tajik', 'tamil', 'tatar', 'telugu', 'thai', 'tigrinya', 'tsonga', 'turkish',
           'turkmen',
           'twi', 'ukrainian', 'urdu', 'uyghur', 'uzbek', 'vietnamese', 'welsh', 'xhosa', 'yiddish', 'yoruba',
           'zulu']
    if item in lan:
        return item

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

def Registration():
    import time
    error = ''
    FirstName = ''
    surname = ''
    age = ''
    phone = ''
    email = ''
    while True:
        if error == 'Q':
            break
        try:
            firstName = input("Enter First Name or Q to quit: ").title().strip()
            if firstName.isalpha() and firstName == 'Q':
                print('Process Cancelled.')
                break

            if not firstName.isalpha() or len(firstName) < 2:
                print("Invalid Name format.")
                firstName = input("Re-enter First Name: ").title().strip()
            if not firstName.isalpha() or len(firstName) < 2:
                print("Invalid Name format.")
                firstName = input("Re-enter First Name: ").title().strip()
            if not firstName.isalpha() or len(firstName) < 2:
                print("Invalid name format.")
                firstName = input("Re-enter First Name: ").title().strip()
            if not firstName.isalpha() or len(firstName) < 2:
                print("Invalid name format.")
                continue
            FirstName += firstName

            Surname = input("Enter Surname 'Q' to quit: ").title().strip()
            if Surname.isalpha() and Surname == 'Q':
                print('process cancelled.')
                break
            if not Surname.isalpha() or len(Surname) < 2:
                print("Invalid name Format.")
                Surname = input("Re-enter Surname only Alphabet: ").title().strip()
            if not Surname.isalpha() or len(Surname) < 2:
                print("Invalid name format")
                Surname = input("Ee-enter Surname [A-Z]: ").title().strip()
            if not Surname.isalpha() or len(Surname) < 2:
                print("Invalid name format.")
                Surname = input("Re-enter Surname: ").title().strip()
            if not Surname.isalpha() or len(Surname) < 2:
                print("Invalid name format.")
                continue
            surname += Surname

            Age = input("Enter Age or 0 to quit: ").strip()
            if Age.isdigit() and Age == '0':
                print('Process cancelled')
                break

            if AgeRegex(Age) is None:
                print("Unexpected age value. It seems you're blow 18 years old or off expected age limit of 159 years.")
                Age = input("Re-enter Age [18 - 159]: ").strip()
            if AgeRegex(Age) is None:
                print("Unexpected age value .")
                Age = input("Re-enter Age [18 - 159]: ").strip()
            if AgeRegex(Age) is None:
                print("Unexpected age value.")
                Age = input("Re-enter age [18 - 159]: ").strip()
            if AgeRegex(Age) is None:
                print("We sorry it appears you are not old enough..")
                continue
            age += Age

            Phone = input("Enter Phone 0 to quit: ").strip()
            if Phone == '0':
                print('Process Cancelled.')
                break

            if PhoneNumber(Phone) is None:
                print("Invalid Nig phone Format.")
                Phone = input("Re-enter Nig Phone Number: ").strip()
            if PhoneNumber(Phone) is None:
                print("Invalid Nig phone Format.")
                Phone = input("Re-enter Nig Phone Number: ").strip()
            if PhoneNumber(Phone) is None:
                print("Invalid Nig phone Format.")
                Phone = input("Re-enter Nig Phone Number: ").strip()
            if PhoneNumber(Phone) is None:
                print("Invalid Nig phone Format.")
                continue
            phone += Phone

            Email = input("Enter Email or Q to quit: ").lower().strip()
            if Email.upper() == 'Q':
                print('Process cancelled')
                break
            if EmailRegex(Email) is None:
                print("Invalid email Format.")
                Email = input("Re-enter email accept[a-z 0-9 . _]: ").lower().strip()
            if EmailRegex(Email) is None:
                print("Invalid email Format.")
                Email = input("Re-enter email accept[a-z 0-9 . _]: ").lower().strip()
            if EmailRegex(Email) is None:
                print("Invalid email Format.")
                Email = input("Re-enter email accept[a-z 0-9 . _]: ").lower().strip()
            if EmailRegex(Email) is None:
                print("Invalid Nig phone Format.")
                continue
            email += Email
            break
        except KeyboardInterrupt:
            print('Program terminated.')
            break

    if len(email) > 0:
        print("Working on it...")
        time.sleep(1)
        keys = GenerateCode()
        Pin = keys[0]
        PrivateKey = keys[1]
        PublicKey = keys[2]

        Error = insert(FirstName, surname, phone, age, email, Pin, PrivateKey, PublicKey)
        if Error is None:
            print('print registration completed')
            print(f"Dear {FirstName}, \nyour longin details are:")
            print(f"Public key: {PublicKey}")
            print(f"Private key: {PrivateKey}")
            print(f"Pin: {Pin}")
            print("You will need them for authentication.")
        else:
            error += 'Q'
            print('Error occurred.')

def Translator():
        import pandas as pd
        import time
        from deep_translator import GoogleTranslator
        while True:
            try:
                try:
                    num = eval(input("From 1-3, how many languages would you like to be translated at once? or enter 0 to exit:"))
                except NameError:
                    print(f"Invalid selection")
                    continue
                except SyntaxError:
                    print("Emptiness...")
                    continue
                if num == 0:
                    print("Quiting...")
                    time.sleep(2)
                    break
                elif num > 3:
                    print("Were are sorry we can't translate more three languages at once at the moment")
                    continue
                if num == 1:
                    source = input("""ENTER THE SOURCE LANGUAGE OR "Q" TO QUIT : """).lower().strip()
                    if source == 'q':
                        print("Quiting")
                        time.sleep(2)
                        break
                    lan = input("""ENTER THE TARGET LANGUAGE OR "Q" TO QUIT : """).lower().strip()
                    if lan == 'q':
                        print("Quiting")
                        time.sleep(2)
                        break
                    text = input("""ENTER THE TEXT TO BE TRANSLATED OR "Q" TO QUIT : """).lower().strip()
                    if text == 'q':
                        print("Quiting")
                        time.sleep(2)
                        break

                    if len(text) == 0:
                        print("Empty text input are not allowed.")
                        time.sleep(2)
                        continue

                    if text[0].isdigit():
                        print("Unexpected value: Text does not start with digit.")
                        continue
                    if languages(source) is None or languages(lan) is None:
                        time.sleep(2)
                        print('We are sorry one or more of the languages are not available for translation.')
                        continue
                    else:
                        lang = {}

                        def trans(source, target, text):
                            translated = GoogleTranslator(source= source, target=target).translate(text)
                            lang[target.title()] = translated
                            print(lang)

                        trans(source,lan, text)
                        try:
                            f = open('TranslationNote.txt', 'a')
                            f.write(f"\n{source.title()}={lang}")
                            f.close()
                        except UnicodeEncodeError:
                            print("UnicodeEncodeError occurred. ")
                        except NameError:
                            print("NameError occurred")

                        Source = ([source])
                        Target = list(lang)
                        word = (list(lang.values()))
                        TranslationTable = pd.DataFrame({'Source': Source, 'Target': Target, 'Text': word})
                        TranslationTable.index = TranslationTable.index + 1
                        print(TranslationTable)
                        try:
                            TranslationTable.to_csv("TranslationTable.csv")
                        except PermissionError:
                            print('Permission denied')

                elif num == 2:
                    source1 = input("""ENTER THE SOURCE LANGUAGE OR "Q" TO QUIT : """).lower().strip()
                    if source1 == 'q':
                        print("Quiting")
                        time.sleep(2)
                        break
                    lan1 = input("""ENTER THE TARGET LANGUAGE OR "Q" TO QUIT : """).lower().strip()
                    if lan1 == 'q':
                        print("Quiting")
                        time.sleep(2)
                        break
                    lan2 = input("""ENTER THE TARGET LANGUAGE OR "Q" TO QUIT : """).lower().strip()
                    if lan2 == 'q':
                        print("Quiting")
                        time.sleep(2)
                        break
                    text = input("""ENTER THE TEXT TO BE TRANSLATED OR "Q" TO QUIT : """).lower().strip()
                    if text == 'q':
                        print("Quiting")
                        time.sleep(2)
                        break

                    if len(text) == 0:
                        print("Empty text input are not allowed.")
                        continue

                    if text[0].isdigit():
                        print("Unexpected value: Text does not start with digit.")
                        continue

                    if languages(source1) is None or languages(lan1) is None or languages(lan2) is None:
                        time.sleep(2)
                        print('We are sorry one or more of the languages are not available for translation.')
                        continue
                    else:
                        lang2 = {}

                        def trans1(source1, target, text):
                            translated = GoogleTranslator(source=source1, target=target).translate(text)
                            lang2[target.title()] = translated
                            print(lang2)

                    trans1(source1,lan1, text)
                    trans1(source1,lan2, text)
                    try:
                        f = open('TranslationNote.txt', 'a')
                        f.write(f"\n{source1.title()}={lang2}")
                        f.close()
                    except UnicodeEncodeError:
                        print("UnicodeEncodeError occurred. ")
                    except NameError:
                        print("NameError occurred")

                    Source = ([source1, source1])
                    Target = list(lang2)
                    word = (list(lang2.values()))
                    TranslationTable = pd.DataFrame({'Source': Source, 'Target': Target, 'Text': word})
                    TranslationTable.index = TranslationTable.index + 1
                    print(TranslationTable)
                    try:
                        TranslationTable.to_csv("TranslationTable.csv")
                    except PermissionError:
                        print('Permission denied')

                elif num == 3:
                    source2 = input("""ENTER THE SOURCE LANGUAGE OR "Q" TO QUIT : """).lower().strip()
                    if source2 == 'q':
                        print("Quiting...")
                        time.sleep(2)
                        break
                    lan1 = input("""ENTER THE TARGET LANGUAGE OR "Q" TO QUIT : """).lower().strip()
                    if lan1 == 'q':
                        print("Quiting...")
                        time.sleep(2)
                        break
                    lan2 = input("""ENTER THE TARGET LANGUAGE OR "Q" TO QUIT : """).lower().strip()
                    if lan2 == 'q':
                        print("Quiting...")
                        time.sleep(2)
                        break
                    lan3 = input("""ENTER THE TARGET LANGUAGE OR "Q" TO QUIT : """).lower().strip()
                    if lan3 == 'q':
                        print("Quiting...")
                        time.sleep(2)
                        break
                    text = input("""ENTER THE TEXT TO BE TRANSLATED OR "Q" TO QUIT : """).lower().strip()
                    if text == 'q':
                        print("Quiting...")
                        time.sleep(2)
                        break

                    if len(text) == 0:
                        print("Enpty text input are not allowed.")
                        continue

                    if text[0].isdigit():
                        print("Unexpected value: Text does not start with digit.")
                        continue
                    if languages(source2) is None or languages(lan1) is None or \
                            languages(lan2) is None or languages(lan3) is None:
                        time.sleep(2)
                        print('We are sorry one or more of the languages are not available for translation.')
                        continue
                    else:
                        lang3 = {}
                        
                        def trans3(source2, target, text):
                            translated = GoogleTranslator(source=source2, target=target).translate(text)
                            lang3[target.title()] = translated
                            print(lang3)

                    trans3(source2, lan1, text)
                    trans3(source2,lan2, text)
                    trans3(source2, lan3, text)

                    try:
                        f = open('TranslationNote.txt', 'a')
                        f.write(f"\n{source2.title()}={lang3}")
                        f.close()
                    except UnicodeEncodeError:
                        print("UnicodeEncodeError occurred. ")
                    except NameError:
                        print("NameError occurred")

                    Source = ([source2, source2, source2])
                    Target = list(lang3)
                    word = (list(lang3.values()))
                    TranslationTable = pd.DataFrame({'Source': Source, 'Target': Target, 'Text': word})
                    TranslationTable.index = TranslationTable.index + 1
                    print(TranslationTable)
                    try:
                        TranslationTable.to_csv("TranslationTable.csv")
                    except PermissionError:
                        print('Permission denied')
            except KeyboardInterrupt:
                print('Error occurred. Program terminated.')
                break

def generateKey():
    import time
    import sqlite3
    Quit = ''
    Pin = ''
    PrivateKey = ''
    PublicKey = ''
    name = ''
    Phone = ''
    brake = ''
    while True:
        try:
            if brake == 'Q':
                break
            phone = input("""Enter your phone number to generate new login details or "E" to Exit: """).strip()
            print("Working on it...")
            if phone == 'e' or phone == 'E':
                Quit += phone.upper()
                time.sleep(1)
                break
            time.sleep(1)
            conn = sqlite3.connect('USER DETAILS.db')
            cur = conn.cursor()
            cur.execute(f"SELECT * FROM UserInfoTable WHERE Phone = '{phone}'")
            records = cur.fetchall()
            if len(records) == 0:
                print("Invalid phone number")
                continue
            else:
                for items in records:
                    if phone == items[2]:
                        Phone += phone
                        name += items[0]
                        keys = GenerateCode()
                        Pin += keys[0]
                        PrivateKey += keys[1]
                        PublicKey += keys[2]
                        brake += 'Q'
            if Quit == 'E' or len(Phone) == 0:
                print('Process cancelled.')
            else:
                conn2 = sqlite3.connect('USER DETAILS.db')
                cur2 = conn2.cursor()
                cur2.execute('INSERT INTO UserLogTable VALUES (?, ?,? ,?)', (Phone, Pin, PrivateKey, PublicKey))
                conn2.commit()
                conn2.close()
                print(f"Dear {name}, \nyour longin details are:")
                print(f"Public key: {PublicKey}")
                print(f"Private key: {PrivateKey}")
                print(f"Pin: {Pin}")
                print("You will need them for authentication.")
        except KeyboardInterrupt:
            print("Program terminated")
            break
        except sqlite3.OperationalError:
            print('Error occurred')
            break

def Login():
    import sqlite3
    brQ = ''
    while True:
        try:
            import time
            if brQ == 'Q':
                break
            PubKy = input("""Enter your Public key to Login or "Q" to Quit: """).strip()
            if PubKy.upper() == 'Q':
                brQ += 'Q'
                print('Quiting...')
                time.sleep(0.5)
                break
            else:
                PinPrKy = input("Enter private key: ").strip()
                pin = input("Enter your pin: ").strip()
                print("Working on it...")
                time.sleep(0.5)
                validKeys = []
                name = ''
                phone = ''
                count = 1
                conn = sqlite3.connect('USER DETAILS.db')
                cur = conn.cursor()
                cur.execute(f"SELECT * FROM UserLogTable WHERE PublicKey = '{PubKy}'")
                records = cur.fetchall()
                for items in records:
                    phone += items[0]
                    for x in items:
                        if PinPrKy == x or pin == x:
                            validKeys.append(x)
                        time.sleep(0.5)
                conn = sqlite3.connect('USER DETAILS.db')
                cur = conn.cursor()
                cur.execute(f"SELECT * FROM UserInfoTable WHERE Phone == '{phone}'")
                records1 = cur.fetchall()
                for items in records1:
                    name += (items[0])
                    count += int((items[5]))
                if len(validKeys) > 1:
                    conn = sqlite3.connect('USER DETAILS.db')
                    cur = conn.cursor()
                    cur.execute(f"Update UserInfoTable SET LoginCount == '{count}' WHERE Phone == '{phone}'")
                    conn.commit()
                    conn.close()
                    print(f"Welcome {name},")
                    time.sleep(1)
                    Translator()
                    break
                else:
                    print("Invalid authentication details.")
                    continue
        except KeyboardInterrupt:
            print('Program terminated.')
        except sqlite3.OperationalError:
            print('Error occurred.')
            break












