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
            conn = sqlite3.connect('USERS BIODATA.db')
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
                        from LoginDetailsGen import GenerateCode
                        keys = GenerateCode()
                        Pin += keys[0]
                        PrivateKey += keys[1]
                        PublicKey += keys[2]
                        brake += 'Q'
            if Quit == 'E' or len(Phone) == 0:
                print('Process cancelled.')
            else:
                conn2 = sqlite3.connect('USERS BIODATA.db')
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
        except sqlite3.OperationalError as err:
            print('OperationalError: ', err)
            break


# generateKey()
