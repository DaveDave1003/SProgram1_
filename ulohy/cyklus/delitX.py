def delitelna(x,y):
    vysledek = []

    for i in range(x, y + 1, x):
        vysledek.append(i)

    return vysledek



print(delitelna(3,10))
print(delitelna(5,20))
print(delitelna(2,10))