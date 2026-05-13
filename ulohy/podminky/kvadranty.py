import math

#Zadej libovolnou hodnotu neznámých
X= float(input("Zadej x: "))
Y= float(input("Zadej y: "))



if Y > 0 and X > 0:
    print("Bod leží v I. kvadrantu")
elif Y > 0 and X < 0:
    print("Bod leží v II. kvadrantu")
elif Y < 0 and X < 0:
    print("Bod leží ve III. kvadrantu")
elif Y < 0 and X > 0:
    print("Bod leží ve IV. kvadrantu")
elif Y == 0 and X != 0:
    print("Bod leží na ose X")
elif X == 0 and Y != 0:
    print("Bod leží na ose Y")
else:
    print("Bod leží v počátku")

