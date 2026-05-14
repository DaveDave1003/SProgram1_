def typ_znaku(z):
    
    for znak in z:
        if znak.islower():
            return "malé písmeno"
        
        elif znak.isupper():
            return "velké písmeno"
        
        elif znak.isdigit():
            return "Číslice"

        elif not znak.isalnum() or not znak.isspace():
            return "speciální znak"
        


print(typ_znaku('a'))
print(typ_znaku('A'))
print(typ_znaku('5'))
print(typ_znaku('!'))
print(typ_znaku(' '))