import random


def bubble_sort_normal(pole):
    n = len(pole)
    slozitost = 0
   
    for i in range(n - 1):            
        for j in range(n - 1):  
            slozitost += 1    
            
            
            # pokud je prvek vlevo větší než vpravo, prohodíme
            if pole[j] > pole[j + 1]:
                pole[j], pole[j + 1] = pole[j + 1], pole[j]
    
    return pole, slozitost

