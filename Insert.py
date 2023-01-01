
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





