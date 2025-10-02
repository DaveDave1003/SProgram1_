import random



def insertion_sort(pole):
    
    slozitost = 0

    for i in range(1,len(pole)):
        klic = pole[i]
        j = i - 1
        slozitost += 1
        while j >= 0 and pole[j] > klic:
            slozitost += 1
            pole[j+1] = pole[j]
            j -= 1
        
        pole[j+1] = klic
        
    
    return pole, slozitost






