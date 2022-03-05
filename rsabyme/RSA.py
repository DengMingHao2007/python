L = 80
E=19
D=2

for i in range(79):
    tmp = E*D
    if tmp%L == 1:
        print(D)
    else:
        D+=1 