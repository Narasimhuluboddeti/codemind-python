n=int(input())
m=list(map(int,input().split()))
k=set(m)
l=list(k)
c=0
for i in range(len(l)):
    if l[i]%2==1:
        c+=1
print(c)