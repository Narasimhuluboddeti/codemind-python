n=int(input())
c=[]
m=list(map(int,input().split()))
for i in range(len(m)):
    k=m[i]*m[i]
    c.append(k)
c.sort()
print(*c)
