def bubble_sort_kratsi_rozsah(arr):
    n = len(arr)
    slozitost = 0
    
    for i in range(n - 1):
        
        # V každém průchodu je největší prvek už na správném místě
        # Takže můžeme zkrátit rozsah o i pozic
        for j in range(n - 1 - i):  # Místo (n-1) jen (n-1-i)!
            slozitost += 1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                
    return arr, slozitost
