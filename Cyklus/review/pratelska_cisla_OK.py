#jsou čísla, kde součet dělitelů jednoho čísla (krom sama sebe) se rovná druhému čísli a naopak

import math

for number in range (1,10000):

    temp_result_1= 0
    temp_result_2= 0

    for i in range (1,number):
        if number % i == 0 :
            temp_result_1 += i
    for i in range(1, temp_result_1):
        if temp_result_1 % i == 0:
            temp_result_2 += i
    
    if number == temp_result_2 and number != temp_result_1:
        print(f"{number} <-> {temp_result_1} - jsou přátelská čísla")


