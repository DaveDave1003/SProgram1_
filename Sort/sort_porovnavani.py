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

#Ruzne velke seznamy s nahodne serazenymi cisly
measure_lenghts = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000, 2100, 2200, 2300, 2400, 2500, 2600, 2700, 2800, 2900, 3000]

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
plt.plot(measure_lenghts, cely_seznam(bubble_sort_normal), label="Normal", color="#1B17F3")
plt.plot(measure_lenghts, cely_seznam(bubble_sort_s_detekci), label="Detection", color="#1D7E09")
plt.plot(measure_lenghts, cely_seznam(bubble_sort_kratsi_rozsah), label="Short", color="#A7100B")
plt.plot(measure_lenghts, cely_seznam(cocktail_sort), label="Cocktail", color="#C7760B")
plt.plot(measure_lenghts, cely_seznam(insertion_sort), label="Insertion", color="#C4076F")
plt.plot(measure_lenghts, cely_seznam(selection_sort), label="Selec", color="#00FFBF")
plt.plot(measure_lenghts, cely_seznam(shell_sort), label="Shell", color="#000000")

plt.legend()
plt.show()