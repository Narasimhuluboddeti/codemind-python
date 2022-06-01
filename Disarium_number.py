n=int(input())
t=n
s=0
c=0
x=0
i=1
while n!=0:
    r=n%10
    s=s*10+r
    c=c+1
    n=n//10
for i in range(i,c+1,1):
    m=s%10
    x=x+m**i
    s=s//10
if t==x:
    print("True")
else:
    print("False")