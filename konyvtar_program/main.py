from konyvtar.modulok import adatok_beolvasasa, adatok_mentese, uj_konyv_hozzaadasa, konyvek_listazasa, kereses, modositas, torles

FAJLNEV = "konyvek.json"

konyvek = adatok_beolvasasa(FAJLNEV)

print("Üdvözöllek kedves olvasó!", sep = "\n" )

new_book = "Új könyv hozzáadása"
lista = "Könyveim listázása"
search = "Keresés"
mod = "Könyv adatainak vagy állapotának módosítása"
torl = "Könyv törlése"
ex = "Kilépés"
menu = [new_book, lista, search, mod, torl, ex]

while True:
    print("------------------------------",
    "\nVálassz az alábbi menüből!"
    "\nFőmenü: ")
    for i, szo in enumerate(menu):
        print(f"{i+1}. {szo}")        
    valasztas = input("Add meg a választott menü számát: ")

    if valasztas == "1":
        print(f"\n{new_book} kiválasztva")
        uj_konyv_hozzaadasa(konyvek)
        adatok_mentese(FAJLNEV,konyvek)

    elif valasztas == "2":
        print(f"\n{lista} kiválasztva")
        konyvek_listazasa(konyvek)

    elif valasztas == "3":
        print(f"\n{search} kiválasztva")
        kereses(konyvek)

    elif valasztas == "4":
        print(f"\n{mod} kiválasztva")
        modositas(konyvek)
        adatok_mentese(FAJLNEV,konyvek)
    elif valasztas == "5":
        print(f"\n{torl} kiválasztva")
        torles(konyvek)
        adatok_mentese(FAJLNEV,konyvek)

    elif valasztas == "6":
        print(f"\nViszontlátásra!\n")
        break

    else:
        print("\nIlyen menüpont nincs, kérlek válassz a menüpontokból, 1-től 6-ig!")
       