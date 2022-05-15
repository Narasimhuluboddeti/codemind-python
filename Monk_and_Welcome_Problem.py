n=int(input())
m=list(map(int,input().split()))
k=list(map(int,input().split()))
for i in range(len(m)):
    m[i]=m[i]+k[i]
print(*m)
    