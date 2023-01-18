def ertekeles():
    etel = input("Étel neve: ")
    rendelo = input("Étel rendelőjének neve: ")
    ertek = int(input('Értékelés (1-5): '))
    if (ertek < 0):
        print("Az értékelés nem lehet negatív!")
    elif (ertek > 5):
        print("5 pont feletti értékelés nem elfogadható!")
    elif (ertek == 0):
        print("0 pont értékelés nem adható")
    else:
        print("Köszönjük az értékelést! ")



