a,b=map(int,input().split())
while b:
    if a>b:
        a,b=b,a
    b=b%a
print(a)