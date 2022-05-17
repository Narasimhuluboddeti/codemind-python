n=int(input())
m=list(map(int,input().split()))
c=0
k=set(m)
l=list(k)
for i in range(len(l)):
    if l[i]%2==1:
        c+=l[i]
print(c)