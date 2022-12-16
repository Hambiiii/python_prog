# szoveg = "ezegyszöveg"
# if "v" in szoveg:
#     print("benne van")
# else:
#     print("nincs")
# print("*************************")
# szoveg = "ezegyszöveg"
# beker = input("Kérem a betűt: ")
# if beker in szoveg:
#     print(f"{beker} betű benne van a szövegben")
# else:
#     print(f"{beker} betü nincsen benn a szövegben")


# hetnapjai = ["hétfő", "kedd", "szerda", "csütörtök", "péntek", "szombat", "vasárnap"]
# if beker in hetnapjai:
#     print(f"{beker} nap bennevan a listában")
# else:
#      print(f"{beker} nap nincsen a listában")
    

# hetnapjai = ["hétfő", "kedd", "szerda", "csütörtök", "péntek", "szombat", "vasárnap"]
# hetnapjai_kisbetu = [item.lower() for item in hetnapjai]
# hetnapjai_nagybetu = [item.upper() for item in hetnapjai]
# beker = input("Kérem a napot! ").upper()

# if beker in hetnapjai_kisbetu:
#     print(f"{beker} nap bennevan a listában")
# else:
#      print(f"{beker} nap nincsen a listában")


kocsi = ["Audi", "ferrai", "suzuki", "bmw", "volvo", "smart", "opel"]
kocsi_kisb = [item.lower() for item in kocsi]
beker = input("Kérek egy kocsimárkát: ").lower()
if beker in kocsi_kisb:
    print(f"{beker} bent áll a garázsban:)")
else:
    print(f"{beker} nincsen a garázsban:(")








