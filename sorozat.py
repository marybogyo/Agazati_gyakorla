import random
def paratlan():

    dollar = ""
    i = 0
    while i < 12:
        vel = int(random.random() * 1001) - 10
        if i == 11:
            dollar += str(vel) + ""
        else:
            dollar += str(vel) +"$"
        i += 1
    print(dollar)
    return dollar


def paratlanok_szama():
    i = 0
    lista_m = paratlan()
    lista = lista_m.split("$")
    ossz_db = 0
    while i < len(lista):
        if int(lista[i]) % 2 != 0:
            ossz_db += 1
        i += 1
    return ossz_db

def konzol_kiir():
    osszesen = paratlanok_szama()
    print(f"A páratlan számok száma: {osszesen}")

    return osszesen
def fajba_kiir():
    kon = konzol_kiir()
    fajl = open("eredmeny.txt", "w", encoding="utf-8")
    fajl.write(f" A páratlan számok száma: {str(kon)}")
    fajl.close()
    print(fajl)
