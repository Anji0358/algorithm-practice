N,A,B=int(input())

def calc_sum(n):
    sum=0
    i=n
    while(n>0):
        sum+=n%10
        n/10
    return sum


sum=0
for i in range(N):
    if(A<=calc_sum(N)<=B):
        sum+=i

print(sum)

"""
N, A, B = map(int, input().split())

1 から N まで調べたい場合は、

range(1, N + 1)
"""