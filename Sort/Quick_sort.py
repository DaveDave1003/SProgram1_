


def Quick_sort(arr):
    slozitost = 0 

    def partition(start, end):
        nonlocal slozitost
        if start >= end:
            return

        slozitost += 1

        i = start
        j = end
        pivot = arr[(start + end) // 2]

        while i <= j:
            #Kdyz je levo mensi nez pivot
            while arr[i] < pivot:
                i += 1
            #Kdyz je pravo vetsi nez pivot
            while arr[j] > pivot:
                j -= 1

            #Kdyz jsou hodnoty stejne -> prohodit
            if i <= j:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
                j -= 1

        if start < j:
            partition(start, j)
        if i < end:
            partition(i, end)

    partition(0, len(arr) - 1)
    return arr, slozitost




