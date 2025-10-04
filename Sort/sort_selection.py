def selection_sort(pole):

    slozitost = 0


    #Všechny prvky v poli
    for i in range(len(pole) - 1):
        #Pamatovani nejmensiho prvku
        nejmensi_index = i

        for kontrolovany_index in range(i, len(pole)):
            slozitost += 1

            if (pole[kontrolovany_index] < pole[nejmensi_index]):
                #Novy nejmensi
                nejmensi_index = kontrolovany_index
        #Prohození nejmensiho
        pole[i], pole[nejmensi_index] = pole[nejmensi_index], pole[i]

    return pole, slozitost

