
print('Welcome to One-World Translation....')

def LogIN():
    import Functions
    import time
    while True:
        try:
            time.sleep(1)
            options = input("""Enter "L" to login, "R" to register or "N" to get new log in details "Q" to Quit: """).upper()
            print('Working on it...')
            time.sleep(1)
            if options == 'Q':
                print('Quiting...')
                time.sleep(2)
                break
            if options == 'L':
                Functions.Login()
                time.sleep(0.5)
                continue

            elif options == 'R':
                Functions.Registration()
                time.sleep(0.5)
                continue

            elif options == 'N':
                Functions.generateKey()
                time.sleep(0.5)
                continue

            else:
                print('No valid option selected')
        except KeyboardInterrupt:
            print('Program terminated.')
            break


LogIN()
