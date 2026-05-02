from tabulate import tabulate

class Konyv:
    '''Könyv osztály'''
    #a konyv adatait határozza meg, amik a konyvben lesznek
    def __init__(self, szerzo, cim, isbn, allapot = "Elérhető"):
        #a felesleges szóközöket levágja és minden szót nagybetűvel kezdődővé tesz
        self.szerzo = szerzo.strip().title()
        #a felesleges szóközöket levágja és a cím első betűjét nagybetűvé teszi
        self.cim = cim.strip().capitalize()
        #felesleges szóközöket levágja
        self.isbn = isbn.strip()
        self.allapot = allapot
    #ha egy könyvet szeretnénk kiiratni ez mondja meg, hogyan nézzen ki amikor kiírja
    def __str__(self):
        '''A könyvek kilistázásához, ha ki szeretnénk írni'''
        return f"{self.szerzo} | {self.cim} | {self.isbn} | {self.allapot}"

    #metódus, amivel a szótárat létrehozza a könyvnek
    def szotarba (self): 
        return {"Szerző" : self.szerzo,
                "Cím" : self.cim,
                "ISBN" : self.isbn,
                "Állapot" : self.allapot}

#Az új könyv hozzáadását végző függvény
def uj_konyv_hozzaadasa (konyvek):
    '''Új könyvek hozzáadását végzi.'''
    print("Add meg a könyv adatait!")
    #bekéri a könyv adatait (az állapot alapértelmezetten "elérhető")
    szerzo = input("Szerző: ")
    cim = input("Cím: ")
    isbn = input("ISBN szám: ")
    #ellenőrzi van-e ilyen ISBN számú könyv a listában (egyedi azonosító, nem lehet kettő ugyanolyan)
    if isbn_foglalt(isbn, konyvek):
        print("\nHiba! Ilyen ISBN számú könyv már van a rendszerben!")
        return
    #egy változóba menti el az új könyv példányt
    uj_konyv = Konyv(szerzo, cim, isbn)
    #listába helyezi az új könyvet
    konyvek.append(uj_konyv)
    print(f"\nSikeresen hozzáadva: {cim}")

#A könyvek kilistázását végző függvény
def konyvek_listazasa(konyvek, uzenet = "Nincsenek még mentett könyveid"):
    '''Könyvek adatait kilistázza táblázatosan.'''
    if konyvek == []:  
        print(uzenet)
    else:
        #a könyveket a abc sorrendbe teszi szerző, cím, állapot szerint(ebben a sorrendben)
        rendezett_konyvek = sorted(konyvek, key = lambda k: (k.szerzo,k.cim,k.allapot))
        konyvek_listaja = []
        #a sorrendben levő könyveket szótárba alakítja és egy listába teszi
        for konyv in rendezett_konyvek:
            konyvek_listaja.append(konyv.szotarba())
        print("\nKönyveid: ")
        #a könyveket egy rácsos listában jeleníti meg
        print(tabulate(konyvek_listaja, headers = "keys", tablefmt = "grid"))

#A könyvek keresését végző függvény
def kereses (konyvek):
    '''A könyvek keresését végzi szerző, cím vagy állapot alapján. Szó részletekre is kiadja a találatokat.'''
    keresett_szo = input("Írd be a szerző nevét vagy a könyv címét! (Vagy annak egy részletét)").lower().strip()

    if not keresett_szo:
        print("\n Nem írtál be semmit a kereséshez!")
        return
    
    talalatok = []
    for konyv in konyvek:
        if keresett_szo in konyv.szerzo.lower() or keresett_szo in konyv.cim.lower():
            talalatok.append(konyv)
    konyvek_listazasa(talalatok, uzenet = f"Sajnos nincs ilyen találat!")


#Ellenőrzi, hogy a beírt ISBN szám benne van-e a rendszerben. Segédfüggvénye az uj_konyv_hozzaadasa és a modositas függvénynek.
def isbn_foglalt(uj_isbn, konyvek, megtalalt_konyv = None):
    '''Megnézi, hogy az ISBN szám már benne van-e a rendszerben, másik könyv által.'''
    for szam in konyvek:
        if szam.isbn == uj_isbn and szam != megtalalt_konyv:
            return True
    return False

#Ellenőrzi hogy egy eldöntendő kérdésre a megfelelő bemenetet kapta-e, ha nem, ezt jelzi a felhasználó felé. Segédfüggvénye a modositasok függvénynek.
def kerdes_dontes(valasz):
    ''''Eldöntendő kérdésre megnézi igen vagy nem a válasz. Ha nem megfelelő a bemenet, jelzi a felhasználó felé.'''
    while True:
        dontes = input(valasz).lower().strip()
        if dontes in ['i','n']:
            return dontes
        print("\nIlyen lehetőség nincs, kérlek válassz az alábbiakból: I (igen)/ N (nem)")

def kereses_valamihez(konyvek, muvelet_nev):
    '''Más függvényhez segít keresni ISBN szám alapján és ellenőrzi van-e ilyen a rendszerben.
    A kiírás paraméterben lehet definiálni milyen módosításhoz szeretnénk használni.'''
    azonosito = input(f"Add meg a {muvelet_nev} kívánt könyv ISBN számát: ").strip()
    for konyv in konyvek:
        if azonosito == konyv.isbn:
            return konyv
    return None

#Könyv adatainak (szerző, cím, ISBN) módosítását végző függvény. A modositas függvény segédfüggvénye.
def adat_modositas (megtalalt_konyv, konyvek):
    '''A könyv adatainak (szerző, cím, ISBN) módosításait végzi.'''
    mod = "Sikeres módosítás!" 
    #Bekéri a választ egy kérdésre, ellenőrzi helyes-e a bemenet és ha módosítani szeretne a felhasználó, elvégzi a módosítást.
    valasz = kerdes_dontes(f"\nSzeretnéd módosítani a szerző nevét? (Jelenleg: {megtalalt_konyv.szerzo} (I/N)")
    if valasz == "i":
        megtalalt_konyv.szerzo = input("Új szerző: ").title()
        print(f"\n{mod}")
    #Bekéri a választ egy kérdésre, ellenőrzi helyes-e a bemenet és ha módosítani szeretne a felhasználó, elvégzi a módosítást.
    valasz = kerdes_dontes(f"\nSzeretnéd módosítani a könyv címét? (Jelenleg: {megtalalt_konyv.cim}) (I/N)").lower()
    if valasz == "i":
        megtalalt_konyv.cim = input("Új cím: ").capitalize()
        print(f"\n{mod}")
    #Bekéri a választ egy kérdésre, ellenőrzi helyes-e a bemenet.
    valasz = kerdes_dontes(f"\nSzeretnéd módosítani a könyv ISBN számát? (Jelenleg: {megtalalt_konyv.isbn}) (I/N)").lower()
    if valasz == "i":
        uj_isbn = input("Új ISBN: ").strip()
        #Ellenőrzi az ISBN szám benne van-e a rendszerben, ha igen, ezt jelzi. Ha nem, elvégzi a módosítást.
        if isbn_foglalt(uj_isbn, konyvek, megtalalt_konyv):
            print("\nHiba! Ilyen ISBN számú könyv már van a rendszerben!")
        else:
            megtalalt_konyv.isbn = uj_isbn
            print(f"\n{mod}")

#Állapot módosítást végző függvény. A modositas függvény segédfüggvénye.                        
def allapot_modositas (megtalalt_konyv):
    '''Könyv állapotának módosítását végzi.'''
    mod = "Sikeres módosítás!"
    allapotok =["Elérhető", "Kölcsönadva", "Eladva", "Eltűnt"]
    print(f"Jelenlegi állapot: {megtalalt_konyv.allapot}")
    #Bekéri a választ egy kérdésre, ellenőrzi helyes-e a bemenet és ha módosítani szeretne a felhasználó, elvégzi a módosítást.
    uj_allapot = input(f"\nMi legyen a könyv állapota? \n Lehetséges állapotok: {allapotok}\nÚj állapot: ").strip().title()
    if uj_allapot in allapotok:
        megtalalt_konyv.allapot = uj_allapot
        print(f"\n{mod}")
    else:
        print("\nHiba! Ilyen állapot nincs!")             


#A könyv adatainak módosítását végzi
def modositas (konyvek):
    #ISBN szám alapján keres, mert ez egyedi
    megtalalt_konyv = kereses_valamihez(konyvek, "módosítani")
    #megnézi van-e ilyen könyv a rendszerben, ha igen megy tovább, ha nem, akkor kiírja, hogy nincs
    if megtalalt_konyv == None:
        print("\nIlyen könyv nem található.")
    #Választás a könyv módosítási lehetőségei közül.    
    else:
        while True:
            print("\nMit szeretnél módosítani?\n A: Könyv adatainak módosítása (szerző, cím, ISBN)\n " \
            "B: Könyv állapotának módosítása\n " \
            "C: Vissza a főmenübe")
            modositani = input("Add meg a választott módosítás betűjelét: ").lower()
            #Az adatokat itt módosítja.
            if modositani == "a":
                adat_modositas(megtalalt_konyv, konyvek)
            #Az állapotot itt módosítja.
            elif modositani == 'b':
                allapot_modositas(megtalalt_konyv)
            elif modositani == 'c':
                break
            else:
                print("\nIlyen menüpont nincs, kérlek válassz a menüpontokból, A, B vagy C!")

def torles(konyvek):
    megtalalt_konyv = kereses_valamihez(konyvek, "törölni")
    if megtalalt_konyv == None:
        print("\nIlyen könyv nem található. ")
    else:
        print(f"\nKiválasztva: {megtalalt_konyv.szerzo}: {megtalalt_konyv.cim}")
        valasz = kerdes_dontes("BIZTOSAN törölni szeretnéd a kiválasztott könyvet? \nA művelet nem visszavonható! (I/N): ")
        if valasz == "i":
            konyvek.remove(megtalalt_konyv)
            print("\nSikeresen törölve!")
        else:
            print("Törlés megszakítva!")

    