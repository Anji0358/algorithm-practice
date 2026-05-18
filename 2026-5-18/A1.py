N=int(input())
A=list(map(int,input().split()))

cnt=0
while(1):
    for i in range(N):
        if(A[i]%2==1):A[i]/=2
        break
    print(A)
    count+=1

print(cnt)

"""
1. AtCoderでは整数として扱いたいことが多いので、整数のまま割りたい場合は // を使う。
2. while True:
    処理

    if 終了条件:
        break
3. all() の使い方

all() は、すべての条件が True のときに True を返す。
例：

numbers = [2, 4, 6]

print(all(x % 2 == 0 for x in numbers))

出力：

True
"""