def Translator():
    import pandas as pd
    import time
    from deep_translator import GoogleTranslator
    while True:
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
            from languages import languages
            if languages(source) is None or languages(lan) is None:
                time.sleep(2)
                print('We are sorry one or more of the languages are not available for translation.')
                continue
            else:
                lang = {}

                def trans(source, target, text):
                    translated = GoogleTranslator(source= source, target=target).translate(text)
                    lang[target.title()] = translated

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

            from languages import languages
            if languages(source1) is None or languages(lan1) is None or languages(lan2) is None:
                time.sleep(2)
                print('We are sorry one or more of the languages are not available for translation.')
                continue
            else:
                lang2 = {}

                def trans1(source1, target, text):
                    translated = GoogleTranslator(source=source1, target=target).translate(text)
                    lang2[target.title()] = translated

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
            from languages import languages
            if languages(source2) is None or languages(lan1) is None or languages(lan2) is None or \
                    languages(lan3) is None:
                time.sleep(2)
                print('We are sorry one or more of the languages are not available for translation.')
                continue
            else:
                lang3 = {}

                def trans3(source2, target, text):
                    translated = GoogleTranslator(source=source2, target=target).translate(text)
                    lang3[target.title()] = translated

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


#Translator()
