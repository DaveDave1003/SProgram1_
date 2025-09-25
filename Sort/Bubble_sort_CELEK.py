def bubble_sort_normal(arr):
    n = len(arr)
    print("Původní pole:", arr)

    for i in range(n - 1):
        print(f"\nPrůchod {i+1}:")
        for j in range(n - 1 - i):
            print(f"  Porovnávám {arr[j]} a {arr[j+1]}...", end=" ")
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                print("prohodím →", arr)
            else:
                print("nechám beze změny")
        print("Výsledek po průchodu:", arr)

    print("\nKonečně seřazeno:", arr)
    return arr



def bubble_sort_kratsi_rozsah(arr):
    n = len(arr)
    print("Původní pole:", arr)
    
    for i in range(n - 1):
        print(f"\nPrůchod {i+1}:")
        # V každém průchodu je největší prvek už na správném místě
        # Takže můžeme zkrátit rozsah o i pozic
        for j in range(n - 1 - i):  # Místo (n-1) jen (n-1-i)!
            print(f"  Porovnávám {arr[j]} a {arr[j+1]}...", end=" ")
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                print("prohodím →", arr)
    return arr



def bubble_sort_optimalizovany(arr):
    n = len(arr)
    print("Původní pole:", arr)
    
    for i in range(n - 1):
        print(f"\nPrůchod {i+1}:")
        prohodil_se = False  # Flag pro detekci výměn
        
        for j in range(n - 1):
            
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                prohodil_se = True  # Zaznamenáme výměnu
        
        # Pokud se nic neprohodilo, pole je seřazené!
        if not prohodil_se:
            print(f"Pole seřazeno po {i + 1} průchodu(ech)")
            break
        print("Výsledek po průchodu:", arr)
    
    
    print("\nKonečně seřazeno:", arr)
    return arr


def bubble_sort_s_detekci(pole):
    n = len(pole)
    count = 0
    print("Původní pole:", pole)

    for i in range(n - 1):
        print(f"\nPrůchod {i+1}:")
        prohodil_se = False  # Flag pro detekci výměn
        
        for j in range(n - 1):
            print(f"  Porovnávám {pole[j]} a {pole[j+1]}...", end=" ")
            count = count + 1

            if pole[j] > pole[j + 1]:
                pole[j], pole[j + 1] = pole[j + 1], pole[j]
                prohodil_se = True  # Zaznamenáme výměnu
            print("prohodím →", pole)

        # Pokud se nic neprohodilo, pole je seřazené!
        if not prohodil_se:
            print(f"Pole seřazeno po {i + 1} průchodu(ech)")
            break
    
    
    print("\nKonečně seřazeno:", pole)
    return count






pole = [1,2,4,3,5]

#bubble_sort_kratsi_rozsah(pole)
bubble_sort_normal(pole)
#bubble_sort_optimalizovany(pole)

#bubble_sort_s_detekci(pole)



