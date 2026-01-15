class Kontrola_zavorky:
    def __init__(self, text):
        self.text = text
        self.zasobnik = []
        self.zavorky = {')': '(', '}': '{', ']': '['}

    def zkontroluj(self):
        for znak in self.text:
            if znak in self.zavorky.values():
                self.zasobnik.append(znak)
            elif znak in self.zavorky:
                if not self.zasobnik:
                    return False
                if self.zasobnik.pop() != self.zavorky[znak]:
                    return False
        return len(self.zasobnik) == 0
    

texty = ["((a+b)*c)", "(a+b)", "(a+b", "a+b)", ")(", ","]

for item in texty:
    kontrola = Kontrola_zavorky(item)
    vysledek = kontrola.zkontroluj()
    print(f"{item} -> {vysledek}")

