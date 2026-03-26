def eratosthenovo_sito(n):
    if n < 2:
        return []
    
    # Vytvoříme seznam, kde index reprezentuje číslo
    # True = zatím považujeme za prvočíslo
    sito = [True] * (n + 1)
    sito[0] = sito[1] = False  # 0 a 1 nejsou prvočísla
    
    for i in range(2, int(n ** 0.5) + 1):
        if sito[i]:
            # Označíme všechny násobky i jako složené
            for j in range(i * i, n + 1, i):
                sito[j] = False
    
    # Vybereme čísla, která zůstala označená jako prvočísla
    return [i for i in range(2, n + 1) if sito[i]]

    
# Příklad použití
print(eratosthenovo_sito(10))   # Očekávaný výstup: [2, 3, 5, 7]
print(eratosthenovo_sito(20))   # Očekávaný výstup: [2, 3, 5, 7, 11, 13, 17, 19]
print(eratosthenovo_sito(1))    # Očekávaný výstup: []