# Hangman-Spiel mit Strichmännchen

def hangman_malen(fehler):
    fortschritt = [
        '''
           -------
           |     |
           |     
           |     
           |     
           |     
        ''',
        '''
           -------
           |     |
           |     O
           |     
           |     
           |     
        ''',
        '''
           -------
           |     |
           |     O
           |     |
           |     
           |     
        ''',
        '''
           -------
           |     |
           |     O
           |    /|
           |     
           |     
        ''',
        '''
           -------
           |     |
           |     O
           |    /|\\
           |     
           |     
        ''',
        '''
           -------
           |     |
           |     O
           |    /|\\
           |    /  
           |     
        ''',
        '''
           -------
           |     |
           |     O
           |    /|\\
           |    / \\
           |     
           -GAME OVER-
        '''
    ]

    return fortschritt[fehler]
# Hangman-Spiel


def hangman(wort):
    fehler = 0
    max_fehler = 6
    geratene_buchstaben = [" ", "-", "!"]
    wort = wort.upper()
    while fehler < max_fehler:
        angezeigtes_wort = ""
        for buchstabe in wort:
            if buchstabe in geratene_buchstaben:
                angezeigtes_wort += buchstabe
            else:
                angezeigtes_wort += "_"
        print(angezeigtes_wort)
        print(hangman_malen(fehler))
        if angezeigtes_wort == wort:
            print("Gewonnen, das Wort war:", wort)
            break
        eingabe = input("Rate einen Buchstaben: ").upper()
        if eingabe in geratene_buchstaben:
            print("Du hast diesen Buchstaben bereits getippt.")
        elif eingabe in wort:
            print("Richtig geraten!")
        else:
            fehler += 1
            print("Leider falsch geraten", max_fehler - fehler, "Versuche übrig")
        geratene_buchstaben.append(eingabe)
    if fehler >= max_fehler:
        print(hangman_malen(fehler))
        print("Verloren, das Wort war:", wort)


if __name__ == '__main__':
    zu_ratendes_wort = "Hangman"
    hangman(zu_ratendes_wort)