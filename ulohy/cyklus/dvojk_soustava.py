def do_dvojkove(n):
    if n == 0:
        return 0
    

    vysledek = "" 

    while n > 0:
        zbytek = n % 2
        vysledek = str(zbytek) + vysledek
        n = n//2
        
    return vysledek





print(do_dvojkove(0))    # → '0'
print(do_dvojkove(5))    # → '101'
print(do_dvojkove(10))   # → '1010'
print(do_dvojkove(255))  # → '11111111'