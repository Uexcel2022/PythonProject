
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
                    from Translator import Translator
                    Translator()
                else:
                    print("Invalid authentication details.")
                    continue
        except KeyboardInterrupt:
            print('Program terminated.')
        except sqlite3.OperationalError:
            print('Error occurred.')
            break


# Login()


