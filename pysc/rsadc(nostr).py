N = int(input("Please enter N:"))
D = int(input("Please enter D:"))
num = int(input("Please enter the encrypted number:"))


#密文的D次幂
num = pow(num,D)

#与N取余
num=num%N

print(num)