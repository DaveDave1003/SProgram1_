import linear_regrese




x= []
y= []


#bod_nula_x=x.append(0)
#bod_nula_y=y.append(0)

bod_A_x= x.append(int(input("Zvol x bodu A: ")))
bod_A_y= y.append(int(input("Zvol y bodu A: ")))

bod_B_x= x.append(int(input("Zvol x bodu B: ")))
bod_B_y= y.append(int(input("Zvol y bodu B: ")))

bod_C_x= x.append(int(input("Zvol x bodu C: ")))
bod_C_y= y.append(int(input("Zvol y bodu C: ")))

print(x)
print(y)


def costfunction(k):
    sum= 0
    for i in range(len(x)):
        sum += (y[i] - k*x[i])**2
    return 1/len(x) * sum


for i in range (-5, 5, 1):
    print(f"k: {i}, Cost function je : {costfunction(i)}")