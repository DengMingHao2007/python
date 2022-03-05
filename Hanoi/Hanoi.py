def hanoi(n,x,y,z):
    global times
    if n == 1:
        times += 1
        print(x,"-->",z)
    else:
        times += 1
        hanoi(n-1,x,z,y)
        print(x,"-->",z)
        hanoi(n-1,y,x,z)
times=0
n=int(input("Pieces:"))
hanoi(n,"X","Y","Z")
print("Times:",times)