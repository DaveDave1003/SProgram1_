import math

class Zlomek:
    def __init__(self,citatel,jmenovatel = 1):
        self.citatel = int(citatel)
        self.jmenovatel = int(jmenovatel)

    def __add__(self,novy):
        return Zlomek(self.citatel * novy.jmenovatel + novy.citatel * self.jmenovatel, self.jmenovatel * novy.jmenovatel).zkrat()
  

    def __sub__(self,novy):
        return Zlomek(self.citatel * novy.jmenovatel - novy.citatel * self.jmenovatel, self.jmenovatel * novy.jmenovatel).zkrat()

    def __mul__(self,novy):
        return Zlomek(self.citatel *  novy.citatel, novy.jmenovatel * self.jmenovatel).zkrat()
    
    def __truediv__(self, novy):
        return Zlomek(self.citatel * novy.jmenovatel, self.jmenovatel * novy.citatel).zkrat()

    def __str__(self):
        return f"{self.citatel}/{self.jmenovatel}"
    
    def zkrat(self):
        nsd = math.gcd(abs(self.citatel), abs(self.jmenovatel))
        self.citatel = int(self.citatel / nsd)
        self.jmenovatel = int(self.jmenovatel / nsd)

        return self


a = Zlomek(1, 2)
b = Zlomek(1, 3)
print(a + b)   # → 5/6
print(a - b)   # → 1/6
print(a * b)   # → 1/6
print(a / b)   # → 3/2