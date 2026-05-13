S = int(input("Zadejte vzdálenost v kilometrech: "))

T_h = int(input("Doba jízdy v hodinách: "))
T_min = int(input("Doba jízdy v minutách: "))

time = T_h + (T_min / 60) 
avg_v = S / time

print(f"Průměrná rychlost {round(avg_v, 2)} km/h")