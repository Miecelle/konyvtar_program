# Könyv nyilvántartó program
## I. Program leírása

A program lehetővé teszi a könyveink nyilvántartását. Konzolos felületen működik, lehetővé teszi a könyvek adatainak (szerző, cím, ISBN szám, állapot) tárolását, keresését, módosítását és törlését. Az adatok a program bezárását követően is megmaradnak egy külső fájlban.
## II. Funkciók
1. **Új könyv hozzáadása:** lehetővé teszi új könyv felvételét a nyilvántartásba. Ehhez a szerzőt, címet és ISBN számot kell megadni. Az állapot alapértelmezetten *"Elérhető"*, amit módosíthatunk.
2. **Könyveim listázása:** a nyilvántartásba felvett könyveket kilistázza abc sorrendben rendre a szerző, cím és elérhetőség szerint. 
3. **Keresés:** lehetővé teszi a keresést a nyilvántartott könyvek között. Cím, szerző és ezek egy részletének alapján is lehet keresni. A program kilistázza az összes találatot, amelyben a keresett karakterlánc megtalálható.
4. **Könyv adatainak vagy állapotának módosítása:** az ISBN szám alapján kiválasztott könyv adatait (szerző, cím, ISBN) vagy az állapotát (*"Elérhető", "Kölcsönadva", "Eladva", "Eltűnt"*) lehet módosítani. 
5. **Törlés:** lehetővé teszi egy ISBN szám által kiválasztott könyv törlését a nyilvántartásból.A törlést nem lehet visszavonni.
6. **Kilépés:** a program leállításáért felel.

## III. Használat

### Első lépések: 
A program futtatásához **Python** szükséges. A program Python **3.12.10**-es verzióban íródott.

**Szükséges csomagok:** tabulate==0.10.0
A program használata előtt a csomagot telepítsük. A következőt kell beírni a konzolba : *pip install tabulate*

Ezt követően a program a futtatásra készen áll.

### A program futtatása:
Navigáljunk a program mappájába, majd futtassuk a `main.py` fájlt.

### Program működése:
A program induláskor ellenőrzi, hogy létezik-e a `konyvek.json` fájl. Ha nem létezik, akkor létrehozza és üres könyvtárral indul. Ha létezik, akkor beolvassa az adatokat. 

A program üdvözöl minket, majd megjelenik a főmenü, amelyben a funkciók közül választhatunk:

1. Új könyyv hozzáadása
2. Könyveim listázása
3. Keresés
4. Könyv adatainak vagy állapotának módosítása
5. Törlés
6. Kilépés

A program bekéri a választott menü számát, amihez a konzolba a megfelelő számot kell beírni, majd entert ütni. Ha nem a menü számai közül választunk, akkor a program figyelmeztet minket, hogy csak 1-6-ig választhatunk számokat.

### 1. Új könyv hozzáadása:
A program bekéri az adatokat: egyesével a könyv szerzőjét, címét és ISBN számát (a beírást követően entert kell ütni). 

A szerző nevének beírásánál a program mindig úgy menti el, hogy a kezdőbetűk nagyok, míg a többi kicsi, bárhogy írjuk be. A cím esetében csak a legelső betű lesz nagy a többi kicsi, bárhogy írjuk be. 

Az ISBN szám egyedi azonosító, ezért a program a beírást követően ellenőrzi, hogy benne van-e már a nyilvántartásban, ha igen, akkor a program erre figyelmeztet. (Azonos ISBN számú könyveket, nem tud kezelni. Azaz azonos kiadásból több példányt.) 

Az állapotot alapértelmezetten *"Elérhető"*-nek tekinti a program. A program elmenti a felvitt adatokat a `konyvek.json` fájlba, majd visszatér a főmenübe.

### 2. Könyveim listázása:
A menüpont kiválasztásával a program kilistázza a nyilvántartásba vett könyveket a `konyvek.json`fájlból egy táblázatban (szerző, cím, ISBN, állapot). 

A táblázatban a könyveket abc sorrendben rendre a szerző, cím és elérhetőség szerint tartalmazza. A kilistázás után visszatér a főmenübe.

### 3. Keresés:
A program bekér egy szerzőt vagy címet. Elegendő ezeknek csak egy részletét is beírni, majd entert ütni. Ezután a program kilistázza táblázatosan az összes találatot amelyben a keresett karakterlánc megtalálható. Amennyiben nem található ilyen könyv, akkor jelzi felénk *"Sajnos nincs ilyen találat!"* üzenettel. Ezt követően visszatér a főmenübe.

### 4. Könyv adatainak vagy állapotának módosítása:
A könyv bekéri a módosítani kívánt könyv ISBN számát (ezt könnyen meg lehet tudni a *2. Könyveim listázása* vagy a *3. Keresés menüpont* választásával). Ezután egy almenübe lép be, melynél az alábbi opciók közül lehet választani:

- A: Könyv adatainak módosítása (szerző, cím, ISBN)
- B: Könyv állapotának módosítása
- C: Vissza a főmenübe
  
A megfelelő betűt kell beírni, majd entert ütni. A program nem érzékeny a nagybetűre, a kisbetűt is elfogadja. Amennyiben nem a felsoroltak betűjele közül választunk a program jelzi felénk *ilyen menüpont nincs, kérlek válassz a menüpontokból, A, B vagy C!"* üzenettel.

*A könyv adatainak módosítását* választva egyenként megkérdezi a program, hogy szeretnénk-e megváltoztatni a szerző nevét, a könyv címét vagy az ISBN számát. Erre I (igen) vagy N (nem) beütésével, majd enterrel reagálhatunk. A program a kis és nagy betűt is elfogadja. Amennyiben nem megfelelő betűt ütjük be a program jelzi felénk és ismét várja a választ.

Az ISBN szám változtatásánál a program ellenőrzi, hogy van-e másik könyv aminek ugyanez az ISBN száma. Ha igen, akkor ezt jelzi felénk, nem lehet ilyen számmal elmenteni. Amennyiben  a könyv eredeti ISBN számát írjuk be újra, a program ugyanúgy fogja elmenteni a könyvet, nem ír ki hibát.

Az adatok megváltoztatása után a program elmenti a változtatásokat és visszatér a 4. almenübe, ahonnan a *vissza a főmenübe* funkció kiválasztásával lehet a főmenübe visszatérni.

*A könyv állapotának módosítását* választva a program megkérdezi minket, hogy mire szeretnénk változtatni a könyv állapotát. A felsoroltak közül kell beírnia a választott állapotot, majd entert ütni. (Kis és nagybetű nem számít a beírásnál.) Ezután a program elmenti a változtatásokat. Amennyiben ez nem egyezik meg a felsorolt állapotokkal, akkor a program erre figyelmezteti és visszatér az almenübe, ahonnan a fentebb leírtak szerint lehet visszalépni a főmenübe.

### 5. Törlés:
A program bekéri a törölni kívánt könyv ISBN számát. Ezután figyelmeztet, hogy a **törlés nem visszavonható** és megkérdezi valóban törölni szeretnénk-e a könyvet a nyilvántartásunkból.A program a kis és nagy betűt is elfogadja. Amennyiben nem megfelelő betűt ütjük be a program jelzi felénk és ismét várja a választ. A törlést követően a fájl frissül.

### 6. Kilépés:
A menüpont kiválasztásával a program elköszön, majd leáll.

## IV. Fájlok
Program mappa tartalma:
- `requirements.txt`, ami tartalmazza a futtatáshoz szükséges könyvtárakat, amelyeket előzetesen telepíteni kell.
- `readMe.md`, ami tartalmazza a program használatához szükséges információkat
- `main.py`, ami a program menüjét tartalmazza. Ezzel kell futtatni a programot.
- `konyvtar` mappa, ami a modulokat tartalmazza.

Modulok:
- `adatkezeles`, ami az adatok beolvasásáért és mentéséért felelős függvényeket tartalmazza.
- `konyvtarkezeles`, ami a funkciókhoz szükséges függvényeket és azok segédfüggvényeit tartalmazza.
- `__init__`, amibe az *adatkezeles* és *konyvtarkezeles* modulok függvényei be vannak hívva.
   
   