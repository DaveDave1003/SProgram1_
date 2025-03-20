
Johan = {"jmeno": "Jonáš", "barva": "běloch", "vyska": "záprtek"}

print (Johan.values())

Johan["pohlavi"] = "nevim"

for klic, hodnota in Johan.items():
    print(f"{klic}: {hodnota}")
