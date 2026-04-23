import random



def bubble_sort(pole):
    delka = len(pole)
    slozitost = 0

    for i in range (delka-1):
        for j in range (delka-1):
            slozitost += 1

            if pole[j] > pole[j+1]:

                pole[j], pole[j+1] = pole[j+1], pole [j]
    
    return pole, slozitost


delka = int(input("Zadej délku seznamu: "))
pole = []

for i in range(delka):
    pole.append(random.randint(0, int(delka)))

print(f"Seznam {pole} se upravil na {bubble_sort(pole)} ")