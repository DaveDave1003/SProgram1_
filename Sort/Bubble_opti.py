def cocktail_sort(arr):
    n = len(arr)
    
    slozitost = 0
    for i in range(n - 1):
        
        prohodil_se = False  # Flag pro detekci výměn
        
        for j in range(n - 1):
            slozitost += 1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                prohodil_se = True  # Zaznamenáme výměnu
        
        # Pokud se nic neprohodilo, pole je seřazené!
        if not prohodil_se:
            break
        
    return arr, slozitost