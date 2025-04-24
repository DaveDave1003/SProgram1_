



def prevod_na_minuty(hodiny, int):
   
   if not isinstance(hodiny, int):
        return None

    if not isinstance(minuty,int):
        return None
    
    
    if hodiny < 0 or minuty < 0:
        return None

    celkem_minut = hodiny * 60 + minuty
    return celkem_minut

print(prevod_na_minuty(1,20))

   
    


