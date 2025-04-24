def je_palindrom_v1(slovo):

    slovo = slovo.lower()

    return slovo == slovo [ : : -1]



def je_palindrom_v2(slovo):
    slovo = slovo.lower()

    for i in range(len(slovo) //2):
        if slovo[i] == slovo[len(slovo) - 1 - i]:
            return false
    
    return true


# print(je_palindrom_v1("madam"))
print(je_palindrom_v2("madam"))