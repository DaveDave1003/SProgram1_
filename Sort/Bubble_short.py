def bubble_sort_kratsi_rozsah(arr):
    n = len(arr)
    slozitost = 0
    
    #Průchod celého pole
    for i in range(n - 1):
        
        #nejvetsi prvek na konec (pokazde o 1 mene)
        for j in range(n - 1 - i):  
            slozitost += 1
            
            
            # pokud je prvek vlevo větší než vpravo, prohodíme
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                
    return arr, slozitost
