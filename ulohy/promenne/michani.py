V_1 = int(input("Zadejte množství v ml: "))
C_1 = int(input("Jakou má roztok koncentraci v %: "))
V_2 = int(input("Zadejte množství v ml: "))
C_2 = int(input("Jakou má roztok koncentraci v %: "))

C = (V_1 * C_1 + V_2 * C_2) / (V_1 + V_2)


print(f"Koncentrace: {round(C, 2)} %")