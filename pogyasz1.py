from Pogyasz import Pogyasz

def beolvas():
   csomag_fajl = open("csomag.txt", "r", encoding="utf-8")
   csomag_fajl.readline()
   csom = csomag_fajl.readlines()
   csomag_fajl.close()
   print(csom)
   i = 0
   pogyaszok = []
   while i< len(csom):
      pogyaszok.append(Pogyasz(csom[i].strip().split("#")))
      i +=1
   pogyaszok_szama(pogyaszok)
   otvenegycm_pogyaszok(pogyaszok)
   #magassag(pogyaszok)

   return pogyaszok

def pogyaszok_szama(csom):
   print(f"A pogyászok száma: {len(csom)} pogyaszok_szama")


def otvenegycm_pogyaszok(csom):
   i = 0
   sulya = 0
   otvenegy = 0
   while i < len(csom):
      if csom[i].szelesseg == 51:
         otvenegy += 1
         sulya += csom[i].suly
      i += 1
   atlag = sulya / otvenegy
   print(f"Az 51 cme-es poggyászok átlag súlyértéke: {int(atlag * 1000)} g")


def magassag(pogyasz):
   i = 1
   legmagasabb = pogyasz[0]

   while i < len(pogyasz):
      if pogyasz[i].magassag > legmagasabb.magassag:
         legmagasabb = pogyasz[i]
      i += 1

   return legmagasabb