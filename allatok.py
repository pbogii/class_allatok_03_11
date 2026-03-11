class Allat:
    def __init__(self, nev_, faj_, eletkor_, elohely_, meret_):
        self.nev = nev_
        self.faj = faj_
        self.eletkor = eletkor_
        self.elohely = elohely_
        self.meret = meret_

    def __str__(self):
        return f"{self.nev} nevű  {self.faj}, {self.eletkor} éves, élőhelye {self.elohely}, mérete {self.meret}"
    
    
class Madar(Allat):
    def __init__(self, nev_, eletkor_):
        super().__init__(nev_, "madar", eletkor_, "erdő", "kicsi")
    def csirip(self):
        print(f"{self.nev} épp csiripel")


class Keteltu(Allat):
    def __init__(self, nev_, eletkor_):
        super().__init__(nev_, "keteltu", eletkor_, "tópart", "kicsi")
    def brekeg(self):
        print(f"{self.nev} épp brekeg")


class Hullo(Allat):
    def __init__(self, nev_, eletkor_):
        super().__init__(nev_, "hullo", eletkor_,"szikla", "kicsi")
    def napozik(self):
        print(f"{self.nev} épp napozik egy kövön")