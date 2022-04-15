n=int(input())
m=int(input())
for i in range(n,m+1):
    s=0
    t=i
    while(t!=0):
        r=t%10
        s=s*10+r
        t//=10
    if i==s:
        print(s,end=" ")
        