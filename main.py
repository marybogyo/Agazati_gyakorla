import ertekel
import pogyasz1
import sorozat
from Pogyasz import Pogyasz


#ertekel.ertekeles()
sorozat.paratlan()
sorozat.paratlanok_szama()
sorozat.konzol_kiir()
sorozat.fajba_kiir()

pogyaszok = pogyasz1.beolvas()
lmp = pogyasz1.magassag(pogyaszok)
print(f"A legmagasabb pogyász méretei:{lmp.szelesseg}x{lmp.magassag}x{lmp.melyseg},súlya: {lmp.suly} kg.")
