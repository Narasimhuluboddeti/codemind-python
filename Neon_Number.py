n=int(input())
t=n
m=n*n
s=0
while(m!=0):
    r=m%10
    s+=r
    m//=10
if s==n:
    print("Neon Number")
else:
    print("Not Neon Number")