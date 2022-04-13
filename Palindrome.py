n=int(input())
temp=n
s=0
while(n!=0):
    r=n%10
    s=s*10+r
    n//=10
if s==temp:
    print("True")
else:
    print("False")