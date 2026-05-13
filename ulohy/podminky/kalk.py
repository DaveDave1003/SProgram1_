def kalkulacka(A,B,O):
    if O == "+":
        plus = A+B
        return(plus)
    elif O == "-":
        minus = A-B
        return(minus)
    elif O == "*":
        mult = A*B
        return(mult)
    elif O == "/":
        if B == 0:
            return("nelze dělit 0")
        else:
            div = A/B
            return(div)
    else:
        return("Neznámá operace")








A = int(input("Zadej hodnotu A: "))
B = int(input("Zadej hodnotu B: "))
O = input("Operace (+,-,*,/): ")

print(kalkulacka(A,B,O))
