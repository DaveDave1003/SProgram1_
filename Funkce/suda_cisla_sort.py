

def vypis_suda_od_do(a,b):
    
    suda = []
    
    if b > a:
        for i in range(a,b+1):
            if i % 2 == 0:
             suda.append(i)
    else:
       return "chyba"
    
    return suda
            
a= int(input("kolik je A: "))
b= int(input("kolik je B: "))

print(vypis_suda_od_do(a,b))