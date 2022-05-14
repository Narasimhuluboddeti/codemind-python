n=int(input())
c=0
s=0
m=list(map(int,input().split()))
for i in range(len(m)):
    if i%2==0:
        c+=m[i]
for j in range(len(m)):
    if j%2==1:
        s+=m[j]
if c-s==0:
    print("YES")
else:
    print("NO")
    