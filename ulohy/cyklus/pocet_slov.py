def pocet_slov(text):
    if text == "":
        return 0
    
    pocet = 0
    ve_slovo = False


    for znak in text:
        if znak != " " and ve_slovo == False:
            pocet += 1
            ve_slovo = True

        elif znak == " ":
            ve_slovo = False

        
    return pocet











print(pocet_slov('    ahoj   '))
print(pocet_slov(' '))
print(pocet_slov('Python'))
print(pocet_slov('   Ahoj světe  '))