n=int(input())
c=0
m=list(map(int,input().split()))
k=set(m)
l=list(k)
for i in range(len(l)):
    if l[i]%2==1:
        c+=1
print(c)