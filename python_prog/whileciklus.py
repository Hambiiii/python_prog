#eddig tanult ciklusok:
#  for i in range()
#for item i <lista>:

# i = 0
# while i < 6:
#     print(i)
#     i = i + 1



# lista = [1,2,3,4,5,6,7,8,9,10]
# i = 0
# while i < len(lista):
#     print(lista[i],end=' ')
#     i += 1

varosok = ["Pécs","Debrecen","Dabas","Sopron","Szeged","Budapest","Székesfehérvár",]
print(varosok)
print("***************************")
#Írassuk ki azokat a VÁROSOKAT Amelyek D betűvel kezdödnek
for i in range (len(varosok)):
    if varosok[i].startswith("D"):
        print(varosok[i])
print("***************************")
for item in varosok:
    if item.startswith("D"):
        print(item)