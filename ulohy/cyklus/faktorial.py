def faktorial(hodnota):
    faktorial = 1
    if hodnota == 0:
        return "1"
    
    
    for i in range(1, hodnota+1):
        faktorial *= i

    return faktorial

print(faktorial(0))
print(faktorial(3))
print(faktorial(5))