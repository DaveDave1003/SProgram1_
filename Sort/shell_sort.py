import random




def shell_sort(arr):
    n = len(arr)
    gap = n // 2
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
        gap //= 2

    return arr, slozitost









