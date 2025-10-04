def selection_sort(pole):

    slozitost = 0

    for i in range(len(pole) - 1):

        nejmensi_index = i

        for kontrolovany_index in range(i, len(pole)):
            slozitost += 1

            if (pole[kontrolovany_index] < pole[nejmensi_index]):

                nejmensi_index = kontrolovany_index

        pole[i], pole[nejmensi_index] = pole[nejmensi_index], pole[i]

    return pole, slozitost

pole = [4, 2, 3, 1, 0, 5]
print(selection_sort(pole))

