C = int(input("Zadejte teplotu v Celsiích: "))

#Kelviny
K = C + 273.15


#Fahrenheity
F = (9/5) * C + 32

print (f"{round (K, 2)} K, {round(F, 2)} °F")