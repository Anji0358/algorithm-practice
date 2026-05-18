N=int(input())
S=input()

cnt=0
for i in range(1,N+1):
    if(S[i]=="a"):cnt+=1

print(cnt)


##print(S.count("a"))