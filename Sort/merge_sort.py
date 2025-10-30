
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









 
 
 
 



    