def bubble_sort(pole):
    delka = pole(len)
    slozitost = 0

    for i in range (delka-1):
        for j in range (delka-1):
            slozitost += 1

            if pole[j] > pole[j+1]:

                pole[j], pole[j+1] = pole[j+1], pole [j]
    
    return pole, slozitost




        