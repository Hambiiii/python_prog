lista = [] #üres lista

lista.append("Fifa")
lista.append("Fortnite")
lista.append("COD")
lista.append("LOL")
lista.append("God of War")
lista.append("GTA")



#kiíratás 3 féle képpen
#1.
print(lista)

print("*******************************************")

#2.
for item in lista:
    print(item)

#3.
for i in range(len(lista)):
    print(lista[i])

print("*****************************************")

#szűrés
for item in lista:
    if item == "COD":
        print("IGEN")
else :
    print("NO")
        
print("*******************************************")