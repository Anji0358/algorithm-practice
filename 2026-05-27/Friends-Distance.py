from collections import deque

N,M=map(int,input().split())
G=[[] for _ in range(N)]

for _ in range(M):
    a,b=map(int,input().split())
    a-=1
    b-=1
    G[a].append(b)
    G[b].append(a)

dist=[-1]*N
dist[0]=0
q=deque(0)

while q:
    v=q.popleft()

    for nv in G[v]:

        if dist[nv]!=-1:
            continue

        dist[nv]=dist[v]+1
        q.append(nv)

print(dist[N-1])