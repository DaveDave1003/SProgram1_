import random
import time

arr = [random.randint(1, 10000) for i in range(100000)]


def split_merge(arr):
    
    slozitost = 0

    if len(arr) > 1:
        mid = len(arr) // 2
        leva = arr[:mid] 
        prava = arr[mid:] 

        slozitost += split_merge(leva)[1]
        slozitost += split_merge(prava)[1]

        i = j = k = 0

        while i < len(leva) and j < len(prava):
            slozitost += 1

            if leva[i] < prava[j]:
                arr[k] = leva[i]
                i += 1
                
            else:
                arr[k] = prava[j]
                j += 1
            k += 1

        while i < len(leva):
            arr[k] = leva[i]
            i += 1
            k += 1

        while j < len(prava):
            arr[k] = prava[j]
            j += 1
            k += 1

    return arr, slozitost



def python(arr):
    sorted(arr)

    return



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



def insert_sort(arr, left, right):
    for i in range(left + 1, right + 1):
        key = arr[i]
        j = i - 1
        while j >= left and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1
#17 - 12, 
def hybrid_quick_sort(arr, low=0, high=None, threshold=12):
    if high is None:
        high = len(arr) - 1
    while low < high:
        if high - low < threshold:
            insert_sort(arr, low, high)
            break
        else:
            pivot_index = partition(arr, low, high)
            if pivot_index - low < high - pivot_index:
                hybrid_quick_sort(arr, low, pivot_index - 1, threshold)
                low = pivot_index + 1
            else:
                hybrid_quick_sort(arr, pivot_index + 1, high, threshold)
                high = pivot_index - 1
    return arr



arr1 = arr.copy()
arr2 = arr.copy()
arr3 = arr.copy()
arr4 = arr.copy()

arr6 = arr.copy()




start_merge = time.perf_counter()
split_merge(arr1)
end_merge = time.perf_counter()


start_python = time.perf_counter()
python(arr2)
end_python = time.perf_counter()

start_quick = time.perf_counter()
Quick_sort(arr3)
end_quick= time.perf_counter()

start_shell = time.perf_counter()
shell_sort_v2(arr4)
end_shell= time.perf_counter()



start_hybrid = time.perf_counter()
hybrid_quick_sort(arr6)
end_hybrid = time.perf_counter()




print(f"merge trval: {end_merge - start_merge:.6f} s")
print(f"SORTED trval: {end_python - start_python:.6f} s")

print(f"quick trval: {end_quick - start_quick:.6f} s")
print(f"shell trval: {end_shell - start_shell:.6f} s")
print(f"hybrid trval: {end_hybrid - start_hybrid: .6f} s")