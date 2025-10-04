import random


def cocktail_sort(pole):
    n = len(pole)
    start = 0
    end = n - 1
    slozitost = 0
    while start < end:
        prohodil_se = False
        
        
        for i in range(start, end):
            slozitost += 1

            if pole[i] > pole[i + 1]:
                pole[i], pole[i + 1] = pole[i + 1], pole[i]
                prohodil_se = True
        end -= 1 
        
        if not prohodil_se:
            break
            
        
        for i in range(end, start, -1):
            slozitost += 1
            if pole[i] < pole[i - 1]:
                pole[i], pole[i - 1] = pole[i - 1], pole[i]
                prohodil_se = True
        start += 1  
        
        if not prohodil_se:
            break
    
    return pole , slozitost


