N,Q=map(int,input().split())

parents=[i for i in range(N)]

def find(x):
    if parents[x]!=x:
        parents[x]=find(parents[x])
    return parents[x]

def union(a,b):
    ra=find(a)
    rb=find(b)

    if ra==rb:
        return
    else:
        parents[rb]=ra

for j in range(len(Q)):
    opt,a,b=map(int,input().split())

    if opt==1:
        union(a,b)
    
    else:
        if find(a)==find(b):
            print("Yes")
        else:print("No")

"""
N, Q = map(int, input().split())

parents = [i for i in range(N)]
size = [1] * N

def find(x):
    if parents[x] != x:
        parents[x] = find(parents[x])
    return parents[x]

def union(a, b):
    ra = find(a)
    rb = find(b)

    if ra == rb:
        return

    if size[ra] < size[rb]:
        ra, rb = rb, ra

    parents[rb] = ra
    size[ra] += size[rb]

for _ in range(Q):
    opt, a, b = map(int, input().split())
    a -= 1
    b -= 1

    if opt == 1:
        union(a, b)
    else:
        print("Yes" if find(a) == find(b) else "No")
"""