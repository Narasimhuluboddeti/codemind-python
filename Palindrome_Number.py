a=int(input())
for i in range(a):
    n=int(input())
    t=n
    s=0
    while n!=0:
        r=n%10
        s=s*10+r
        n=n//10
    if s==t:
        print("True")
    else:
        print("False")