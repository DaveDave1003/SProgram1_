import random


def shell_sort_v2(arr):
    n = len(arr)
    gap = 3 * n + 1
    slozitost = 0

    while gap > 0:

        for i in range(gap, n):
            slozitost += 1
            temp = arr[i]
            j = i 

            while j >= gap and arr[j- gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 3

    return arr, slozitost
