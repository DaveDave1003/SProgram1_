def bubble_sort_verbose(arr):
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


# -----------------------------
# Přímý vstup od uživatele
# -----------------------------
user_input = input("Zadej čísla oddělená čárkou (např. 5,3,8,4,2): ")
data = [int(x.strip()) for x in user_input.split(",")]

bubble_sort_verbose(data)