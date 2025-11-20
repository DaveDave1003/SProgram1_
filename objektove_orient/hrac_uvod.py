#https://code-vault-gjs.vercel.app/

class Hrac:
    # Konstruktor
    def __init__(self, name):
        # atributy
        self.jmeno = name
        self.zivoty = 100       
        self.__penize = 20

    # metody
    def utrzi_zraneni(self, dmg):
        self.__penize = self.__penize + 15
        self.zivoty -= dmg

    def zjisti_penize(self):
        vysledek = self.__penize
        return vysledek




hrac1 = Hrac("David")

print(hrac1.zjisti_penize())
hrac1.utrzi_zraneni(10)
print(hrac1.zjisti_penize())

