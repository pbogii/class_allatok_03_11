from allatok import Allat, Madar, Keteltu, Hullo
from emlos import Emlos, Macska, Kutya

allat1 = Allat("Bodri", "kutya", 5, "kert", "közepes")
allat2 = Allat("Cirmi", "macska", 3, "lakás", "pici")
print(allat1)
print(allat2)


emlos1= Emlos("miau", "macska", 3, "ház", "szürke")
emlos2= Emlos("Morzsi", "kutya", 6, "kenel", "fekete")
print(emlos1)
print(emlos2)


macska1 = Macska("Hubert", "macska", 4, "cirmos")
print(macska1)
macska1.dorombol()


kutya1 = Kutya("Hyrax","kutya", 8, "barna")
print(kutya1)
kutya1.ugat()


madar1 = Madar("Fakopancs",  1, "kicsi")
print(madar1)
madar1.csirip()


keteltu1 = Keteltu("Breik", 2, "kicsi")
print(keteltu1)
keteltu1.brekeg()


hullo1 = Hullo("Gyikk", 3, "kicsi")
print(hullo1)
hullo1.napozik()
