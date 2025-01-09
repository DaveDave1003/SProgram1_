import math

#Zadej 3 libovolné koeficienty
a= float(input("Zadej koeficient A: "))
b= float(input("Zadej koeficient B: "))
c= float(input("Zadej koeficient C: "))

d= b*b-4*a*c

#Výsledná hondnota
if d >= 0:
    print(round(((-b + math.sqrt(d))/ (2*a)),2))

elif d < 0:
    print("neexistuje řešení")  

if d > 0:
    print(round(((-b - math.sqrt(d))/ (2*a)),2))
