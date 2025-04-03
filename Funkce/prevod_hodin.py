


i = 60
X = 0

def prevod_na_minuty(hodiny,minuty):
    i = hodiny / 60 

    X = minuty + i 
    return X
    








hodiny = int(input("Kolik je hodin: "))
minuty = int(input("Kolik je minut: "))

print (prevod_na_minuty(hodiny,minuty))