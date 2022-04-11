n=int(input())
t=n
s=1
k=0
while(n!=0):
    r=n%10
    s=s*r
    k+=r
    n=n//10
    m=s-k
print(m)
    
    