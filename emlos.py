from allatok import Allat
class Emlos(Allat):
    def __init__(self, nev_, faj_, eletkor_, elohely_,  szorzet_):
        super().__init__(nev_, faj_, eletkor_, elohely_, "közepes")
        self.szorzet = szorzet_

    def __str__(self):
        return super().__str__() + f", szorzete {self.szorzet}"
    
class Macska(Emlos):
    def __init__(self, nev_, faj_, eletkor_, szorzet_):
        super().__init__(nev_, faj_ , eletkor_, "lakas", szorzet_)

    def dorombol(self):
        print(f"{self.nev} épp dorombol")


class Kutya(Emlos):
    def __init__(self, nev_, faj_, eletkor_, szorzet_):
        super().__init__(nev_, faj_, eletkor_, "kert", szorzet_)

    def ugat(self):
        print(f"{self.nev} épp ugat")