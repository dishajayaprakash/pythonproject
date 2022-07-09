import math
n=int(input("enter n value: "))
sum=0
sum1=0
for i in range(1,n+1):
    sum1=math.pow(n,n)
    sum+=sum1/n
print(sum)
