def nejdelsi_serie(s):
    if s == "":
        return 0
    

    actual = 1
    maximum = 1
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            actual += 1
        else:
            actual = 1

        if actual > maximum:
            maximum = actual
        


    return maximum

print(nejdelsi_serie('aaabbdddd'))