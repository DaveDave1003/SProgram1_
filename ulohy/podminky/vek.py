def urci_kategorii(X):
    if 0 <= X and X <= 12:
        return "Dítě"
    elif 13 <= X and X <= 17:
        return "Mladistvý"
    elif 18 <= X and X <= 64:
        return "Dospělý"
    elif 65 <= X:
        return "Senior" 
    


print(urci_kategorii(5))
print(urci_kategorii(17))
print(urci_kategorii(25))
print(urci_kategorii(67))