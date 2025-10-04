import random
def bubble_sort_s_detekci(pole):
    n = len(pole)
    slozitost = 0
    

    for i in range(n - 1):
       
        prohodil_se = False  # Výměna
        
        for j in range(n - 1):
            
            slozitost += 1
           
            # pokud jsou prvky ve špatném pořadí, prohodíme
            if pole[j] > pole[j + 1]:
                pole[j], pole[j + 1] = pole[j + 1], pole[j]
                prohodil_se = True  # Zaznamenáme výměnu
            

        # pokud se nic neprohodilo, pole je setříděné
        if not prohodil_se:
            
            break
    
    
    
    return pole, slozitost



