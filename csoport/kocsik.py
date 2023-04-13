with open("autok.txt", "r", encoding="UTF-8") as fajl:
    autok = [a.strip().split("  ") for a in fajl]


print(autok)

print("******************************************************************************************************************************")

autok_szama = 0
for auto in autok:
    autok_szama = autok_szama + 1
print(f"A garázsban lévő autók száma: {autok_szama} db")

print("******************************************************************************************************************************")


oloero = 0
for auto in autok:
    oloero = oloero + int(autok[2])
print(oloero)
    