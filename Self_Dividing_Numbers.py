n=int(input())
m=int(input())
for i in range(n,m+1):
    l=len(str(i))
    t=i
    s=0
    c=0
    while i!=0:
        r=i%10
        if(r==0):
            pass
        elif t%r==0:
            c+=1
        i//=10
    if c==l:
        print(t,end=" ")