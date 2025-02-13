#Pokud postupně nahrazujeme číslo součtem druhých mocnin jeho číslic, skončíme u 1

import math

for number in range(1,100):
    temp_result = 0
    temp_number= number

    while temp_number != 1 or temp_number != 4:
        temp_result = 0
        for digit in str(temp_number):
            print(f"{temp_number}")
            temp_result += int(digit) ** 2
        temp_number = temp_result 

    if temp_number == 1:
        print(f"Číslo {temp_number} je šťastné")