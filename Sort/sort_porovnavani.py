import matplotlib.pyplot as plt
import random

#vyvolání funkcí
from Bubble_normal import bubble_sort_normal
from Bubble_opti import cocktail_sort
from Bubble_short import bubble_sort_kratsi_rozsah
from Bubble_detection import bubble_sort_s_detekci
from sort_insert import insertion_sort
from sort_selection import selection_sort
from shell_sort import shell_sort
from Shell_sort_V2 import shell_sort_v2
from Quick_sort_DOH_v1 import quick_celek
from merge_sort import split_merge
#Ruzne velke seznamy s nahodne serazenymi cisly

measure_lenghts = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500]
#measure_lenghts = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

#jeden seznam pro jeden sort
def jeden_seznam(algoritmus, list_lenght):
    test_seznam = list(range(list_lenght))
    random.shuffle(test_seznam)
    return algoritmus(test_seznam)[1]

#vsechny seznamy pro jeden sort
def cely_seznam(algoritmus):
    vysledek = []
    for list_lenght in measure_lenghts:
        vysledek.append(jeden_seznam(algoritmus, list_lenght))
    return vysledek


#graficke zobrazeni efektivity funkce
plt.plot(measure_lenghts, cely_seznam(bubble_sort_normal), label="Bubble_v1", color="#1B17F3")
plt.plot(measure_lenghts, cely_seznam(bubble_sort_s_detekci), label="Bubble_v2", color="#1D7E09")
plt.plot(measure_lenghts, cely_seznam(bubble_sort_kratsi_rozsah), label="Bubble_v3", color="#A7100B")
plt.plot(measure_lenghts, cely_seznam(cocktail_sort), label="Bubble_v4", color="#C7760B")
plt.plot(measure_lenghts, cely_seznam(insertion_sort), label="Insertion", color="#C4076F")
plt.plot(measure_lenghts, cely_seznam(selection_sort), label="Select", color="#00FFBF")
plt.plot(measure_lenghts, cely_seznam(shell_sort), label="Shell", color="#000000")
plt.plot(measure_lenghts, cely_seznam(shell_sort_v2), label="Shell_v2", color="#301A30")
plt.plot(measure_lenghts, cely_seznam(quick_celek), label ="Quick", color="#02283A")
plt.plot(measure_lenghts, cely_seznam(split_merge), label="Merge", color="#304E29")

plt.style.use('dark_background')



plt.legend()
plt.show()