#Nalezení nejmenší společného dělitele (A : B)

def nejmensi_delitel(A, B):
    
    if B == 0:
        return A
    else:
        return nejmensi_delitel(B, A % B)
    

#print(nejmensi_delitel(10, 0))

#print(nejmensi_delitel(48, 18))
#print(nejmensi_delitel(252, 105))


#BONUS - Josefův problém - losováním - kde stát 

# N = počet lidí
# K = posun o K



def losovani(N, K):
    pocet_lidi= []

    for i in range(N):
        pocet_lidi.append(i+1)

    if N == 1:
        return 0
    
    else:
        return (losovani(N - 1, K) + K) % N
    

    
    

    
    





print(losovani(512, 51) + 1)