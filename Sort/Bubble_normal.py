def bubble_sort_normal(arr):
    n = len(arr)
   
    slozitost = 0

    for i in range(n - 1):
       
        for j in range(n - 1 - i):
            slozitost += 1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr, slozitost 
