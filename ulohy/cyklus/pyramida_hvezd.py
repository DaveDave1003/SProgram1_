def pyramida(n):
    vysledek = ""

    for i in range(n):
        mezery = n - i - 1
        hvezdy = 2 * i + 1

        radek = " " * mezery + "*" * hvezdy
        vysledek += radek + "\n"

    return vysledek


print(pyramida(3))
print(pyramida(7))