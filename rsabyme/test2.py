import base64
p = int(input("Please enter two prime numbers(1/2):"))
q = int(input("Please enter two prime numbers(2/2):"))
data = input("Please enter the original data:")
N=p*q

a = p - 1
b = q - 1

#求p-1与q-1的最小公倍数L
for i in range(min(a,b),0,-1):
    if a % i ==0 and b % i == 0:
        L = a*b//i
        break

#求E
tmp = 1
n = 0
while n != 1:
    tmp+=1
    m = max(tmp, L)
    n = min(tmp, L)
    r = m % n
    while r != 0:
        m = n
        n = r
        r = m % n
E = tmp
D = 2
while E * D % L != 1:
    D+=1

#加密程序主体

#原始字符转ascii数组
lst = list(data)
for i in range(len(lst)):
    lst[i]=base64.b64encode(lst[i].encode())

print(list(lst))

#ascii数组的E次幂
for i in range(len(lst)):
    lst[i]=pow(lst[i],E)

#与N取余
for i in range(len(lst)):
    lst[i]=lst[i]%N

print("N:",N,"D:",D)
print(lst)