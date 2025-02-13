#https://gjs-education.vercel.app/seminare/prog1/python/seznamy/modifikace-seznamu



E = [2, 3, 1, 0, 5, 6, 4]


nejv = 0
nejm = 0
soucet = 0

for x in E:
    soucet += x
    
    if x > nejv:
        nejv = x
    
    if x < nejm:
        nejm = x
prumer = soucet / len(E)

print(nejv, nejm, prumer)







