import random
test = list(range(50))
random.shuffle(test)

print(test)


from Bubble_normal import bubble_sort_normal
from Bubble_opti import bubble_sort_optimalizovany
from Bubble_short import bubble_sort_kratsi_rozsah
from Bubble_detection import bubble_sort_s_detekci

print(bubble_sort_normal(test[:]))
print(bubble_sort_optimalizovany(test[:]))
print(bubble_sort_kratsi_rozsah(test[:]))
print(bubble_sort_s_detekci(test[:]))

