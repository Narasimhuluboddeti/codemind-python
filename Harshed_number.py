n=int(input())
t=n
s=0
while n!=0:
    r=n%10
    s=s+r
    n//=10
if t%s==0:
    print("True")
else:
    print("False")