from allatok import Madar, Hullo, Keteltu
from emlos import Kutya, Macska


allatok_allatok= []
with open('adatok/allatokk.txt', 'r', encoding='utf-8') as forrasfajl:
    next(forrasfajl)
    for sor in forrasfajl:
        nev, faj, eletkor, szorzet_szine = sor.strip().split(',') 
        if faj == "kutya":
            allatok_allatok.append(Kutya(nev, faj, int(eletkor), szorzet_szine))
        elif faj == "macska":
            allatok_allatok.append(Macska(nev, faj, int(eletkor), szorzet_szine))
        elif faj == "madar":
            allatok_allatok.append(Madar(nev, int(eletkor)))
        elif faj == "keteltu":
            allatok_allatok.append(Keteltu(nev, int(eletkor)))
        elif faj == "hullo":
            allatok_allatok.append(Hullo(nev, int(eletkor)))




for allat in allatok_allatok:
    print(allat)