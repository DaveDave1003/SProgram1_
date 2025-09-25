import random
import time
import matplotlib.pyplot as plt
# Musíš si stáhnout knihovnu - napíšeš do konzole pip install matplotlib
# Je to jen na vykreslení grafu - nebylo to povinné

# Obyčejný neoptimalizovaný bubble sort
def bubble_v1(arr):
    comp = 0
    while True:
        a = sorted(arr)
        comp += a
        if a == len(arr):
            break
        for i in range(len(arr)-1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
            comp += 1
    return comp

# 1. Optimalizace - vždy se vysereš na poslední prvky, protože víš že jsou seřazený
def bubble_v2(arr):
    comp = 0
    j = 0
    while True:
        a = sorted(arr)
        comp += a
        if a == len(arr):
            break
        j += 1
        for i in range(len(arr)-j):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
            comp += 1
    return comp

# 2. optimalizace - místo volání sorted() checkuješ seřazenost v hlavním loopu
def bubble_v3(arr):
    comp = 0
    j = 0
    while True:
        w = 0
        j += 1
        for i in range(len(arr)-j):
            if arr[i] > arr[i+1]:
                w += 1
                arr[i], arr[i+1] = arr[i+1], arr[i]
            comp += 1
        
        if w == 0:
            break
    return comp

# 3. optimalizace - sortíš střídavě oběma směry, takže sereš i na začátek i na konec
def bubble_v4(arr):
    comp = 0
    l = 0
    r = 1
    while True:
        w = 0
        for i in range(len(arr)-r):
            if arr[i] > arr[i+1]:
                w += 1
                arr[i], arr[i+1] = arr[i+1], arr[i]
            comp += 1
        r += 1
        if w == 0:
            break
        
        w = 0
        for i in range(len(arr)-r, l, -1):
            if arr[i] < arr[i-1]:
                w += 1
                arr[i], arr[i-1] = arr[i-1], arr[i]
            comp += 1
        l += 1
        if w == 0:
            break
    return comp

# Checkne jestli je pole seřazený, ono to sice úplně nefunguje, ale aby se to rozbilo musela by být velmi specifická situace, to neřeš
def sorted(arr):
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            return i+1
    return len(arr)



# Otestuje jak dlouho to trvá a vykreslí graf
def measure(func):
    data = []
    for i in range(100, 1100, 100):
        start = time.time()
        output = func([random.randint(0, 1000) for _ in range(i)])
        end = time.time()
        data.append(output)
        print(i)

    plt.plot(range(1000, 11000, 1000), data, label=func.__name__)
    plt.xlabel('Array Size')
    plt.ylabel('Time')

measure(bubble_v1)
measure(bubble_v2)
measure(bubble_v3)
measure(bubble_v4)


plt.title('Bubble Sort')

plt.legend(loc='best')
plt.show()

