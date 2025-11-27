import math
class Cislo:
    def __init__(self, hodnota):
        self.hodnota = hodnota
            
    def __add__(self, jiny):
        return Cislo(self.hodnota + jiny.hodnota)

    def __sub__(self, jiny):
        return Cislo(self.hodnota - jiny.hodnota)    
    
    def __mul__(self, jiny):
        return Cislo(self.hodnota * jiny.hodnota)
    
    def __truediv__(self, jiny):
        return  Cislo(self.hodnota / jiny.hodnota)
    
    def __eq__(self, jiny):
        return self.hodnota == jiny.hodnota

    def __lt__(self, jiny):
        return self.hodnota < jiny.hodnota

    def __gt__(self, jiny):
        return self.hodnota > jiny.hodnota


    def __str__(self):
        return f"Vysledek ({self.hodnota})"


class Zlomek:
    def __init__(self, citatel, jmenovatel=1):
        self.citatel = citatel
        self.jmenovatel = jmenovatel
        
        if jmenovatel == 0:
            pass
        
    def __str__(self):
       return f"{int(self.citatel)} / {int(self.jmenovatel)}"
        




c = Zlomek(4, 2)
print(c)



a = Cislo(4)
b = Cislo(2)
plus = a + b
minus = a - b
mult = a * b
div = a / b
eq = a == b
lt = a < b
gt = a > b

print(plus)
print(minus)
print(mult)
print(div)
print(a == b)
print(a < b)
print(a > b)
