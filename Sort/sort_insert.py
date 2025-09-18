def insertion_sort(pole):
    
    for i in range(1,len(pole)):
        klic = pole[i]
        j = i - 1

        while j >= 0 and pole[j] > klic:
            pole[j+1] = pole[j]
            j -= 1
        
        pole[j+1] = klic




def insertion_sort_v2(pole):
    print("Původní pole:", pole)
    
    for i in range(1, len(pole)):
        klic = pole[i]
        j = i - 1

        print(f"    Vkládám {klic} na správné místo...")

        # posouváme větší prvky doprava
        while j >= 0 and pole[j] > klic:
            pole[j + 1] = pole[j]
            j -= 1
            print(f"        Posouvám {pole[j+1]} doprava: {pole}")

        pole[j + 1] = klic
        print(f"        -> Vložil jsem {klic} na pozici {j+1}: {pole}")

    print("Seřazené pole:", pole)

# -----------------------------
# Přímý vstup od uživatele
# -----------------------------
pole = [3,2,5,4,1]
insertion_sort_v2(pole)
print(pole)
