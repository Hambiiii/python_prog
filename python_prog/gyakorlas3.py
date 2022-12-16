x = int(input("Add meg a pontszámod"))
print(x)

if x < 50:
    print("elégtelen")
elif x >= 50 and x<60:
    print("elégséges")
elif x >= 60 and x<70:
    print("közepes")
elif x >= 70 and x<85:
    print("jó")
elif x >= 85 and x<100:
    print("jeles")

else:
    print("nem megfelelő a megadott szám")
 
    
    

 