
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
            from AgeRegex import AgeRegex
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
            from PhoneRegex import PhoneNumber
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
            from EmailRegex import EmailRegex
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
        from LoginDetailsGen import GenerateCode
        keys = GenerateCode()
        Pin = keys[0]
        PrivateKey = keys[1]
        PublicKey = keys[2]

        from Insert import insert
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


# Registration()




