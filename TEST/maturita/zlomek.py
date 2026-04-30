import math

class Zlomek:
    def __init__(self, citatel, jmenovatel=1):
        self.citatel = citatel
        self.jmenovatel = jmenovatel
        
        if jmenovatel == 0:
            pass

        self = self.zkrat()
        
    def zkrat(self):
        #Nejmenší Společný Dělitel
        nsd = math.gcd(abs(self.citatel), abs(self.jmenovatel))
        
        self.citatel = self.citatel / nsd 
        self.jmenovatel = self.jmenovatel / nsd 
       
        pass


    def __add__(self,jiny):
        return Zlomek(self.citatel * jiny.jmenovatel + jiny.citatel * self.jmenovatel, self.jmenovatel * jiny.jmenovatel)



z1 = Zlomek(1, 2)
z2 = Zlomek(3, 4)
z3 = Zlomek(5)
print(f"z1 = {z1}")  # 1/2
print(f"z2 = {z2}")  # 3/4
print(f"z3 = {z3}")  # 5/1
# Test 2: Sčítání
print(f"{z1} + {z2} = {z1 + z2}")  # 5/4
# Test 3: Odčítání
print(f"{z2} - {z1} = {z2 - z1}")  # 1/4
# Test 4: Násobení
print(f"{z1} * {z2} = {z1 * z2}")  # 3/8
# Test 5: Dělení
print(f"{z1} / {z2} = {z1 / z2}")  # 2/3
# Test 6: Složitější výpočet
print(f"({z1} + {z2}) * {z3} = {(z1 + z2) * z3}")  # 25/4
# Test 7: Zkracování
z4 = Zlomek(8, 12)
print(f"Před zkrácením: {z4}")  # 8/12
z4.zkrat()
print(f"Po zkrácení: {z4}")    # 2/3