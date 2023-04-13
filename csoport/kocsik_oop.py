class Kocsik:
    def __init__ (self,nev,ev,loero):
        self.nev = nev
        self.ev = ev
        self.loero = loero

fajl = open("autok.txt", "r", encoding="UTF-8")
    
autok_lista = []
for sorok in fajl:
    oszlop = sorok.strip().split("  ")
    autok_lista.append(Kocsik(oszlop[0],oszlop[1], oszlop[2]))
for item in autok_lista:
    print(f"Név {item.nev}  Év:{item.ev}    Lóerő:{item.loero}")


