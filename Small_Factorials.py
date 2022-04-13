n=int(input())
for i in range(1,n+1):
    k=int(input())
    c=1
    for j in range(1,k+1):
        c*=j
    print(c)