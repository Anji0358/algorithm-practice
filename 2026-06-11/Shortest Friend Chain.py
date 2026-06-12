from collections import deque

N,M=map(int,input().split())
S,T=map(int,input().split())

q=deque()
dist[S]=0
q.append(S)

while q:
    v=q.popleft()

    for nv in G[v]:
        if dist[nv]!=-1:
            continue

        dist[nv]=dist[v]+1
        q.append(nv)

