n=int(input())
m=list(map(int,input().split()))
s=sum(m)//len(m)
if s in m:
    print("True")
else:
    print("False")
    