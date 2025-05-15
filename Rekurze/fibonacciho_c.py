



def fibonacciho_cislo(n):
    if n == 0:
        return 0

    if n == 1:
        return 1

    return fibonacciho_cislo(n-1) + fibonacciho_cislo(n-2)

n = int(input(f"Jaké číslo: "))

print(fibonacciho_cislo(n))