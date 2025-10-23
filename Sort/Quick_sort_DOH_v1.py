def partition(left, right, pivot, numbers, slozitost):
    
    while(left < right):
        slozitost += 1

        while(numbers[left]<pivot):
            left += 1
            slozitost += 1

        slozitost += 1
        while(pivot<numbers[right]):
            right -= 1
            slozitost += 1

        if(left<=right):
            temp = numbers[left]
            numbers[left] = numbers[right]
            numbers[right] = temp

            left += 1
            right -= 1

    return left, slozitost   

def quicksort(left, right, numbers, slozitost):

    if (left < right):
        
        pivot = numbers[(left + right) // 2]
        mid, slozitost = partition(left, right, pivot, numbers, slozitost)
        slozitost = quicksort(left, mid - 1,numbers, slozitost)
        slozitost = quicksort(mid, right, numbers, slozitost)
        
    return slozitost


def quick_celek(numbers):
    slozitost = quicksort(0, len(numbers) - 1, numbers, 0)
    
    return numbers, slozitost

