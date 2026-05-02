import os
import json
from .konyvtarkezeles import Konyv
fajlnev = "konyvek.json"


#Adatokat olvas be a fájlból
def adatok_beolvasasa (fajlnev):
    konyvek = []
    #megnézi létezik-e a fájl
    if os.path.exists(fajlnev): 
        #megnyitja a fájlt olvasásra, utf-8 gondoskodik arról, hogy magyar magánhangzók is jól legyenek a fájlban
        with open(fajlnev, "r", encoding = "utf-8") as konyvtar_fajl: 
            adatok = json.load(konyvtar_fajl)
            #a szótárakból az adatokat a könyv osztállyal példányosítja és egy listába veszi őket. 
            for szotar in adatok: 
                konyvek.append(Konyv(szotar["Szerző"], szotar["Cím"], szotar["ISBN"], szotar["Állapot"]))
            return konyvek
    return []

#Az adatokat menti el
def adatok_mentese (fajlnev, konyvek):
    mentes = []
    #a könyvek listából kiveszi a könyv példányokat és visszaalakítja szótárakká, majd egy listába teszi
    for konyv in konyvek: 
        mentes.append(konyv.szotarba())
    #megnyitja a fájlt írásra    
    with open(fajlnev, "w", encoding = "utf-8") as mentes_fajl:
        #elmenti az adatokat egy json fájlba, az indent = 4 miatt lesz olvasható, az ensure_ascii miatt maradnak az ékezetes betűk 
        json.dump(mentes, mentes_fajl, indent = 4, ensure_ascii = False) 
