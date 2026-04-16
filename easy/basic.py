# 01
"""
A,B=map(int,input().split())
print(A*B)
"""
# 02
"""
a,b=map(int,input().split())
if(a*b)%2==0:
    print("even number")
else:
    print("odd number")

"""
#Fiz Buzz
"""
a=input()
a=int(a)
for i in range(1,a+1):
    if i%3==0 and i%5==0:
         print("fizbuzz")
    elif i%3==0:
        print("fizz")
    elif i%5==0:
        print("buzz")
    else:
        print(i)
"""
#03
"""
H,A=map(int,input().split())
if H%A==0:
    print(H//A)
else:
    print(H//A+1)
"""
#04
"""
K=input()
K=int(K)
A,B=map(int,input().split())
exsist=False
for n in range(A,B+1):
    if n%K==0 :
        exsist=True

print("ok" if exsist else "NG")
"""
#05
"""
N,A,B=map(int,input().split())
total=0
for i in range(1,N+1):
    sum=0
    tmp=i
    while tmp!=0:
        sum+=tmp%10
        tmp=tmp//10
    
    if sum>=A and B>=sum:
        total+=i
print(total)
"""

#06
"""
N=int(input())
A=list(map(int,input().split()))
cnt=0
flag=True
while flag:
    for i in range(0,N):
        if A[i]%2!=0:
            flag=False
    if flag:
        for i in range(N):
            A[i] //= 2
        cnt+=1
print(cnt)
"""
"""
#別解
def func(num):
    cnt=0
    while num%2==0:
        num=num//2
        cnt+=1
    return cnt

N=int(input())
A=list(map(int,input().split()))
result=min(map(func,A))
print(result)
"""
#07
""""""
N=int(input())
a=list(map(int,input().split()))
sum=0
a.sort(reverse=True)

for i in range(0,N):
    if i%2==0:
        sum+=a[i]
    else:
        sum-=a[i]

print(sum)