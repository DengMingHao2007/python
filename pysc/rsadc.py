N = int(input("Please enter N:"))
D = int(input("Please enter D:"))
num = input("Please enter the encrypted data(Use ',' to Separate):")
data = [int(n) for n in num.split(",")]


#密文的D次幂
for i in range(len(data)):
    data[i]=pow(data[i],D)

#与N取余
for i in range(len(data)):
    data[i]=data[i]%N

#ascii数组转原文数组
for i in range(len(data)):
    data[i]=chr(data[i])
#数组转字符串并打印
print("".join(data))