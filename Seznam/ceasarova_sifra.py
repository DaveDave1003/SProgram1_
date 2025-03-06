#abeceda = 26 prvků (písmen), klíč je hodnota posunu "o něco"  (klic=2 => (A = C))


text = input("Zadejte text k zašifrování: ")

klic = int(input("Zadejte klíč: "))

abeceda = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

zasifrovany_text = ""

for znak in text:
    if znak in abeceda:
        for i in range(len(abeceda)):
            if znak == abeceda[i]:
                novy_znak = abeceda[(i + klic)% len(abeceda)]
                zasifrovany_text += novy_znak

print(zasifrovany_text)

#dešifrování
puvodni_text = ""
for znak in zasifrovany_text:
    if znak in abeceda:
        for i in range(len(abeceda)):
            if znak == abeceda[i]:
                novy_znak = abeceda[(i-klic)% len(abeceda)]
                puvodni_text += novy_znak

print(puvodni_text)