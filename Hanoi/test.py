def f(n):
    if n==0:
        return 0
    else:
        return 2*f(n-1)+1
x=int(input("Pieces："))
print("Times:",f(x))