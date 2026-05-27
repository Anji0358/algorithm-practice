from collections import deque
N,M,K=map(int,input().split())
H=list(map(int,input().split()))

G=[[] for _ in range(N)]

for _ in range(M):
    a,b=map(int,input().split())
    a-=1
    b-=1
    G[a].append(b)
    G[b].append(a)

q=deque()
q.append(1)
dist=[-1]*N
dist[0]=1

while q:
    v=q.popleft()
    for nv in G[v]:
        if dist[nv]!=-1:
            continue

        dist[nv]=dist[v]+1
        q.append(nv)
    
flag=False
for h in range(H):
    if dist[h]!=-1:
        flag=True
        break

if flag:
    for h in range(H):
        print(dist[h]+" ")
else:print(-1)

"""
from collections import deque

N, M, K = map(int, input().split())

H = [x - 1 for x in map(int, input().split())]

G = [[] for _ in range(N)]

for _ in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    G[a].append(b)
    G[b].append(a)

dist = [-1] * N
q = deque()

for h in H:
    dist[h] = 0
    q.append(h)

while q:
    v = q.popleft()

    for nv in G[v]:
        if dist[nv] != -1:
            continue

        dist[nv] = dist[v] + 1
        q.append(nv)

print(*dist)
"""
