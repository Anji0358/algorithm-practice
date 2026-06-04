N,Q=map(int,input().split())

parents=[i for i in range(N)]

size=[1]*N

def find(x):
    if parents[x]!=x:
        parents[x]=parents[find(x)]
        
    return parents[x]

"""
def find(x):
    if parents[x] != x:
        parents[x] = find(parents[x])
    return parents[x]
"""

def union(a,b):
    ra=a-1
    rb=b-1

    if find(a)==find(b):
        return 
    
    if size[ra]<size[rb]:
        ra,rb=rb,ra
    
    parents[rb]=ra
    size[ra]+=size[ra]

for _ in range(Q):
    opt,a,b=map(int,input().split())

    if a==1:
        union(a,b)
    else:
        print(size[a])

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
    query = list(map(int, input().split()))

    if query[0] == 1:
        _, a, b = query
        a -= 1
        b -= 1
        union(a, b)

    else:
        _, x = query
        x -= 1
        root = find(x)
        print(size[root])
"""