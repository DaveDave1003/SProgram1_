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

    
    
    def __str__(self):
       return f"{int(self.citatel)} / {int(self.jmenovatel)}"
        




z = Zlomek(6, 2)
print(z)  # Mělo by vypsat: 3/4
z2 = Zlomek(5, 10)
print(z2)  # Mělo by vypsat: 5/1

