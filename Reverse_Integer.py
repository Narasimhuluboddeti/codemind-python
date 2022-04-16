n=int(input())
t=n
c=0
if n<1:
    n=n*-1
    c+=1
t=n
s=0
while n!=0:
    r=n%10
    s=s*10+r
    n//=10
if c==1:
    print(-s)
else:
    print(s)